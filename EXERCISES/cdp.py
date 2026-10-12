#!/usr/bin/env python3
"""CDP probe — read/eval/screenshot the Pine IDE page directly.

The window capture (`import -window`) can hand back a stale buffer, and the IDE's own
status row can disagree with the engine. This talks to the page itself so a claim is
made against the page's real state.

Usage:
  python3 cdp.py eval '<js expression>'      # print the JSON result
  python3 cdp.py shot /tmp/out.png           # Page.captureScreenshot (real page pixels)
  python3 cdp.py info                        # title/url of the page target
"""
from __future__ import annotations
import base64
import json
import sys
import urllib.request

import websocket  # websocket-client

CDP = "http://127.0.0.1:9222"


def page_ws() -> str:
    with urllib.request.urlopen(f"{CDP}/json/list", timeout=5) as r:
        targets = json.load(r)
    for t in targets:
        if t.get("type") == "page" and "pine.html" in (t.get("url") or ""):
            return t["webSocketDebuggerUrl"]
    raise SystemExit(f"NO_PAGE_TARGET: {[t.get('url') for t in targets]}")


class _C:
    def __init__(self, url: str):
        self.ws = websocket.create_connection(url, timeout=180)
        self.i = 0

    def call(self, method: str, params: dict | None = None):
        self.i += 1
        self.ws.send(json.dumps({"id": self.i, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.i:
                if "error" in msg:
                    raise SystemExit(f"CDP_ERROR: {msg['error']}")
                return msg.get("result", {})

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd = sys.argv[1]
    c = _C(page_ws())
    try:
        if cmd == "info":
            r = c.call("Runtime.evaluate", {"expression": "JSON.stringify({title:document.title,url:location.href})",
                                            "returnByValue": True})
            print(r["result"]["value"])
        elif cmd == "eval":
            expr = sys.argv[2]
            r = c.call("Runtime.evaluate", {"expression": expr, "returnByValue": True,
                                            "awaitPromise": True, "userGesture": True})
            res = r.get("result", {})
            if res.get("subtype") == "error":
                print("EVAL_ERROR:", res.get("description"))
                return 1
            v = res.get("value")
            print(v if isinstance(v, str) else json.dumps(v, indent=2))
        elif cmd == "shot":
            out = sys.argv[2]
            r = c.call("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})
            with open(out, "wb") as f:
                f.write(base64.b64decode(r["data"]))
            print(f"shot {out}")
        else:
            print(f"unknown command: {cmd}")
            return 2
    finally:
        c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

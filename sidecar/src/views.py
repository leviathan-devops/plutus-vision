#!/usr/bin/env python3
"""views.py — MECHANICAL step `prepare_views` (no model).

Detects the table grid of an investinglive FX-option-expiry JPEG (black grid
lines) and writes deterministic PNG views for the model reads:

  A   full table, zoom so the longest side is <= 1980 px
  B1  label column + first half of the pair columns, zoom 4x (cut on grid lines)
  B2  label column + second half of the pair columns, zoom 4x
  C<i> label column + pair column i only, zoom up to 6x (tie-break read)

usage: views.py <image.jpg> <outdir>   -> prints a JSON manifest on stdout
Same input bytes -> same output bytes (Pillow LANCZOS, no timestamps).
"""
import json, os, sys
from PIL import Image
import numpy as np

MAXDIM = 1980  # the gateway model entry resizes images above 2000 px


def runs(mask):
    """Collapse consecutive True indices into (start, end) runs."""
    out, start = [], None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        if not v and start is not None:
            out.append((start, i - 1)); start = None
    if start is not None:
        out.append((start, len(mask) - 1))
    return out


def grid(img):
    a = np.asarray(img.convert("L"), dtype=np.int16)
    dark = a < 70
    h, w = dark.shape
    vfrac = dark.sum(axis=0) / h
    hfrac = dark.sum(axis=1) / w
    vl = [int((s + e) // 2) for s, e in runs(vfrac > 0.55)]
    hl = [int((s + e) // 2) for s, e in runs(hfrac > 0.55)]
    return vl, hl


def save(img, box, scale, path):
    c = img.crop(box)
    scale = min(scale, MAXDIM / max(c.size))
    c = c.resize((max(1, round(c.size[0] * scale)), max(1, round(c.size[1] * scale))), Image.LANCZOS)
    c.save(path, format="PNG", optimize=False)
    return {"file": os.path.basename(path), "box": list(box), "scale": round(scale, 4), "size": list(c.size)}


def compose(img, label_box, part_box, scale, path):
    """Label column glued to an arbitrary column range (same rows)."""
    lab = img.crop(label_box)
    part = img.crop(part_box)
    canvas = Image.new("RGB", (lab.size[0] + part.size[0], lab.size[1]), (255, 255, 255))
    canvas.paste(lab, (0, 0)); canvas.paste(part, (lab.size[0], 0))
    scale = min(scale, MAXDIM / max(canvas.size))
    c = canvas.resize((round(canvas.size[0] * scale), round(canvas.size[1] * scale)), Image.LANCZOS)
    c.save(path, format="PNG", optimize=False)
    return {"file": os.path.basename(path), "label_box": list(label_box), "box": list(part_box),
            "scale": round(scale, 4), "size": list(c.size)}


def main():
    src, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    img = Image.open(src).convert("RGB")
    w, h = img.size
    vl, hl = grid(img)
    man = {"source": os.path.basename(src), "size": [w, h], "vlines": vl, "hlines": hl, "views": {}}
    man["views"]["A"] = save(img, (0, 0, w, h), 2.2, os.path.join(outdir, "A.png"))
    # vertical lines: [left edge of label col, label|pair1, pair1|pair2, ..., right edge]
    ok = len(vl) >= 4 and len(hl) >= 3
    man["grid_ok"] = ok
    if ok:
        npairs = len(vl) - 2
        man["pair_columns"] = npairs
        top, bot = max(0, hl[0] - 3), min(h, hl[-1] + 4)
        label_box = (max(0, vl[0] - 30), top, vl[1] + 1, bot)  # keep the arrow margin
        half = (npairs + 1) // 2
        man["views"]["B1"] = compose(img, label_box, (vl[1], top, vl[1 + half] + 2, bot), 4.0, os.path.join(outdir, "B1.png"))
        man["views"]["B1"]["pair_index"] = list(range(0, half))
        man["views"]["B2"] = compose(img, label_box, (vl[1 + half], top, min(w, vl[-1] + 3), bot), 4.0, os.path.join(outdir, "B2.png"))
        man["views"]["B2"]["pair_index"] = list(range(half, npairs))
        for i in range(npairs):
            v = compose(img, label_box, (vl[1 + i], top, min(w, vl[2 + i] + 2), bot), 6.0, os.path.join(outdir, f"C{i}.png"))
            v["pair_index"] = [i]
            man["views"][f"C{i}"] = v
    json.dump(man, open(os.path.join(outdir, "views.json"), "w"), indent=1, sort_keys=True)
    print(json.dumps(man, sort_keys=True))


if __name__ == "__main__":
    main()

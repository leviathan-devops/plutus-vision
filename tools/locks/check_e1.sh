#!/usr/bin/env bash
# ENGINE 1 LOCK (operator M-67 / L-62: "lock that immutable. Do not touch anything about Engine 1 at all whatsoever").
# Checks the working tree AND the staged index against tools/locks/E1.sha256; exit 1 on any difference.
# Called by tools/git-hooks/pre-commit on every commit; run by hand as a gate (memory/16_PLAN_M67.md G5).
root="$(git rev-parse --show-toplevel)"; cd "$root" || exit 1
bad=0
while read -r sum path; do
  [ -z "$path" ] && continue
  w=$(sha256sum "$path" 2>/dev/null | cut -d' ' -f1)
  s=$(git show ":$path" 2>/dev/null | sha256sum | cut -d' ' -f1)
  if [ "$w" != "$sum" ]; then echo "E1 LOCK: working tree differs: $path" >&2; bad=1; fi
  if [ "$s" != "$sum" ]; then echo "E1 LOCK: staged copy differs: $path" >&2; bad=1; fi
done < tools/locks/E1.sha256
if git diff --cached --name-only | grep -qx 'tools/locks/E1.sha256'; then
  if ! git diff --cached --quiet HEAD -- tools/locks/E1.sha256 2>/dev/null && git cat-file -e HEAD:tools/locks/E1.sha256 2>/dev/null; then
    echo "E1 LOCK: the lock file itself is being changed - refused" >&2; bad=1
  fi
fi
[ $bad -eq 0 ] && echo "E1 lock: clean ($(wc -l < tools/locks/E1.sha256) files)"
exit $bad

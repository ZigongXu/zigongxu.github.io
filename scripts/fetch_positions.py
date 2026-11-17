#!/usr/bin/env python3
"""Fetch heliocentric positions of my missions from NASA/JPL Horizons.

Writes a small JSON file used by the homepage mission map: positions in the
ecliptic plane (J2000, x toward the vernal equinox, viewed from the north),
in au, for a window of +/- WINDOW_DAYS around today (UTC).

Runs during every website build (see .github/workflows/deploy.yml), which is
also scheduled daily, so the map always opens on today's real positions.
Standard library only. If Horizons cannot be reached, the script exits
non-zero, writes nothing, and the map falls back to its schematic orbits.

Usage: python3 scripts/fetch_positions.py static/data/spacecraft.json
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://ssd.jpl.nasa.gov/api/horizons.api"
WINDOW_DAYS = 180
# key: (Horizons id, step in hours). PSP moves fast near perihelion: finer step.
BODIES = {
    "psp": ("-96", 6),     # Parker Solar Probe
    "solo": ("-144", 24),  # Solar Orbiter
    "earth": ("399", 24),  # Earth
}


def fetch(command, start, stop, step_h):
    params = {
        "format": "json",
        "COMMAND": f"'{command}'",
        "OBJ_DATA": "'NO'",
        "MAKE_EPHEM": "'YES'",
        "EPHEM_TYPE": "'VECTORS'",
        "CENTER": "'500@10'",          # Sun body centre
        "REF_PLANE": "'ECLIPTIC'",
        "REF_SYSTEM": "'ICRF'",
        "START_TIME": f"'{start:%Y-%m-%d}'",
        "STOP_TIME": f"'{stop:%Y-%m-%d}'",
        "STEP_SIZE": f"'{step_h} h'",
        "VEC_TABLE": "'1'",
        "OUT_UNITS": "'AU-D'",
        "CSV_FORMAT": "'YES'",
        "VEC_LABELS": "'NO'",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                result = json.load(r)["result"]
            break
        except Exception as e:  # network hiccup: retry
            if attempt == 2:
                raise
            print(f"retry {command}: {e}", file=sys.stderr)
            time.sleep(5)
    if "$$SOE" not in result:
        raise RuntimeError(f"Horizons returned no ephemeris for {command}:\n{result[:500]}")
    rows = result.split("$$SOE")[1].split("$$EOE")[0].strip().splitlines()
    xy = []
    for row in rows:
        f = [c.strip() for c in row.split(",")]
        # JDTDB, Calendar date, X, Y, Z
        xy += [round(float(f[2]), 5), round(float(f[3]), 5)]
    return xy


def main(out):
    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    start, stop = today - timedelta(days=WINDOW_DAYS), today + timedelta(days=WINDOW_DAYS)
    data = {
        "source": "NASA/JPL Horizons",
        "frame": "heliocentric ecliptic J2000, au",
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "start": start.strftime("%Y-%m-%d"),
        "bodies": {},
    }
    for key, (cmd, step_h) in BODIES.items():
        xy = fetch(cmd, start, stop, step_h)
        data["bodies"][key] = {"step_days": step_h / 24, "xy": xy}
        print(f"{key}: {len(xy) // 2} positions", file=sys.stderr)
    with open(out, "w") as f:
        json.dump(data, f, separators=(",", ":"))
    print(f"wrote {out}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "static/data/spacecraft.json")

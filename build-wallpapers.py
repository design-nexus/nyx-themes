#!/usr/bin/env python3
"""Render the Omarchy vector wordmark in each Nyx theme's accent and background."""
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

THEMES = {
    "nyx-dark": ("#0d0e12", "#3d8ae8"),
    "nyx-light": ("#ecedf2", "#136dcd"),
}

root = Path(__file__).resolve().parent
ET.register_namespace("", "http://www.w3.org/2000/svg")

for theme, (background, accent) in THEMES.items():
    group = next(iter(ET.parse(root / "wordmark.svg").getroot()))
    group.set("fill", accent)
    group.set("transform", "translate(1120 892) scale(1.316872427983539)")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160">\n'
        f'<rect width="3840" height="2160" fill="{background}"/>\n'
        + ET.tostring(group, encoding="unicode")
        + "\n</svg>\n"
    )
    target = root / theme / "backgrounds" / "omarchy.png"
    subprocess.run(["rsvg-convert", "-o", str(target)], input=svg.encode(), check=True)

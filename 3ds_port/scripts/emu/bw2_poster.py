"""Choose an unedited, timestamped frame of a real capture as its screenshot."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "build/bw2-python"))
import av

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("capture", type=Path)
p.add_argument("--seconds", type=float, required=True)
a = p.parse_args()
report_path = a.capture / "capture.json"
report = json.loads(report_path.read_text(encoding="utf-8"))
video = a.capture / "demo.mp4"
if hashlib.sha256(video.read_bytes()).hexdigest() != report["video"]["sha256"]:
    raise ValueError("Video changed since validation")
container = av.open(str(video))
for frame in container.decode(video=0):
    if frame.time >= a.seconds:
        image = a.capture / "screenshot.png"
        frame.to_image().save(image)
        report["screenshot_sha256"] = hashlib.sha256(image.read_bytes()).hexdigest()
        report["screenshot_source"] = {"type": "unedited decoded native video frame", "time": frame.time}
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report["screenshot_source"]))
        break
else:
    raise ValueError("Requested time is outside the captured video")
container.close()

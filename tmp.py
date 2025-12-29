import json

IN_FILE  = "C:\\Users\\marti\\Downloads\\Greenify the Earth.json"
OUT_FILE = "amazon_clean.json"

with open(IN_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

layers = data.get("layers", [])

# 1) Remove the text layer (ty==5 OR matching name)
def is_text_layer(l):
    return (l.get("ty") == 5) or ("SAVE THE AMAZON" in (l.get("nm") or ""))

data["layers"] = [l for l in layers if not is_text_layer(l)]

# 2) Set comp out-point to max layer out-point (prevents early cutoff)
max_op = max([l.get("op", data.get("op", 0)) for l in data["layers"]] + [data.get("op", 0)])
data["op"] = max_op

# Optional: remove fonts block entirely (cleaner)
if "fonts" in data:
    data["fonts"] = {"list": []}

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

print(f"Wrote: {OUT_FILE}")

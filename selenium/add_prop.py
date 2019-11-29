import json

with open("./radios.json") as f:
    radios = json.load(f)

for radio in radios:
    radio["current_status"] = False

with open("./output.json", "w") as f:
    json.dump(radios, f, indent=2)

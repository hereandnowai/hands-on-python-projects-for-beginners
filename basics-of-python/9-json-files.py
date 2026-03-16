# activity 1
import json
import os

# Construct the path to 9-example.json relative to this script
json_path = os.path.join(os.path.dirname(__file__), "9-example.json")

with open(json_path) as f:
    data = json.load(f)

print(data["brand"]["slogan"])
print(data["brand"]["organizationShortName"])

# activity 2
import json
import os

with open("basics-of-python/9-example.json") as f:
    data = json.load(f)

print(data["brand"]["slogan"])
print(data["brand"]["organizationShortName"])
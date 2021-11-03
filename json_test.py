import json

with open('listings.json', 'r') as infile:
    contents = json.load(infile)

available = [job for job in contents if job["available"]]

with open('available-listings.json', 'w') as outfile:
    json.dump(available, outfile, indent=2)

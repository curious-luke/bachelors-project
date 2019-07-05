# This code synthesizes all given JSON files to one comprehensive JSON file
import os, json
from pathlib import Path
from glob import iglob

# Import extracted tweets
print("Importing JSON Files ...")
data = []
path_to_json = 'D:/Dokumente/Uni/Bachelorarbeit/BA-Projekt/ExtractedTweets'  # Path to JSON Files
rootdir = Path(path_to_json)
json_files = list(rootdir.glob('**/*.json'))
print(len(json_files))

# Strip tweet objects to data array
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js), encoding="utf-8") as json_file:
        for line in json_file:
            if line.strip():
                data.append(json.loads(line))

# Write results to JSON file
print("Writing results to JSON ...")
with open('all_extracted_tweets_2017-12.json', 'w', encoding="utf-8") as file:
    for item in data:
        file.write("%s\n" % json.dumps(item))

# Print number of all extracted tweets
print("Number of all extracted tweets: ")
print(len(data))

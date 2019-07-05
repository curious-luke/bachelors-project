# This code filters JSON files for tweets which contain the term Bitcoin, bitcoin, btc or BTC
import os, json
from pathlib import Path
from glob import iglob

# Import raw JSON data
print("Importing data ...")

path_to_json = 'D:/Dokumente/Uni/Bachelorarbeit/Daten/Archive.org/2017/12/14' # Path to JSON Files
rootdir = Path(path_to_json)
json_files = list(rootdir.glob('**/*.json')) # List with all JSON Files

key_tweets = [] # Array for Key Tweets
st_bitcoin = ("Bitcoin", "bitcoin", "BTC", "btc") # Searchterms

# Start filter process
print("Filter process started ...")
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        for line in json_file:
            if line.strip():
                tweet_line = json.loads(line)
                line_items = tweet_line.items()

                # 1. Filter: Check for deleted tweets
                for (k, v) in line_items:    # k = key, v = value
                    if k == "source":   # key = source

                # 2. Filter: Check if tweet has more than 140 characters (truncated = true)
                        if tweet_line['truncated'] == True:
                            tweet_text = tweet_line['extended_tweet']['full_text']
                        else:
                            tweet_text = tweet_line['text']

                # 3. Filter: Check if text contains any of the searchterms (st_bitcoin)
                        if any(s in tweet_text for s in st_bitcoin):
                            key_tweets.append(tweet_line)
                        else:
                            continue
                    else:
                        continue
print("Filter process finished! ")

# Write results to JSON file
print("Writing results to JSON ...")
with open('key_tweets_2017-12-14.json', 'w', encoding="utf-8") as file:
    for item in key_tweets:
        file.write("%s\n" % json.dumps(item))

# Print number of key tweets
print("Number of Key Tweets: ")
print(len(key_tweets))

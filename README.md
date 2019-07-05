# bachelors-project
This repository contains the code pipeline that I developed in my bachelors project.
----------------------------------------------------------------------------------------

The whole code pipeline can be seen in file Pipeline.jpg.

Data source: https://archive.org/details/archiveteam-twitter-stream-2017-11

1) Analyzer.py
This script filters out all tweets from the dataset that contain the searchterms "Bitcoin", "bitcoin", "BTC" or "btc". These key tweets are written into a JSON file called key_tweets.json

2) Extracter.py
This script reduces the tweet attributes from the key_tweets.json only to the relevant ones and writes these into a JSON file called extracted_tweets.json.

3) Synthesizer.py 
To condense all extracted tweets together this script collects all extracted_tweets.json files and writes them in one JSON file called all_extracted_tweets.json.

4) ES.py
This script connects to the local elasticsearch cluster, creates the index tweets_2017-12 and indexes all the tweet objects from the all_extracted_tweets.json file. 

The final output is a dashboard visualized in Kibana. 

----------------------------------------------------------------------------------------

Elasticsearch version 6.6.0
Kibana version 6.6.0

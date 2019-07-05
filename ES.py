# This code connects to Elasticsearch, creates an Index and fills it with the tweets
from elasticsearch import Elasticsearch
import requests
import json

# Connect to the elastic cluster
es = Elasticsearch([{'host':'localhost','port':9200}])
print(es)

# Setup the settings and mapping
settings = {
    "settings": {
        "index.mapping.total_fields.limit": 80000,
        "number_of_shards": 5,
        "number_of_replicas": 1
    },
  "mappings": {
    "tweet": {
      "properties": {
        "created_at": {
          "type": "date",
          "format": "EEE MMM dd HH:mm:ss Z yyyy",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "coordinates.coordinates": {
          "type": "geo_point"
        },
        "place.bounding_box": {
          "type": "geo_shape",
          "coerce": "true",
          "ignore_malformed": "true"
        },
        "user": {
          "properties": {
            "created_at": {
                "type": "date",
                "format": "EEE MMM dd HH:mm:ss Z yyyy",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            }
          }
        }
      }
    }
  }
}

# Create a new index twitter_analysis_2017-12
es.indices.create(index='twitter_analysis_2017-12', ignore=400, body=settings)
print("Index created")

# Fill created index with all extracted tweets
tweets = []

with open("all_extracted_tweets_2017-12.json") as source:
    for line in source:
        if line.strip():
            tweets.append(json.loads(line))

for i in range(len(tweets)):
    res = es.index(index='twitter_analysis_2017-12', ignore=400, doc_type='tweet',id=i,body=tweets[i])
print("Index filled")


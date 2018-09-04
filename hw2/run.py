#!/usr/bin/env python3

import json
from pymongo import MongoClient

def consume(source='apple--2018-09-03T13-11-54.json'):
    # open connection
    client = MongoClient('localhost', 27017)
    db = client.hw2

    # load + insert
    with open(source) as f:
        data = json.load(f)

    if data:
        db.insert(data)

    # close connection
    client.close()

if __name__ == '__main__':
    consume(*argv[1:])
    
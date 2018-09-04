#!/usr/bin/env python3

import json
from sys import argv
from datetime import datetime
from pymongo import MongoClient

def consume(source='apple--2018-09-03T13-11-54.json'):
    # open connection
    client = MongoClient('localhost', 27017)
    db = client.hw2

    # load + insert
    with open(source) as f:
        data = json.load(f)

    if data:
        db.hw2col.insert(data)

    # close connection
    client.close()

def analyze(outfile='report.json'):
    # open connection
    client = MongoClient('localhost', 27017)
    db = client.hw2

    cursor = db.hw2col.find({})

    for document in cursor:
        print(document)

    # close connection
    client.close()

if __name__ == '__main__':
    if argv[1] and argv[1] == 'consume':
        consume(*argv[2:])

    elif argv[1] and argv[1] == 'analyze':
        analyze(*argv[2:])
    
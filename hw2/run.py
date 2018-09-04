#!/usr/bin/env python3

import json
from statistics import stdev
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

    cursor_full = db.hw2col.find({
        'timestamp': {
            '$regex':'^(2013-[08|09|10|11|12]|201[4-7]|2018-[01|02|03|04|05|06|07|08])',
        },
        'retweets': {
            '$gte': '0',
        },
    })

    print('=============================================')
    print('Tweets on aapl')
    print('=============================================')

    retweets_full = []
    for document in cursor_full:
        retweets_full.append(int(document['retweets']))

    print('Duration: 2013-08-xx through 2018-08-xx')
    print('Tweets >= 0')
    print('')
    print('')
    print('total retweets {:.2f}: '.format(sum(retweets_full)))
    print('mean retweets {:.2f}: '.format(sum(retweets_full) / len(retweets_full)))
    print('stdev retweets {:.2f}: '.format(stdev(retweets_full)))
    print('=============================================')
    print('')

    cursor_gt1 = db.hw2col.find({
        'timestamp': {
            '$regex':'^(2013-[08|09|10|11|12]|201[4-7]|2018-[01|02|03|04|05|06|07|08])',
        },
        'retweets': {
            '$gt': '1',
        },
    })

    retweets_gt1 = []
    for document in cursor_gt1:
        retweets_gt1.append(int(document['retweets']))

    print('Duration: 2013-08-xx through 2018-08-xx')
    print('Tweets > 1')
    print('')
    print('')
    print('total retweets {:.2f}: '.format(sum(retweets_gt1)))
    print('mean retweets {:.2f}: '.format(sum(retweets_gt1) / len(retweets_gt1)))
    print('stdev retweets {:.2f}: '.format(stdev(retweets_gt1)))
    print('=============================================')

    cursor_gt2 = db.hw2col.find({
        'timestamp': {
            '$regex':'^(2013-[08|09|10|11|12]|201[4-7]|2018-[01|02|03|04|05|06|07|08])',
        },
        'retweets': {
            '$gt': '2',
        },
    })

    # close connection
    client.close()

if __name__ == '__main__':
    if argv[1] and argv[1] == 'consume':
        consume(*argv[2:])

    elif argv[1] and argv[1] == 'analyze':
        analyze(*argv[2:])
    

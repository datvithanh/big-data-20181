import sys
import os
from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf=conf)
# lines = sc.textFile("hw1/test.txt")
lines = sc.textFile(sys.argv[1])


lines = lines.filter(lambda l: len(l.split())>1)
friend_list = lines.map(lambda l:(l.split()[0], l.split()[1].split(',')))
friend_pairs = friend_list.flatMapValues(lambda l: l)

def mutual(pair):
    pairs = []
    for x in pair[1]:
        for y in pair[1]:
            if(x != y):
                pairs.append((x,y))
    return pairs

def rec_list(pair):
    rec = str(pair[0]) + "    "
    rec_list = []
    last_val = -1
    for (_id, value) in pair[1]:
        if(value == last_val):
            rec_list.append((_id,value))
        if(len(rec_list) >= 10):
            continue
        rec_list.append((_id, value))
        if(len(rec_list) == 10):
            last_val = value
    first = False
    for (_id, value) in rec_list:
        if(first):
            rec += ","
        first = True
        rec += str(_id)
    return rec
    
mutual_pairs = friend_list.flatMap(mutual).subtract(friend_pairs)
mutual_list = mutual_pairs.map(lambda w: ((int(w[0]), int(w[1])), 1)).reduceByKey(lambda n1, n2: n1 + n2)
grouped = mutual_list.map(lambda w: (w[0][0], (w[0][1], w[1]))).sortBy(lambda w: (w[0], -w[1][1])).groupByKey().mapValues(list).sortBy(lambda w: w[0])
res = grouped.map(rec_list)
res.saveAsTextFile(sys.argv[2])
sc.stop()
# for item in res.collect():
#     print(item)
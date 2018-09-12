import re
import sys
import os
from pyspark import SparkConf, SparkContext

def gen_pair(line):
    pairs = []
    key = line.split()[0]
    if len(line.split()) > 1:
        for num in line.split()[1].split(','):
            pairs.append((key, num))
    return pairs

conf = SparkConf()
sc = SparkContext(conf=conf)
lines = sc.textFile("test.txt")

friend_pairs = lines.flatMap(lambda l: gen_pair(l))
mutual_friend_pairs = friend_pairs.reduceByKey(lambda n1,n2: n1.append(n2))
res = mutual_friend_pairs
# res.saveAsTextFile(sys.argv[2])
# pairs = []
# sc.stop()
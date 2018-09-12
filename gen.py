# lines = list(["2	0,117,135,1220,2755,12453,24539,24714,41456,45046,49927,6893,13795,16659,32828,41878", "11	0,1754,6027,7789,11142,12633,17898,19049,22486,26970,27554,27585,27591,27679,29576,32631,34906,41444"])

# def gen_pair(line):
#     pairs = []
#     key = line.split()[0]
#     for num in line.split()[1].split(','):
#         pairs.append((key, num))
#     return pairs

# line = lines[0]
# print((line.split()[0], line.split()[1].split(',')))

# import sys
# from pyspark import SparkConf, SparkContext

# conf = SparkConf()
# sc = SparkContext(conf=conf)
# lines = sc.textFile("./hw1/data.txt")

# print(lines.take(5))
import numpy as np
import sys
a = np.random.random_sample([30,30]) > 0.9
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if(a[i,j]):
            a[j,i] = True
for i in range(a.shape[0]):
    sys.stdout.write(str(i))
    sys.stdout.write(" ")
    ok = False
    for j in range(a.shape[1]):
        if(a[i,j] and i != j):
            if(ok):
                sys.stdout.write(",")            
            sys.stdout.write(str(j))
            ok = True
    sys.stdout.write("\n")
# print(np.random.random_sample([30,30]))
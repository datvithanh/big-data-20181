import sys
from data import data
from collections import deque
import numpy as np

words, link = data()
N = len(link)
words_dict = {}
visited = [0]*N
path = []

def bfs(u):
    queue = deque([u])
    visited[u] = 1
    while len(queue) > 0:
        x = queue.popleft()
        for i in link[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)

def findpath(u,v):
    path.append(words[v])
    if v == u:
        print(np.flip(path))
        return
    for i in link[v]:
        if visited[i] == visited[v]-1:
            findpath(u,i)
            path.pop()

if __name__ == "__main__":      
    if len(sys.argv) < 3:
        print("Please pass 2 words as arguments")
        exit(0)

    for (key,value) in enumerate(words):
        words_dict[value] = key
    
    if words_dict.get(sys.argv[1]) == None or words_dict.get(sys.argv[2]) == None:
        print("Words not in dict")
        exit(0)

    u,v = words_dict[sys.argv[1]], words_dict[sys.argv[2]]

    bfs(u)

    if visited[v] == 0:
        print("{} and {} are not connected".format(sys.argv[1], sys.argv[2]))

    print("shortest path:", visited[v]-1)    
    findpath(u,v)
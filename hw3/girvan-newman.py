import sys
from data import data, getBetweenness
from collections import deque
import numpy as np


words, link = data()
N = len(link)
words_dict = {}
visited = [0]*N
edge_visited = {}
path_count = [0]*N
vertex_labels = [0]*N

betweenness = []
path = []


def bfs(u):
    queue = deque([u])
    visited[u] = 1
    path_count[u] = 1
    while len(queue) > 0:
        x = queue.popleft()
        for i in link[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)
                path_count[i] = path_count[x]
            else:
                if visited[i] == visited[x] + 1:
                    path_count[i] += path_count[x]

def dfs(v):
    vertex_labels[v] = max(vertex_labels[v], 1)
    for key, i in enumerate(link[v]):
        if visited[i] == visited[v] + 1 and edge_visited.get((v,i)) == None:
            edge_visited[(v,i)] = 1
            dfs(i)
            vertex_labels[v] += vertex_labels[i]*path_count[v]/path_count[i]
            betweenness[v][key] += vertex_labels[i]*path_count[v]/path_count[i]
            
            for k, j in enumerate(link[i]):
                if j == v:
                    betweenness[i][k] += vertex_labels[i]*path_count[v]/path_count[i]
                    break

def reset():
    global visited, path_count, vertex_labels, edge_visited
    edge_visited = {}
    visited = [0]*N
    path_count = [0]*N
    vertex_labels = [0]*N

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please enter the number of biggest edges you want to show")
        exit(0)
    if not is_number(sys.argv[1]):
        print("Argument must be a integer number")

    # for i in range(N):
    #     betweenness.append(np.zeros(len(link[i])))
    # for i in range(N):
    #     print(i)
    #     if len(link[i]) > 0:
    #         reset()
    #         bfs(i)
    #         dfs(i)

    betweenness = getBetweenness()

    sorted_betweenness = []
    for i in range(N):
        for j in range(len(link[i])):
            sorted_betweenness.append([betweenness[i][j], (words[i],words[link[i][j]])])

    sorted_betweenness.sort(key=lambda x: x[0], reverse=True)

    for item in sorted_betweenness[:2*int(sys.argv[1]):2]:
        print(item[1], item[0])
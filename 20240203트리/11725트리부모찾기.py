import sys
import networkx as nx
sys.stdin = open("input.txt", "r")

arr = []
n = int(sys.stdin.readline())
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

G = nx.DiGraph()
G.add_edges_from(arr)

parents = {node: list(G.predecessors(node))[0] if G.predecessors(node) else None for node in G.nodes}

for i in range(2, n+1):
    print(parents.get(i))
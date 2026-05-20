import heapq
import math

class Graph:
    def __init__(self):
        self.adj_G = {}     # adjacency list
        self.w = {}         # weights
        
    def get_weight(self, u, v):
        return self.w[frozenset({u, v})]

    def set_weight(self, u, v, weight):
        self.w[frozenset({u, v})] = weight    

    def has_weight(self, u, v):
        return frozenset({u, v}) in self.w
        
class Vertex:
    def __init__(self, id):
        self.id = id
        self.pi = None
        self.key = math.inf

def prims_eager(G, r):
    r.key = 0
    Q = []

    for u in G.adj_G:
        # Can't compare vertices directly, so store as tuple
        # u.id used as tiebreaker, per lecture instructions
        # FOR FUTURE REF: heapq compares tuples element by element
        heapq.heappush(Q, (u.key, u.id, u))
    
    while Q:
        _, _, u = heapq.heappop(Q)
        for v in G.adj_G[u]:
            if v in [q[2] for q in Q] and G.get_weight(u, v) < v.key: # if v is in Q and weight(u, v) < v.key
                v.pi = u
                v.key = G.get_weight(u, v)
                heapq.heapify(Q) # heapq doesn't support decrease-key, so use heapify as an alternative
    return G

# Proper implementation (not also using the queue as a visited set)
def prims_eager(G, r):
    r.key = 0
    Q = []
    in_Q = set()

    for u in G.adj_G:
        heapq.heappush(Q, (u.key, u.id, u))
        in_Q.add(u)
    
    while Q:
        _, _, u = heapq.heappop(Q)
        in_Q.remove(u)
        for v in G.adj_G[u]:
            if v in in_Q and G.get_weight(u, v) < v.key:
                v.pi = u
                v.key = G.get_weight(u, v)
                heapq.heappush(Q, (v.key, v.id, v)) # Add new entry for v with updated key
    
    return G
# import numpy as NP
# from scipy import linalg as LA
# import operator
# import math, random, sys, csv
# from utils import parse, print_results

def degree(input_graph, vertex):
    degree = 0
    for j in range(len(input_graph)):
        if (input_graph[vertex][j] == 1):
            degree += 1
    return degree

def degree_centrality(input_graph):
    degree_centrality_set = {}
    size = len(input_graph)
    for i in range(size):
        degree_centrality_set[i]= degree(input_graph,i)/(size-1)
    return degree_centrality_set

def shortest_way(input_graph, vertex_begin, vertex_end):
    short_way = input_graph.copy()
    for i in range(len(input_graph)):
        for j in range(len(input_graph)):
            if short_way[i][j]==0:
                short_way[i][j]=len(input_graph)
    for k in range(len(input_graph)):
        for i in range(len(input_graph)):
            for j in range(len(input_graph)):
                short_way[i][j] = min(short_way[i][j], short_way[i][k] + short_way[k][j])
    return short_way[vertex_begin][vertex_end]

def sum_shortest_ways(input_graph, vertex):
    sum_ways=0
    size = len(input_graph)
    for i in range(size):
        sum_ways+= shortest_way(input_graph, vertex,i)
    return sum_ways

def closeness_centrality(input_graph):
    closeness_centrality_set = {}
    size = len(input_graph)
    for i in range(size):
        closeness_centrality_set[i] = 1/sum_shortest_ways(input_graph, i)
    return closeness_centrality_set

def sum_all_shortest_ways(input_graph, vertex):
    sum_ways=0
    size = len(input_graph)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                all_ways = all_ways(input_graph,j,k)
                ways_with_i = []
                for way in all_ways:
                    if str(i) in way:
                        ways_with_i.append(way)
                sum_ways+= len(all_ways)/len(ways_with_i)
    return sum_ways

def betweenneess_centrality(input_graph):
    betweenneess_centrality_set = {}
    size = len(input_graph)
    for i in range(size):
        betweenneess_centrality_set[i] = sum_all_shortest_ways(input_graph, i)
    return betweenneess_centrality_set

def eigenvector_centrality(input_graph):
    e_vals, e_vecs = LA.eig(input_graph)
    return e_vals,e_vecs

class PageRank:
    def __init__(self, graph, directed):
        self.graph = graph
        self.V = len(self.graph)
        self.d = 0.85
        self.directed = directed
        self.ranks = dict()
    def pagerank_centrality(self):
        for key, node in self.graph.nodes(data=True):
            if self.directed:
                self.ranks[key] = 1 / float(self.V)
            else:
                self.ranks[key] = node.get('rank')
        for _ in range(10):
            for key, node in self.graph.nodes(data=True):
                rank_sum = 0
                curr_rank = node.get('rank')
                if self.directed:
                    neighbors = self.graph.out_edges(key)
                    for n in neighbors:
                        outlinks = len(self.graph.out_edges(n[1]))
                        if outlinks > 0:
                            rank_sum += (1 / float(outlinks)) * self.ranks[n[1]]
                else:
                    neighbors = self.graph[key]
                    for n in neighbors:
                        if self.ranks[n] is not None:
                            outlinks = len(self.graph.neighbors(n))
                            rank_sum += (1 / float(outlinks)) * self.ranks[n]
                self.ranks[key] = ((1 - float(self.d)) * (1 / float(self.V))) + self.d * rank_sum
        return 0
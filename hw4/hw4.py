# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx

file1 = "CA-GrQc.txt";
file2 = "p2p-Gnutella04.txt";
file3 = "Wiki-Vote.txt";

G1 = nx.read_edgelist(file1);
G2 = nx.read_edgelist(file2);
G3 = nx.read_edgelist(file3);
G4 = nx.erdos_renyi_graph(5000,0.01);

print file1+' %.8f' % (nx.average_clustering(G1));
print file2+' %.8f' % (nx.average_clustering(G2));
print file3+' %.8f' % (nx.average_clustering(G3));
print "random_graph "+'%.8f' % (nx.average_clustering(G4));


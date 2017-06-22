# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx

G = nx.petersen_graph();
nx.draw(G)
plt.savefig("petersen.png")

plt.figure()
G = nx.tutte_graph();
nx.draw(G)
plt.savefig("tutte.png")

plt.figure()
G = nx.sedgewick_maze_graph();
nx.draw(G)
plt.savefig("sedgewick_maze.png")

plt.figure()
G = nx.tetrahedral_graph();
nx.draw(G)
plt.savefig("tetrahedral.png")

plt.figure()
G = nx.complete_graph(10);
nx.draw(G)
plt.savefig("complete10.png")

plt.figure()
G = nx.complete_bipartite_graph(3,100);
nx.draw(G)
plt.savefig("compbipartite.png")

plt.figure()
G = nx.barbell_graph(10,10);
nx.draw(G)
plt.savefig("barbell.png")

plt.figure()
G = nx.lollipop_graph(10,20);
nx.draw(G)
plt.savefig("lollipop.png")

plt.figure()
G = nx.karate_club_graph();
nx.draw(G)
plt.savefig("karate_club.png")

plt.figure()
G = nx.erdos_renyi_graph(500,0.01);
nx.draw(G)
plt.savefig("erdos_renyi.png")
#plt.show()

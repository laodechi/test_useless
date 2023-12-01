import networkx as nx
import community as community_louvain

# import the graph
G = nx.Graph()


# using Louvain alogrithms
partition = community_louvain.best_partition(G)

# communities list 
communities = []
for com in set(partition.values()):
    list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
    communities.append(list_nodes)

# computing the modularity
modularity = community_louvain.modularity(partition, G)
print(f"Modularity: {modularity}")

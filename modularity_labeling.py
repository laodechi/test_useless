import networkx as nx
from networkx.algorithms import community


G = nx.Graph()


communities = list(community.label_propagation_communities(G))


partition = {node: i for i, com in enumerate(communities) for node in com}
modularity = community.modularity(G, communities)
print(f"Modularity: {modularity}")

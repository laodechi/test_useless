import networkx as nx
import community as community_louvain
from sklearn.metrics import normalized_mutual_info_score

# input G
G = nx.Graph()


partition = community_louvain.best_partition(G)

# NMI transform
algorithm_labels = list(partition.values())

# comparison data input
true_labels = [ ... ] 

# 计算NMI
nmi = normalized_mutual_info_score(true_labels, algorithm_labels)
print(f"Normalized Mutual Information (NMI): {nmi}")

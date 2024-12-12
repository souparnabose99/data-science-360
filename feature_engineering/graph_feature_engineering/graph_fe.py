import pandas as pd
import networkx as nx

# Create a dummy social media graph network

# Create a dummy accounts dataframe with 10 nodes
accounts = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "username": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
})

# Create a dummy followers dataframe
followers = pd.DataFrame({
    "follower_id": [2, 3, 4, 5, 1, 3, 4, 7, 1, 3, 8, 9],
    "following_id": [1, 1, 1, 3, 2, 1, 4, 2, 1, 1, 1, 2]
})

# Directed Graph initiation
dir_graph = nx.DiGraph()

# Adding nodes to the graph using dummy accounts DataFrame
for _, row in accounts.iterrows():
    dir_graph.add_node(row["user_id"], username=row["username"])

# Adding edges to the graph using dummy followers DataFrame
for _, row in followers.iterrows():
    dir_graph.add_edge(row["follower_id"], username=row["following_id"])

# Compute total degree for each node
accounts["total_degree"] = accounts["user_id"].apply(lambda x: dir_graph.degree(x))

# Compute in degree for each node
# G.in_degree(x) -> counts edges directed toward the node x
accounts["in_degree"] = accounts["in_degree"].apply(lambda x: dir_graph.in_degree(x))

# Compute out degree for each node
accounts["out_degree"] = accounts["out_degree"].apply(lambda x: dir_graph.out_degree(x))


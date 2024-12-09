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



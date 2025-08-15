import networkx as nx
import matplotlib.pyplot as plt

def create_campus_graph():
    G = nx.Graph()  # UNDIRECTED GRAPH
    
    locations = [
        "Admission Office", "AB-4", "Food Court", "Gym", "Medical Center",
        "Engineering Building", "Green Garden", "Central Mosque", "AB-1",
        "Innovation Lab", "Rowsanara Hall", "YKSG-2", "Transport", "YKSG-1"
    ]
    G.add_nodes_from(locations)
    
    edges = [
        ("Admission Office", "AB-4", 3),
        ("AB-4", "Food Court", 13),
        ("Food Court", "Gym", 5),
        ("Gym", "Medical Center", 8),
        ("Medical Center", "YKSG-2", 10),
        ("YKSG-2", "Engineering Building", 7),
        ("Admission Office", "Green Garden", 9),
        ("Green Garden", "Central Mosque", 6),
        ("Central Mosque", "AB-1", 2),
        ("AB-1", "Innovation Lab", 1),
        ("Innovation Lab", "Rowsanara Hall", 12),
        ("Rowsanara Hall", "YKSG-2", 15),
        ("AB-1", "Transport", 4),
        ("Transport", "YKSG-1", 2)
    ]
    G.add_weighted_edges_from(edges)
    
    return G

# Create graph
campus_graph = create_campus_graph()

# Custom positions for better spacing
pos = {
    "Admission Office": (-2, 2),
    "AB-4": (-1, 2.8),           # Moved further from Rowsanara Hall
    "Food Court": (0, 2.2),
    "Gym": (1, 2.0),
    "Medical Center": (2, 1.8),
    "YKSG-2": (3, 1.5),
    "Engineering Building": (4, 1.2),
    "Green Garden": (-1.5, 1),
    "Central Mosque": (-0.5, 0.8),
    "AB-1": (0.8, 0.5),          # Moved further from Transport
    "Innovation Lab": (1.8, 0.3),
    "Rowsanara Hall": (2.8, 0.0),# Moved further from AB-4
    "Transport": (-0.5, -0.5),
    "YKSG-1": (-1, -1)
}

plt.figure(figsize=(12, 9))
plt.axis("off")

# Draw nodes
nx.draw_networkx_nodes(
    campus_graph, pos,
    node_size=3000,
    node_color=range(len(campus_graph.nodes())),
    cmap=plt.cm.plasma,
    alpha=0.9
)

# Draw undirected edges
nx.draw_networkx_edges(
    campus_graph, pos,
    edge_color='black', width=2
)

# Draw labels
nx.draw_networkx_labels(
    campus_graph, pos,
    font_size=10, font_weight="bold",
    font_color="white",
    bbox=dict(facecolor="black", alpha=0.5, edgecolor="none", boxstyle="round,pad=0.3")
)

# Draw edge weights
edge_labels = nx.get_edge_attributes(campus_graph, 'weight')
nx.draw_networkx_edge_labels(
    campus_graph, pos, edge_labels=edge_labels,
    font_size=9, font_color="red", rotate=False
)

plt.title("Campus undirected Graph", fontsize=16, fontweight="bold")
plt.show()

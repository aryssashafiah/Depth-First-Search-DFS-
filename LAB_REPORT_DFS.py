import streamlit as st

# Directed graph from your lab image
graph = {
    'A': ['D', 'B'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F']
}

# DFS with depth (level) tracking using recursion
def dfs_with_discovery_levels(start='A'):
    visited = set()
    discovery = []  # List of (level, node)

    def dfs_recursive(node, level):
        if node not in visited:
            visited.add(node)
            discovery.append((level, node))
            # Visit neighbors in alphabetical order (tie-breaking)
            for neighbor in sorted(graph[node]):
                dfs_recursive(neighbor, level + 1)

    dfs_recursive(start, 0)
    return [node for _, node in discovery], discovery

# =============== STREAMLIT UI ===============
st.set_page_config(page_title="AI Lab 1 – DFS", layout="centered")

# 🖼️ Show your graph image at the very top
st.image("LabReport_BSD2513_1.jpg", caption="Directed Graph from Lab Report", use_column_width=True)

st.title("🔍 Depth-First Search (DFS)")

if st.button("▶️ Generate DFS Output"):
    traversal, discovery = dfs_with_discovery_levels('A')

    # Traversal Order
    st.subheader("Traversal Order:")
    st.markdown(f"**DFS Traversal Order**: {' → '.join(traversal)}")

    # Node Discovery Level (exact format from your image)
    st.subheader("Node Discovery Level:")
    for lvl, node in discovery:
        st.markdown(f"""
        <div style="
            background-color: #f0f8e8;
            padding: 10px;
            margin: 5px 0;
            border-radius: 8px;
            font-family: monospace;
            font-size: 16px;
            color: #006400;
        ">
            Level {lvl} → {node}
        </div>
        """, unsafe_allow_html=True)


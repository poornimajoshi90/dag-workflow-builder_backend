from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Node(BaseModel):
    id: str
    type: str | None = None
    data: Dict[str, Any] | None = None
    position: Dict[str, Any] | None = None

class Edge(BaseModel):
    source: str
    target: str

class Graph(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.post("/pipelines/parse")
def parse_pipeline(graph: Graph):

    nodes = graph.nodes
    edges = graph.edges

    node_count = len(nodes)
    edge_count = len(edges)

    # Build adjacency list
    adj = {node.id: [] for node in nodes}
    indegree = {node.id: 0 for node in nodes}

    for edge in edges:
        adj[edge.source].append(edge.target)
        indegree[edge.target] += 1

    # Topological Sort (Kahn's Algorithm)
    queue = [n for n in indegree if indegree[n] == 0]
    visited = 0

    while queue:
        current = queue.pop(0)
        visited += 1
        for neighbor in adj[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return {
        "nodeCount": node_count,
        "edgeCount": edge_count,
        "isDAG": visited == node_count
    }
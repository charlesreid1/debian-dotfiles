#!/usr/bin/python3
from graph import Graph
from copy import deepcopy

"""
Graph Algorithms

Implementation of various graph algorithms
for application to the wiki link graph.
"""


def floyd_warshall(g):
    """Return new graph - transitive closure of g
    """
    closure = deepcopy(g)
    vertices = list(closure.vertices())
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # does edge (i,k) exist in partial closure?
            if i!=k and closure.get_edge(verts[i],verts[k]) is not None:
                for j in range(n):
                    # verify that edge (k,j) exists in partial closure
                    if i!=j!=k and closure.get_edge(verts[k],verts[j]) is not None:
                        # if (i,j) not yet ncluded, add it to the closure
                        if closure.get_edge(verts[i],verts[j]) is None:
                            closure.insert_edge(verts[i],verts[j])

    return closure


def scc(g):
    """
    Find and return a collection of strongly-connected 
    components.
    
    https://www.geeksforgeeks.org/strongly-connected-components/
    """
    stack = []

    n = g.vertex_count()

    # Initially all vertices are unvisited
    visited = [False]*n

    # Populate the stack with vertices
    # ordered according to finishing time
    vertices = sorted(list(g.vertices()))
    for iv, v in enumerate(vertices):
        if visited[iv] is False:
            scc_fill(g,iv,v,visited,stack)

    # Instead of creating a second reversed graph,
    # we use a reverse DFS method. 

    # Mark all vertices as unvisited
    visited = [False]*n

    # Now process all vertices 
    # in order added to stack
    # (i.e., in order of finish time)
    components = []
    while stack:
        component = []
        iv = stack.pop()
        if visited[iv] is False:
            v = vertices[iv]
            # DFS will accumulate visited nodes in component
            scc_dfs(g, iv, v, visited, component, reverse=True)

            # When we reach this point, DFS is done.
            components.append(component)

    return components


def scc_dfs(g, iv, v, visited, partition, reverse=False):
    """Visit each vertex via DFS
    """
    # Mark the current node as visited
    visited[iv] = True

    # Current node also goes in the parition
    partition.append(v.element())

    # Recur for all vertices adjacent to this vertex
    #
    if reverse:
        # Reverse DFS:
        edges = list(g.incident_edges(v,outgoing=False))
    else:
        # Forward DFS:
        edges = list(g.incident_edges(v,outgoing=True))

    for iw,e in enumerate(edges):
        w = e.opposite(v)
        if visited[iw] is False:
            scc_dfs(g, iw, w, visited, partition)



def scc_fill(g, iv, v, visited, stack):
    """ Add each vertex to the stack 
    in order of when each finished
    """
    # Mark the current node as visited
    visited[iv] = True

    # Recur for all vertices adjacent to this vertex
    for iw,e in enumerate(g.incident_edges(v,outgoing=True)):
        w = e.opposite(v)
        if visited[iw] is False:
            scc_fill(g,iw,w,visited,stack)

    stack.append(iv)


def dfs_complete(g):
    """Perform a DFS for the entire graph. 

    discovered maps each vertex v to the edge
    used to discover it. Root vertices are 
    mapped to None.
    """
    discovered = {}
    for u in g.vertices():
        if u.element() not in diiscovered:
            # u is the root of the tree
            discovered[u.element()] = None
            print("Adding %s as root of tree"%(u.element()))
            dfs(g,u,discovered)

    return discovered


def dfs(g,u,discovered):
    """Perform DFS of the Graph g 
    starting at Vertex u.

    discovered is a dictionary that maps
    each vertex to the edge that was used
    to discover it during the DFS.
    """
    for e in g.incident_edges(u,outgoing=True):
        v = e.opposite(u)
        if v.element() not in discovered:
            discovered[v.element()] = e.element()
            dfs(g,v,discovered)


def construct_path(u,v,discovered):
    """Use the discovered dictionary from 
    depth-first search to reconstruct 
    a path from node u to node v.
    """
    path = []
    # Deal with empty case
    if v not in discovered:
        return path
    
    # build list of edges 
    # that connect v to u,
    # then reverse it.
    path.append(v)
    walk = v
    while walk is not u:
        e = discovered[walk]
        parent = e.opposite(walk)
        path.append(parent)
        walk = parent
    path.reverse()
    return path



def get_transpose_graph(g):
    """Creates a copy of g, transposes it, 
    and returns the result.
    """
    g2 = Graph(directed=g.is_directed())
    
    # Add all vertices
    for v in g.vertices():
        g2.insert_vertex(v.element())
    
    # Find all outgoing edges from a node on g,
    # and add them as incoming edges on g2.
    for u in g2.vertices():
        for e in g2.incident_edges(u,outgoing=True):
            v = e.opposite(u)
            g2.insert_edge(v,u)
    
    return g2 

if __name__=="__main__":
    print("Don't call this script directly: call push_wiki.py instead")


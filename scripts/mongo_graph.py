from graph import Graph

class MongoGraph(Graph):
    """
    Class combining the underlying 
    graph data structure with a 
    serialization layer for turning
    the graph into something that can 
    be stored in a database table.
    """
    def export_graph(self,collection):
        """Export the data to the MongoDB collection.
        Do we store vertices, or edges?
        """
        # Remove existing graph
        collection.drop()

        print("\nExporting graph...")
        for edge in self.edges():
            u,v = edge.endpoints()
            e = edge.element()
            d = {
                    "u":   str(u),
                    "v":   str(v),
                    "_id": str(edge)
                }
            collection.insert_one(d)
        print("Done.\n")

    def import_graph(self,collection):
        """Import the data from the MongoDB collection
        and use it to reconstruct the graph.
        """
        if(self.vertex_count() > 0):
            raise Exception("Error: this graph is not empty!")

        print("\nImporting graph...")
        for document in collection.find():
            ulabel = document['u']
            vlabel = document['v']
            u = self.insert_vertex(ulabel)
            v = self.insert_vertex(vlabel)
            try:
                self.insert_edge(u,v)
            except ValueError:
                pass
        print("Done.\n")




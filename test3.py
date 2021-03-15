from os import name
import networkx as nx

# Person class with init, repr, and str.
class Person:
    def __init__(self, name, couple):
        self.name = name
        self.couple = couple
        self.busy = False
        self.hosting = []
    def __repr__(self):
        return repr(self.name)
    def __str__(self):
        return self.name
    
# Defining variables.
G = nx.DiGraph()
group_max = 3;
week = 1

# Reading the input file.
with open("group1.txt") as file:
    lines = file.read().splitlines()
    for L in lines:
        L = L.replace(", ", "+")
        if "+" in L:
            P = Person(L, True)
        else:
            P = Person(L, False)
        G.add_node(P)

# Build every edge of the complete graph.
for s in G.nodes():
    for v in G.nodes():
        if s != v:
            G.add_edge(s, v)
                
# Iterate each week until there are no more connecting edges.
while G.number_of_edges() > 0:
    print("Week", week)

    # Finding required connections.
    for s in G.nodes():
        if s.hosting:
            continue
        for v in G.adj[s]:
            if not v.busy and len(v.hosting) < group_max:
                s.busy = True
                if (v not in v.hosting):
                    v.hosting.append(v)
                v.hosting.append(s)
                G.remove_edge(s, v)
                break

    # TODO: Assign repeat visitors.
    
    # Showing the hosts for this week.
    # TODO: Improve the text formatting.
    # TODO: Show the graphical visualization.
    for s in G.nodes():
        if (s.hosting):
            print(s.hosting[0], s.hosting[1:])
        s.busy = False
        s.hosting = []

    # Increment the week counter.
    week += 1
    print("\n")

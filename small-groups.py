from os import name
import networkx as nx

# Person class with init, repr, and str.
class Person:
    def __init__(self, name, couple):
        self.name = name
        self.couple = couple
        self.busy = False
        self.hosting = []
        self.host_count = 0
    def __repr__(self):
        return repr(self.name)
    def __str__(self):
        return self.name

    def hosts(self, visitor):
        # Make this household a host if it isn't already.
        if (self.host_count == 0):
            self.hosting.append(self)
            self.host_count += 1
            if self.couple:
                self.host_count += 1
                
        # Host the current household s.
        visitor.busy = True
        self.hosting.append(visitor)
        self.host_count += 1
        if visitor.couple:
            self.host_count += 1

    def reset(self):
        self.busy = False
        self.hosting = []
        self.host_count = 0
    
# Defining variables.
group_size = 3;
filename = "group2.txt"

G = nx.DiGraph()
week = 1
repeat_visits = []

# Reading the input file.
# TODO Get user input for filename and group_size. ------------------------------------------------------
with open(filename) as file:
    lines = file.read().splitlines()
    for L in lines:
        L = L.replace(", ", " + ")
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
            if not v.busy and v.host_count < group_size:
                v.hosts(s)
                G.remove_edge(s, v)
                break

    # Assigning repeated visitors (not required connections).
    for s in G.nodes():
        if not s.busy and not s.hosting:
            for v in G.nodes():
                if s != v and not v.busy and v.host_count < group_size:
                    v.hosts(s)
                    repeat_visits.append(s)
                    break
    
    # Showing the hosts for this week.
    # TODO: Improve the text formatting. (Optional) ------------------------------------------------------
    # TODO: Show the graphical visualization. (Extra Credit)----------------------------------------------
    for s in G.nodes():
        if (s.hosting):
            print(s.hosting[0], s.hosting[1:])
        s.reset()
    # Show repeat visitors (to verify that the algorithm is effecient).
    if (repeat_visits):
        print("Repeats:", repeat_visits)

    # Increment the week counter.
    week += 1
    repeat_visits = []
    print("\n")

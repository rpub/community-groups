from os import name, system
import networkx as nx
import numpy as np

# Requirements.
# Python 3.9.2
# newtorkx-2.5 [pip install networkx]
# numpy-1.20.1 [pip install numpy]

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
G = nx.DiGraph()
week = 1
repeat_visits = []

file_name = input("Please enter your plaintext file with smallgroup names: ")
open(file_name, "r")

# Reading the input file.
with open(file_name) as file:
    lines = file.read().splitlines()
    for L in lines:
        L = L.replace(", ", " + ")
        if "+" in L:
            P = Person(L, True)
        else:
            P = Person(L, False)
        G.add_node(P)

group_size = int(input("What is the group size? (no more than half # of people)"))
print("\n\n")

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
    for s in G.nodes():
        if (s.hosting):
            print(s.hosting[0], s.hosting[1:])
        s.reset()
    # Show repeat visitors (to verify that the algorithm is efficient).
    if (repeat_visits):
        print("Repeats:", repeat_visits)
    
    # Increment the week counter.
    week += 1
    repeat_visits = []
    print("\n")

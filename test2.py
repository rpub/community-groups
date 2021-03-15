from os import name
from igraph import *

# Person class with init, repr, and str.
class Person:

    # This modification only keeps track of the name of the person/couple as one string,
    # and whether or not they are a couple. This avoids extra checks and we can still print the same.
    def __init__(self, name, couple):
        self.name = name
        self.couple = couple

    def __repr__(self):
        return repr(self.name, self.couple)

    def __str__(self):
        return self.name

# Defining variables.
people = []

# Reading the file and building a list of people.
with open("group1.txt") as file:
    for line in file:
        if ',' in line:
            household = Person(line, True)
        else:
            household = Person(line, False)
        people.append(household)

# Build the initial graph based on the people list.
g = Graph(directed=True)
g.add_vertices(len(people))
for i in range(len(people)):
    s = g.vs[i]
    s["household"] = people[i]
    s["label"] = people[i].name

# Defining default attributes of every node.
for s in g.vs:
    s["busy"] = False
    s["host"] = False

# Build every edge of the complete graph.
for s in g.vs:
    for v in g.vs:
        if s != v: 
            g.add_edges([(v, s)])

# For every edge of each node s.       
for s in g.vs:
    # print(s)
    if s["host"] == False:
        for v in g.neighbors(v, mode=ALL)
            print(v)
            # if v["busy"] == False:
            #     s["busy"] = True
            #     v["host"] = True

# Quitting early to focus on the top part.
quit()


# g.vs["label"] = g.vs["name"]

i = 0
m = 0
group_size = 4



for s in g.vs:
    for e in g.es:
        g.es.select(_source=s)

# print(g)

# 			If N is NOT busy AND N is hosting fewer than MAX:
# 				If N is not hosting N:
# 					N hosts N.
# 				N hosts S.
# 				S is busy.
# 				Remove E.



# for v in g.vs:
#     g.add_edges([(v, i)])
    
#         while v.degree() < group_size+1:
            
#             free = [y for y in g.vs[:0] if y.degree() == 0]

#             for y in free:
#                     g.add_edges([(v, y)])       
            
#         # free = [v.index for v in  g.vs if v.degree() == 0] 
#         # while m < group_size + 1:
#         #     for i in free:
#         #         g.add_edges([(v, i)])
#         #         m += 1

# plot(g)


# for v in g.vs:
#     if v.degree() == 0:
    
#         while v.degree() < group_size+1:
            
#             free = [y for y in g.vs[:0] if y.degree() == 0]

#             for y in free:
#                     g.add_edges([(v, y)])       
            
#         # free = [v.index for v in  g.vs if v.degree() == 0] 
#         # while m < group_size + 1:
#         #     for i in free:
#         #         g.add_edges([(v, i)])
#         #         m += 1

# plot(g)


# for v in g.vs:
#     if v.degree() == 0:      
#         next = v.degree() + 1        
#         while next < 4:
#             if v.degree() + next == 0:
#                 g.add_edges([(v, next)])
#                 next += 1

#         g.add_edges([(v, v.index + 1)])

#     print(v)
#     print(g)
# plot(g)



# 	//Find new group connections.
# 	For every node S in G:
# 		For every node N connected to S through edge E:
# 			If N is NOT busy AND N is hosting fewer than MAX:
# 				If N is not hosting N:
# 					N hosts N.
# 				N hosts S.
# 				S is busy.
# 				Remove E.

# Until G is a completely disconnected graph:

# 	//Find unassigned duplicate connections.
# 	For every node S in G:
# 		If S is not busy AND S is not hosting S:
# 			For every node N in G:
# 				If N is NOT busy:
# 					N hosts S.

# 	//Output groups for this week.
# 	Output current week.
# 	Increment week.
# 	For every node S in G:
# 		If S is hosting S:
# 			Output S guest list.

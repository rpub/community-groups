from os import name
from igraph import *

# g = Graph(vertex_attrs={"label": vertices}, edges=edges, directed=False)

class Person:   
    def __init__(self, *inp):
        if len(inp) == 1:
            self.name = inp
            is_couple = 'Single';

        elif len(inp) == 2:
            self.name1 = inp[0]
            self.name2 = inp[1]
            is_couple = 'Married';

        def __repr__(self):
            if self.name1 & self.name2:
                return repr((self.name1, self.name2))
            elif self.name1:
                return repr((self.name1))

        def __str__(self):
            if self.name1 & self.name2:
                return "Married: {John}, {Marie}".format(self.name1, self.name2)
            elif self.name1:
                return "Single: {John}".format(self.name1)

        # ^^^^^^^ code above and below under open doesn't work - but very close to working

people = []

with open("group1.txt") as file:
    for line in file:
        if ',' in line:
            p1, p2, = line.split(',')
            print(p1, p2)
            person = Person(p1, p2)
        else:
            p1 = line
            print(p1)
            person = Person(p1)
        
        people.append(person)

print(people)

# ------------------ This part below works

vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

g = Graph(directed=True)
g.add_vertices(vertices)
g.vs["is_host"] = [False, False, False, False, False, False, False, False, False, False, False, False]
g.vs["is_couple"] = [False, False, False, False, False, False, False, False, False, False, False, False]
g.vs["is_busy"] = [False, False, False, False, False, False, False, False, False, False, False, False]
g.vs["label"] = g.vs["name"]

i = 0
m = 0
group_size = 4

for s in g.vs:
    for v in g.vs:
        if s != v: 
            g.add_edges([(v, s)])
plot(g)

for s in g.vs:
    for e in g.es:
        g.es.select(_source=s)

print(g)

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
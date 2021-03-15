# groups.py - source code

# enter file name
file_name = raw_input("Enter filename: ")
if len(file_name) == 0:
  print ("Next time please enter something")
  exit()
try:
  file = open(file_name, "r")
except IOError:
  print ("There was an error reading file")
  exit()

# enter group size
group_size = raw_input("What is the group size? Group size should be no more than half the size of all people: ")
print(group_size)

# output to smallgroup.txt
print("See smallgroup.txt for your small group assignments")

# Let G be a directed and fully connected graph.
# Let MAX be the size of groups.
# Until G is a completely disconnected graph:

# 	//Find new group connections.
# 	For every node S in G:
# 		Let V be a list of edges of S.
# 		For every node N connected to S through edge E:
# 			If N is NOT busy AND N is hosting fewer than MAX:
# 				If N is not hosting N:
# 					N hosts N.
# 				N hosts S.
# 				S is busy.
# 				Remove E.

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
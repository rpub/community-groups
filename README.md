# Creating Community Small Groups
A work by: Jonathan Hacker and Rami Isaac

*Write an introduction to your work*

## Description
*Describe what your project is about and what language you used*

## Requirements
*The requirements of the program, i.e. Python 3.1, what libraries are needed*

## User Manual
*Once a person clones this into their computer how the person is supposed to run the program, add screenshots showing how your program works, also add here the link to the Youtube video showing the program running*

## Reflection
<<<<<<< HEAD
*Write the reflection about getting the small groups in the minimum number of iterations, etc.*
=======
A brute force approach to this problem would require finding every possible group, and checking for the minimum set. This is obviously very unmanageable, therefore we will use a greedy algorithm that will find an efficient set of groups in a much shorter time.

THE ALGORITHM
1. We will start with a graph such that each household (one person or a couple) is represented with a node. They will begin with no edges, which indicates that no household has visited any other household.
2. For each week, each node will go in order and search for another node which it is able to visit. A household that is not already hosting someone can visit another household if the second household is not already visiting someone else AND they are not already hosting too many people.
3. When they visit, an edge will be added between them to indicate as such. Thus the algorithm is finished when the graph is complete (every household has visited every other household).

There are two additional complications:
1. Couples must increment a hosting count by two instead of one.
2. Repeat visitors (who have no valid household to visit, and are not hosting themselves) must be retroactively assigned to groups. They are not part of the optimal solution, but they still need groups to fulfill the need of the group lists.

TIME COMPLEXITY ANALYSIS
The time complexity of this algorithm is O(N^2) for each week it runs, for it must compare each node to every other node to determine if it is able to visit.

Our actual implementation is slightly different. We optimized it somewhat by doing the inverse of the above algorithm. Instead of adding connections as visits are made, we started with a complete graph and removed connections as visits occur. Thus each node only needs to check nodes that are within its own adjacency list. This still has an upper bound of O(N^2) but some weeks may take only O(N) in the case where each node finds a host immediately. But unfortunately, the repeat visitors phase still takes O(N^2) so while our final solution is more efficient on average, the time complexity is the same.

CHALLENGES FACED
One main challenge we encountered was the difficulty of learning both a new language (Python) and a new library at the same time. We were initially using a library called igraph, but ran into a lot of issues with obscure syntax and confusing documentation. Midway through the assignment we actually switched libraries entirely to NetworkX instead and had a much easier time with that. By spending more time researching, we eventually were able to implement a solution.

Furthermore, there is a challenge in collaborating with a team member. We were able to benefit from working in a team, however, by ensuring regular communication, and dividing work so that each of us was doing the part we felt most comfortable doing.
>>>>>>> e092ce9280962cffbd15a6d343f07a7bc2dd5ab0

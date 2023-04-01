**Escape Pods**<br>
\===========

You've blown up the LAMBCHOP doomsday device and relieved the bunnies of their work duries -- 
and now you need to escape from the space station as quickly and as orderly as possible! The bunnies 
have all gathered in various locations throughout the station, and need to make their way towards the 
seemingly endless amount of escape pods positioned in other parts of the station. You need to get the 
numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between 
the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to 
accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time. 

Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and 
how many bunnies can fit through at a time in each direction of every corridor in between, figure out 
how many bunnies can safely make it to the escape pods at a time at peak.

Write a function solution(entrances, exits, path) that takes an array of integers denoting where the 
groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an 
array of an array of integers of the corridors, returning the total number of bunnies that can get through 
at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path 
element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time 
step. There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit 
at a time.

For example, if you have:<br>
entrances = [0, 1]<br>
exits = [4, 5]<br>
path = [<br>
 [0, 0, 4, 6, 0, 0], # Room 0: Bunnies<br>
 [0, 0, 5, 2, 0, 0], # Room 1: Bunnies<br>
 [0, 0, 0, 0, 4, 4], # Room 2: Intermediate room<br>
 [0, 0, 0, 0, 6, 6], # Room 3: Intermediate room<br>
 [0, 0, 0, 0, 0, 0], # Room 4: Escape pods<br>
 [0, 0, 0, 0, 0, 0], # Room 5: Escape pods<br>
]<br>

Then in each time step, the following might happen:<br>
0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3<br>
1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3<br>
2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5<br>
3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5<br>

So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step. (Note that in this 
example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the 
final solution remains the same.)

**Languages**<br> 
\=========

To provide a Java solution, edit Solution.java<br>
To provide a Python solution, edit solution.py

**Test cases**<br> 
\==========<br>
Your code should pass the following test cases.<br>
Note that it may also be run against hidden test cases not shown here.

**- - Java cases - -**<br> 
Input:<br>
Solution.solution({0, 1}, {4, 5}, {{0, 0, 4, 6, 0, 0}, {0, 0, 5, 2, 0, 0}, {0, 0, 0, 0, 4, 4}, {0, 0, 0, 0, 6, 6}, 
{0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16 

Input:<br> 
Solution.solution({0}, {3}, {{0, 7, 0, 0}, {0, 0, 6, 0}, {0, 0, 0, 8}, {9, 0, 0, 0}})<br> 
Output:<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6

**- - Python cases - -**<br>
Input:<br>
solution.solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6

Input:<br>
solution.solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0,
0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])<br> 
Output:<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use
submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your 
home folder.

**Constraints**<br>

**Java**<br>
\====<br>
Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method
inside the Solution class

Execution time is limited.

Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive
an error when you verify your solution if you have used a blacklisted class.

Third-party libraries, input/output operations, spawning threads or processes and changes to the 
execution environment are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing 
characters. 

**Python**<br> 
\======<br>
Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() 
function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, 
termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing 
characters.
**Solar Doomsday**<br>
\==============

Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor core with solar arrays, and you've been tasked with setting up the solar panels.

Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into three 1x1 square solar panels.

Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, solution(12) would return [9, 1, 1, 1].

**Languages**<br> 
\=========

To provide a Python solution, edit solution.py<br>
To provide a Java solution, edit Solution.java

**Test cases**<br> 
\==========<br>
Your code should pass the following test cases.<br>
Note that it may also be run against hidden test cases not shown here.

**- - Python cases - -**<br>
Input:<br>
solution.solution(15324)<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15129,169,25,1 

Input:<br>
solution.solution(12)<br> 
Output:<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9,1,1,1

**- - Java cases - -**<br> 
Input:<br>
Solution.solution(12)<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9,1,1,1 

Input:<br> 
Solution.solution(15324)<br> 
Output:<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15129,169,25,1

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

**Constraints**<br>

**Java**<br>
\====<br>
Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

Execution time is limited. 

Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class. 

Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed. 

Your solution must be under 32000 characters in length including new lines and and other non-printing characters. 

**Python**<br> 
\======<br>
Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function. 

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib. 

Input/output operations are not allowed. 

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.
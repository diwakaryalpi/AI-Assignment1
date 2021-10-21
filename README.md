# AI-Assignment 1

I have used python3 programming to work on this assignment.

O - Obstacle  
S - Storage  
B - Block  
R - Robot

I have considered below two extra formats while solving the Sokoban puzzle:

"*****" - Block on strage space  
"**.**" - Robot on storage space

### How to compile and execute

I have implemented all the algorithms in 6 different files and named as below:
1. Breadth First Search - bfs.py
2. Depth First Search - dfs.py
3. greedy_manhattan.py
4. greedyOwnHeuristic.py
5. Astar_manhattan.py
6. Astar-ownHeuristic.py

**Two new lines** should be provided after the input puzzle so that the program understands that complete input is considered.

	I have saved the Sokoban puzzle in the text file : puzzle.txt. 
    python3 "python_filename" < "puzzle_input"
    
    python3 bfs.py < puzzle.txt
    python3 dfs.py < puzzle.txt
    python3 greedy_manhattan.py < puzzle.txt
    python3 greedyOwnHeuristic.py < puzzle.txt
    python3 Astar_manhattan.py < puzzle.txt
    python3 Astar-OwnHeuristic.py < puzzle.txt

**Note: input file has to contain 2 new lines after providing puzzle, please check the puzzle.txt to understand the format. It has 2 new lines after the puzzle**

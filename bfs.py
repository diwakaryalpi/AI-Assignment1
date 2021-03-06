import collections
import copy
import time

board=[]
maxLength=0

boxRobot=[]
wallsStorageSpaces=[]
Moves = {'N':[-1,0], 'E':[0,1],'S':[1,0],'W':[0,-1]}

maxRowLength = 0	
lines=0

while(1):
	line =input()
	if line!="":
		lines+=1
		board.append(line)
		if len(line)>maxRowLength:
			maxRowLength=len(line)
	else:
		break	

time_start = time.time()
for i in range(0,lines):
	boxRobot.append([])
	wallsStorageSpaces.append([])
	for j in range(0,maxRowLength):
		boxRobot[-1].append('-')
		wallsStorageSpaces[-1].append('-')



## Making the board a rectangle even if the input is not one
for i in range(0,len(board)):
	if len(board[i])<maxRowLength:
		for j in range(len(board[i]),maxRowLength):
			board[i]+='O'


## Storing walls&storage spaces in one 2d array , boxes and robot in another 2d array
for i in range(0,len(board)):
	for j in range(0,maxRowLength):
		if board[i][j]=='B' or board[i][j]=='R':
			boxRobot[i][j]=board[i][j]
			wallsStorageSpaces[i][j]=' '
		elif board[i][j]=='S' or board[i][j]=='O':
			wallsStorageSpaces[i][j] = board[i][j]
			boxRobot[i][j] = ' '
		elif board[i][j]==' ':
			boxRobot[i][j] = ' '
			wallsStorageSpaces[i][j]=' '
		elif board[i][j] == '*':
			boxRobot[i][j] = 'B'
			wallsStorageSpaces[i][j] = 'S'
		elif board[i][j] == '.':
			boxRobot[i][j] = 'R'
			wallsStorageSpaces[i][j] = 'S'

##BFS

print ("Solving using BFS\n")

movesList=[]
visitedMoves=[]

## Adding source to queue
queue = collections.deque([])
source = [boxRobot,movesList]
if boxRobot not in visitedMoves:
	visitedMoves.append(boxRobot)
queue.append(source)
robot_x = -1
robot_y = -1
completed = 0
while len(queue)!=0 and completed==0:

	### Popping first item from the queue
	temp = queue.popleft()
	curPosition = temp[0]
	movesTillNow = temp[1]

	for i in range(0,lines):
		for j in range(0,maxRowLength):
			if curPosition[i][j]=='R':
				robot_y = j
				robot_x = i
				break
		else:
			continue
		break

	###Getting robot position of the popped element.

	for key in Moves:

		## Checking for all the four directions
		robotNew_x = robot_x+Moves[key][0]
		robotNew_y = robot_y+Moves[key][1] 
		curPositionCopy = copy.deepcopy(curPosition)

		movesTillNowCopy = copy.deepcopy(movesTillNow)
		if curPositionCopy[robotNew_x][robotNew_y] == 'B':

			## If there is a box after robot makes a move
			boxNew_x = robotNew_x + Moves[key][0]
			boxNew_y = robotNew_y + Moves[key][1]
			if curPositionCopy[boxNew_x][boxNew_y]=='B' or wallsStorageSpaces[boxNew_x][boxNew_y]=='O':
				## if the cell after robot pushes the box is another box or wall, avoid further steps.
				continue
			else:
				## if the robot can push the block
				curPositionCopy[boxNew_x][boxNew_y]='B'
				curPositionCopy[robotNew_x][robotNew_y] = 'R'
				curPositionCopy[robot_x][robot_y] = ' '
				if curPositionCopy not in visitedMoves:
					matches= 0
					for k in range(0,lines):
						for l in range(0,maxRowLength):
							if wallsStorageSpaces[k][l]=='S':
								if curPositionCopy[k][l]!='B':
									matches=1
					movesTillNowCopy.append(key)
					if matches == 0:
						completed = 1
						print ("Number of moves : {}\n{} \n".format(len(movesTillNowCopy),movesTillNowCopy))
					else:
						queue.append([curPositionCopy,movesTillNowCopy])
						visitedMoves.append(curPositionCopy)
		else:

			## if the robot moves into a wall
			if wallsStorageSpaces[robotNew_x][robotNew_y]=='O': 
				continue
			else:
				## if the robot moves into empty space
				curPositionCopy[robotNew_x][robotNew_y]='R'
				curPositionCopy[robot_x][robot_y]=' '
				if curPositionCopy not in visitedMoves:
					movesTillNowCopy.append(key)
					queue.append([curPositionCopy,movesTillNowCopy])
					visitedMoves.append(curPositionCopy)

if completed==0:
	print ("Can't make it")

time_end = time.time()
print (time_end-time_start)



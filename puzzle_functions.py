
def get_empty(puzzle):
	for i in range(len(puzzle)):
		if puzzle[i]==0: return i 

def generate_actions(puzzle):
	empty=get_empty(puzzle)
	actions=[]
	if empty not in [0,1,2]: actions.append('^') #empty>2
	if empty not in [6,7,8]: actions.append('v') #empty<6
	if empty not in [2,5,8]: actions.append('>') #empty%3==2
	if empty not in [0,3,6]: actions.append('<') #empty%3==0
	return actions

def apply_action(old_puzzle,action):
	puzzle=old_puzzle[:]
	empty=get_empty(puzzle)
	if action=='>':
		puzzle[empty],puzzle[empty+1]=puzzle[empty+1],puzzle[empty]
	if action=='<':
		puzzle[empty],puzzle[empty-1]=puzzle[empty-1],puzzle[empty]
	if action=='^':
		puzzle[empty],puzzle[empty-3]=puzzle[empty-3],puzzle[empty]
	if action=='v':
		puzzle[empty],puzzle[empty+3]=puzzle[empty+3],puzzle[empty]
	return puzzle

def check_puzzle(puzzle):
	for i in range(len(puzzle)):
		if puzzle[i]!=i: return False
	return True

def puzzle_cost(puzzle,action):
	return 1

def h1(puzzle):
	count=0
	for i in range(len(puzzle)):
		if puzzle[i]!=i : count+=1
	return count

def h2(puzzle):
	count=0
	for i in range(len(puzzle)):
		j=puzzle[i]
		if j!=i:
			count+= abs( int(j/3) - int(i/3) ) + abs( int(j%3) - int(i%3) )
	return count

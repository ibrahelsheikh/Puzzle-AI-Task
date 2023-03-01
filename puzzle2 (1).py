from puzzle_functions import*

def human_play(puzzle):
  while(True):
    print_puzzle(puzzle)
    available_moves=function1(puzzle)
    print("available moves:",available_moves)
    selected_moves=input("select a move:")
    if selected_moves not in available_moves:
        print("game over");break
    elif selected_moves in available_moves:
      puzzle=function2(selected_moves,puzzle)
    if function3(puzzle):
        print_puzzle(puzzle);print('you win');break
    

def print_puzzle(puzzle):
    p=''
    for i in puzzle:
        if i==0:p+=' '
        else :
            p+=str(i)
    print(
        '-'*13+'\n'+
        '|' + p[0] + '|' + p[1] + '|' + p[2] + '|' + '\n'
        '|' + p[3] + '|' + p[4] + '|' + p[5] + '|' + '\n'
        '|' + p[6] + '|' + p[7] + '|' + p[8] + '|' + '\n'
         +'-' * 13 + '\n'
    )
if __name__=='__main__':
    puzzle=[
        3,1,2,
        4,0,5,
        6,7,8]
    print_puzzle(puzzle)
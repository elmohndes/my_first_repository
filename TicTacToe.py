import random

#this function to draw board 
def drawBoard(board):
 print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
 print('-' * 10)
 print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
 print('-' * 10)
 print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
 print(' \n' * 2)
#this function to select player and computer symbols
def selectPlayer():
 while True:
  print('do you want to be X or O')
  letter = ''
  letter = input().upper()
  if letter == 'X':
   return ['X', 'O']
  elif letter == 'O':
   return ['O', 'X']

#this function to select if computer or player win
#we insert in it all possible combination which make winning
def selectWinner(board, let):
 return ((board[1] == board[2] == board[3] == let) or
         (board[4] == board[5] == board[6] == let) or
         (board[7] == board[8] == board[9] == let) or
         (board[1] == board[5] == board[9] == let) or
         (board[3] == board[5] == board[7] == let) or
         (board[1] == board[4] == board[7] == let) or
         (board[2] == board[5] == board[8] == let) or
         (board[3] == board[6] == board[9] == let))

#this function to see if there is an empty place in board
def isSpace(board, i):
  return board[i] == ' ' 

#this function to put items in empty places
def move(board, letter, place):
 if isSpace(board, place):
  board[place] = letter
  drawBoard(board)

#this function make copy of board
def copy(board):
 copyBoard = [' '] * 10
 y = 0
 for i in board:
  copyBoard[y] = i
  y = y + 1
 return copyBoard

#here we will start to write our algorithm to select winner
#here we see which step to take and make our computer or player win 
def expectWinner(board, letter):
 for i in range(1,10):
   makeCopy = copy(board)
   if isSpace(makeCopy, i):
    makeCopy[i] = letter
    if selectWinner(makeCopy, letter): 
     return i
 return -1

#here we make computer try to take corner or center
def computerMove(board, letter): 
 for i in '1 3 7 9'.split() :
  if isSpace(board, int(i)):
   move(board, letter, int(i))
   return
 if isSpace(board, 5):
  move(board, letter, 5)
  return
 for i in '2 4 6 8'.split():
  if isSpace(board, int(i)):
   move(board, letter, int(i))
   return

#here we take user input and put it in the board
def playerMove(board, letter):
 while True:
  print('please select value between(1-9)')
  inp = input()
  if inp in '1 2 3 4 5 6 7 8 9'.split():
   if not isSpace(board, int(inp)):
    print('this place has been played please try an empty place')
    continue
   move(board, letter, int(inp))
   break

def start(board, game):
 if random.randint(0,1) == 0:
  print('computer play first')
  computerMove(board, game[1])
  return 0
 else:
  playerMove(board, game[0])
  return 1

while True:
# here we make empty board
 board = [' '] * 10

#this variable to determine if someone win or not
 win = 0
#here we call selectPlayer game to select user symbol
 game = selectPlayer()
 x = start(board, game)
 if x == 0:
  for i in range(1,5):
   playerMove(board, game[0])
   if selectWinner(board, game[0]):
    print('you had won, congratulations!!!')
    w = 1
    break
   g = -1
#here we put expection for game after player because if game will win we don't need to see value for palyer
   g = expectWinner(board, game[1])
   if g != -1:
    print(g)
    move(board, game[1], g)
   elif g == -1:
    g = expectWinner(board, game[0])
    if g != -1:
     print(g)
     move(board, game[1], g)
   if g == -1:
     computerMove(board, game[1])
   if selectWinner(board, game[1]):
    print('Good luck')
    w = 1
    break

 if x == 1:
  for i in range(1, 5):
    r = -1
    r = expectWinner(board, game[1])
    if r != -1:
     print(r)
     move(board, game[1], r)
    elif r == -1:
     r = expectWinner(board, game[0])
     if r != -1:
      print(r)
      move(board, game[1], r)
    if r == -1:
      computerMove(board, game[1])
    if selectWinner(board, game[1]):
     print('Good luck')
     w = 1
     break
    playerMove(board, game[0])
    if selectWinner(board, game[0]):
     print('you had won, congratulations!!!')
     w = 1
     break

 if w == 0:
  print ('you have tied')

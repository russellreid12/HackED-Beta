"""
Text Based Chess
credits: Victor Kwok, Russel Reid
"""

import PIL as Image
import numpy as np 
import pygame
pygame.init()
#pygame.display.set_mode((500, 500)) 

class Board:
  def __init__(self):
    self.blank = '  '
    self.board = [[self.blank]*8]*8
    self.CurrentPlayer = 'w'
    self.gameOver = False

    self.checkMate = False
    self.inCheck = {"w":False, "b":False}
    self.moveHistory = []

  def __str__(self):
    #convert code representation of pieces into unicode chess pieces
    pieces=['♔','♕','♖','♗','♘','♙','♚','♛','♜','♝','♞','♟︎',' ']
    piecesCode = ['Kw','Qw','Rw','Bw','Nw','Pw','Kb','Qb','Rb','Bb','Nb','Pb',self.blank]
    printBoard = []
    for i in range(8):
      row = []
      for j in range(8):
        row.append(pieces[piecesCode.index(self.board[i][j])])
      printBoard.append(row)
    #print the board
    files = 'ABCDEFGH'
    s = ""
    for i in range(7,-1, -1):
      s += str(i+1) + str(printBoard[i]) + "\n"
    s+= '   A    B    C    D    E    F    G    H'
    return s
     
  def newGame(self):
    #reset the board to starting postion
    self.board[7] = ['Rb','Nb','Bb','Qb','Kb','Bb','Nb','Rb']
    self.board[6] = ['Pb']*8
    for i in range(3,6): self.board[i] = [self.blank]*8
    self.board[1] = ['Pw']*8
    self.board[0] = ['Rw','Nw','Bw','Qw','Kw','Bw','Nw','Rw']

  def inputToCoordinates(self,move):
    b=(ord(move[0].lower())-97) 
    a=int(move[1])-1
    d=(ord(move[3].lower())-97) 
    c=int(move[4])-1
    return a,b,c,d
  
  def validateMove(self, move):
    #move should be in format: A1 B2
    #check input format and convert to coordinates
    if not(len(move) == 5): return False
    if not (move[0].isalpha() and move[1].isnumeric() and move[3].isalpha() and move[4].isnumeric()): return False
    a,b,c,d = self.inputToCoordinates(move)
    if any([ (x not in range(8)) for x in [a,b,c,d]]): return False
    
    #check if selected square is empty
    if self.board[a][b] == self.blank: return False
    #check piece colour
    color = self.board[a][b][1]
    if color != self.CurrentPlayer: return False
    selectedPiece = self.board[a][b][0]

    return True
  
  def move(self, move):
    #move piece on (a,b) to (c,d)
    a,b,c,d = self.inputToCoordinates(move)
    self.board[c][d] = self.board[a][b]
    self.board[a][b] = self.blank
    if self.CurrentPlayer == 'w':
      self.CurrentPlayer = 'b'
    else: self.CurrentPlayer = 'w'
      
def main():
  board = Board()
  board.newGame()
  print(board)
  while(not board.gameOver):
    #get a valid move from user input
    move = input("Enter Next Move: ")
    valid = board.validateMove(move)
    while not valid:
      print("invalid move")
      move = input("Enter Next Move: ")
      valid = board.validateMove(move)
    board.move(move)
    print(board)
    
main()
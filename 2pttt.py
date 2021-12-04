
import random
#import getch
class Cell:
  "cell class for making cells"
  def __init__(self,x,y):
    'create new cells'
    self.alive1=False
    self.last1=False
    self.alive2=False
    self.last2=False
    self.x=x
    self.y=y
    # self.start=0
    # self.end=0
    self.p1act=False
    self.p2act=False
    
  def update(self,cells,direction):
#p1 and p2 move

    if (self.x==board.p1x and self.y==board.p1y)==True:
      self.alive1=True
    else:
      self.alive1=False
      
    # if   (self.x==board.p2x and self.y==board.p2y)==True:
    #   self.alive2=True
    # else:
    #   self.alive2=False


      


 
  def __str__(self):
    return "x=" + str(self.x) + ", y=" + str(self.y)


class Board:
  "does the stuff"
  def __init__ (self,width,height):
    "make the board"
    self.sizesq=200
    self.width=width
    self.height=height
    self.cells = []
    self.addcells(self.cells,self.width,self.height)
    self.starttimer=0
    self.endtimer=0

    self.p1x=self.width//4
    self.p1y=self.height//2

    self.p2x=3*self.width//4  
    self.p2y=self.height//2

    self.moves=0
    self.r1=255
    self.g1=255
    self.b1=255
    self.r2=0
    self.g2=255
    self.b2=0

    #color for when p1 activates
    self.r1a=150
    self.g1a=50
    self.b1a=200
    #color for when p2 activates
    self.r2a=0
    self.g2a=100
    self.b2a=100
    #color for selector
    self.rs=255
    self.gs=255
    self.bs=255
    #color for board
    self.rb=0
    self.gb=0
    self.bb=0
    
    

  def addcells(self,cells,width,height) : 
    for x in range(width):
      cells.append([])
      for y in range(height):
        cells[x].append(Cell(x, y))

  def initialize(self,setup):
    
    
    self.cells[self.p1x][self.p1y].alive1 = True
    # self.cells[self.p2x][self.p2y].alive2 = True
  
  def checkinput(self,direction):
    if direction == 'a':
      board.p1x=(board.p1x-1)%board.width

    elif direction == 'd':
      board.p1x=(board.p1x+1)%board.width
   
    elif direction == 'w':
      board.p1y=(board.p1y-1)%board.height
    
    elif direction == 's':
      board.p1y=(board.p1y+1)%board.height


#draw button pressed    
    elif direction == 'p':
      #if not already
      if (self.cells[self.p1x][self.p1y].p1act==False) and (self.cells[self.p1x][self.p1y].p2act==False):
        if self.moves % 2 == 0:
          self.cells[self.p1x][self.p1y].p1act=True
          self.draw(canvas,True)
          print("player 2's turn")
          #incrment moves and check for win            
          self.moves+=1
          self.didP1Win()
          self.didP2Win()
        else:
          board.cells[board.p1x][board.p1y].p2act=True
          self.moves+=1
          self.didP1Win()
          self.didP2Win()
          self.draw(canvas,True)
          print("player 1's turn")
      else:
        print("\nalready taken sptuid\n")          

  def update(self,direction):
    
    self.checkinput(direction)
   #process input
   #incrment moves and check for win
         
  
  #did someone just win?^       
    if self.moves==9:
      input ("\ntie\npress enter to play again\n")
      self.reset()   
    
    if self.didP1Win()==True:
      input("\nplayer 1 wins!\npress enter to play again\n")
      self.reset() 
      self.draw(canvas,True)
    elif  self.didP2Win() == True:
      input("\nplayer 2 wins!\npress enter to play again\n")
      self.reset() 
      self.draw(canvas,True)

#alive to last for selector
    for i in range(self.width):
      for cell in self.cells[i]:
        cell.last1 = cell.alive1

    # for i in range(self.width):
    #   for cell in self.cells[i]:
    #     cell.last2 = cell.alive2  

#update all
    for i in range (self.width):
      for cell in self.cells[i]:
        cell.update(self.cells,direction)

  def reset(self):
    #for all cells
    for i in range(self.width):
      for cell in self.cells[i]:
        # set all to false 
        cell.p1act=False
        cell.p2act=False
        #cell.alive1=False

    self.draw(canvas,True)
    self.didP1Win()==False
    self.didP2Win()==False
    self.moves=0

  def didP1Win(self):

    #horiz check
    for i in range(self.width):
      if (self.cells[i][0].p1act==True) and (self.cells[i][1].p1act==True) and (self.cells[i][2].p1act==True):
        return True
    #vert check
    for i in range(self.height):
      if (self.cells[0][i].p1act==True) and (self.cells[1][i].p1act==True) and (self.cells[2][i].p1act==True):
        return True
    i=0
    ii=(self.width-1)
    #diag checks
    if (self.cells[i][i].p1act==True) and (self.cells[i+1][i+1].p1act==True) and (self.cells[i+2][i+2].p1act==True):
        return True
    if (self.cells[ii][i].p1act==True) and (self.cells[ii-1][i+1].p1act==True) and (self.cells[ii-2][i+2].p1act==True):
        return True

  def didP2Win(self):
    
    #horiz check
    for i in range(self.width):
      if (self.cells[i][0].p2act==True) and (self.cells[i][1].p2act==True) and (self.cells[i][2].p2act==True):
        return True
    #vert check
    for i in range(self.height):
      if (self.cells[0][i].p2act==True) and (self.cells[1][i].p2act==True) and (self.cells[2][i].p2act==True):
        return True
    i=0
    ii=(self.width-1)
    #diag checks
    if (self.cells[i][i].p2act==True) and (self.cells[i+1][i+1].p2act==True) and (self.cells[i+2][i+2].p2act==True):
        return True
    if (self.cells[ii][i].p2act==True) and (self.cells[ii-1][i+1].p2act==True) and (self.cells[ii-2][i+2].p2act==True):
        return True
    
      
    

  def draw(self, canvas, force):
    
    if force == True:
      for i in range(self.width):
        for cell in self.cells[i]:
          
    #if force is True       
          if cell.alive1 == True:
        #if p1 is activated, avg the selector(rs) and p1 color(r1a)
              if cell.p1act ==True:
                canvas.setFillColor((self.rs+self.r1a)//2, (self.gs+self.g1a)//2, (self.bs+self.b1a)//2)
        #if p2 is activated, avg the selector(rs) and p1 color(r2a)
              elif cell.p2act ==True:
                  canvas.setFillColor((self.rs+self.r2a)//2, (self.gs+self.g2a)//2, (self.bs+self.b2a)//2)
        #if neither, avg the selector(rs) and board(rb)
              else: 
                canvas.setFillColor((self.rs+self.rb)//2, (self.gs+self.gb)//2, (self.bs+self.bb)//2)

          # elif cell.alive2==True:
          #   canvas.setFillColor(self.r2, self.g2, self.b2)
          elif cell.p1act==True:
            canvas.setFillColor(self.r1a, self.g1a, self.b1a)
          elif cell.p2act==True:
            canvas.setFillColor(self.r2a, self.g2a, self.b2a)
          else:
            canvas.setFillColor(0,0,0)
         
          canvas.drawRectFill(cell.x*self.sizesq,cell.y*self.sizesq,
          self.sizesq,self.sizesq)
    #if force is False   
    else: 
      
      for i in range(self.width):
        for cell in self.cells[i]:
#if change
          if cell.alive2 != cell.last2 or cell.alive1 !=cell.last1:
#if selector (alive1), 
            if cell.alive1 == True:
        #if p1 is activated, avg the selector(rs) and p1 color(r1a)
              if cell.p1act ==True:
                canvas.setFillColor((self.rs+self.r1a)//2, (self.gs+self.g1a)//2, (self.bs+self.b1a)//2)
        #if p2 is activated, avg the selector(rs) and p1 color(r2a)
              elif cell.p2act ==True:
                  canvas.setFillColor((self.rs+self.r2a)//2, (self.gs+self.g2a)//2, (self.bs+self.b2a)//2)
        #if neither, avg the selector(rs) and board(rb)
              else: 
                canvas.setFillColor((self.rs+self.rb)//2, (self.gs+self.gb)//2, (self.bs+self.bb)//2)

            # elif cell.alive2==True:
            #   canvas.setFillColor(self.r2, self.g2, self.b2)
            elif cell.p1act==True:
              canvas.setFillColor(self.r1a, self.g1a, self.b1a)
            elif cell.p2act==True:
              canvas.setFillColor(self.r2a, self.g2a, self.b2a)
            else:
              canvas.setFillColor(0,0,0)
            canvas.drawRectFill(cell.x*self.sizesq,cell.y*self.sizesq,
          self.sizesq,self.sizesq)
    canvas.display()
    

    



board=Board(3,3)
import picture
canvas = picture.Picture(800,600)




def main():
  import time
  setup = 1
  board.initialize(setup)
  board.draw(canvas,True)
  time.sleep(1)
  
  #input("\nWelcome to Eating Contest!\n---------------------------\nRULES:\n-player 1 moves with the WASD keys\n-player 2 moves with the IJKL keys\n-eet dots and turn red to WIN\n-eat the blue dots to freeze your opponent \n-buttonmash to get unfrozen quickly!\n   --press enter to begin--")
  


  while 1 == 1:
    #direction = getch.getch()
    direction = input()
    if direction.upper() == 'S' or  direction.upper() == 'W' or direction.upper() == 'A' or direction.upper() == 'D' or direction.upper() == 'J'or  direction.upper() == 'K'or  direction.upper() == 'L'or  direction.upper() == 'I'or  direction.upper() == 'P':
    
      board.update(direction)
      board.draw(canvas,False)
    
    
    #time.sleep(0.1)
    
    
    
main()
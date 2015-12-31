from random import*
from stack import*
from graphics import*

#the graphics version I used (and will include in submission) has the function def yUp()

"""creating a maze of the class Maze will ALSO run both the explore functions, mapping from (1,1) to
a randomly placed key (noted by a orange circle) and then will map in a different colour to
the end (n,n). """




class Maze:
    
    def __init__(self,n:'cells across/vertical of the nxn maze'):
        self.n = n  #the variable that is the number of cells across and up/down
        
        self.row = [True for i in range(n+2)] #a row of trues to make the grid below
        self.north = [self.row[:] for i in range (n+2)] #n +2 because range doesnt use the last number in the range
        self.south =  [self.row[:] for i in range (n+2)] #for  example in a 3x3 matrix it will go from 0 to 4
        self.east =  [self.row[:] for i in range (n+2)]
        self.west =  [self.row[:] for i in range (n+2)]
        self.explore = [self.row[:] for i in range (n+2)] #true that all the squares are UNVISITED

        self.visitedCells = 1
        self.totalCells = n*n
        
        self.c = MyStack()
        self.x,self.y = 1,1 #current Cell Location


        self.win = GraphWin('Maze', 700,700)
        self.win.yUp()


        self.makemaze()
        self.draw()
    
    





        

    def makemaze(self):


        while self.visitedCells != self.totalCells:
    
            self.explore[self.y][self.x] = False





            #find an option
            M = self.option()

            if M == 0:
                    #go back
                    #continue the while loop
                if (self.x,self.y) == self.c.peek():
                    self.c.pop()
                    (self.x,self.y) = self.c.peek()
                else:
                    (self.x,self.y) = self.c.peek()

            else:
                
                self.c.push((self.x,self.y))
                self.x,self.y,self.north, self.east, self.south, self.west = self.newCell(M)

                self.visitedCells +=1
                

        self.explore[self.y][self.x] = False
            
     




    def option(self):
        options = []
        if self.north[self.y][self.x] == True:           #NORTH
            #if there is no walls taken down
                #add as an option
            if self.y-1 > 0 and self.y-1 < self.n+1: 
                if self.explore[self.y-1][self.x] != False:
                    options = options + ['N']#[(x,y-1)]
        if self.south[self.y][self.x] == True:           #SOUTH
            # if there is no south wall
                #add as an option
            if self.y+1 > 0 and self.y+1 < self.n+1:
                if self.explore[self.y+1][self.x] != False:
                     options = options + ['S']#[(x,y+1)]
        if self.east[self.y][self.x] == True:            #EAST
            # if there is no wall taken down
                #add as an option
            if self.x+1 > 0 and self.x+1 < self.n+1:
                if self.explore[self.y][self.x+1] != False:
                     options = options + ['E']#[(x-1,y)]
        if self.west[self.y][self.x] == True:             #WEST
            #if there is no wall west taken down
                #add as an option
            if self.x-1 > 0 and self.x-1 < self.n+1:
                if self.explore[self.y][self.x-1] != False:
                     options = options + ['W']#[(x+1,y)]

       
        

        if len(options) == 0:           #we need to go back the way we came
            return 0
        else:
            k = options[randint(0,len(options)-1)]          #pick a random way to go
            return k


        
    def newCell(self,k):     #this is reassigning the new x,y from the random selection of options
        if k == 'N':
            self.north[self.y][self.x] = False
            #get rid of the north wall
            self.x,self.y = self.x, self.y-1
            self.south[self.y][self.x] = False
            #return the x,y coordinates of the north cell
            #get rid of the south wall of the north cell
            return self.x,self.y, self.north,self.east,self.south, self.west #returns an update of all lists (some will be changed, some not depending on the direction
        elif k == 'E':
            self.east[self.y][self.x] = False
            self.x,self.y = self.x+1, self.y
            self.west[self.y][self.x] = False
            return self.x,self.y,self.north,self.east, self.south, self.west
        elif k == 'S':
            self.south[self.y][self.x] = False
            self.x,self.y = self.x,self.y+1
            self.north[self.y][self.x] = False
            return self.x,self.y,self.north, self.east, self.south, self.west
        else:
            self.west[self.y][self.x] = False
            self.x,self.y = self.x-1,self.y
            self.east[self.y][self.x] = False
            return self.x,self.y,self.north,self.east,self.south,self.west

        
        

        
    def draw(self):

        self.win.setBackground("black") #going for a pac man theme
        
        size = 700/self.n #used to draw the points for the lines (the walls)


        #this is checking all the lists for all the x,y combinations and drawing the walls for where it is
        #set to False
        
        for y in range(0, (self.n)):
            for x in range(0, (self.n)):
                if self.east[y+1][x+1] == True:
                    #draw line
                    line = Line(Point((x*size) + size,y*size),Point( (x*size)+ size ,(y*size)+ size))
                    line.setWidth(3)
                    line.setFill('blue')
                    line.draw(self.win)
                if self.north[y+1][x+1] == True:
                    #draw line
                    line = Line(Point(x*size,y*size) ,Point((x*size)+size,y*size))
                    line.setWidth(3)
                    line.setFill('blue')
                    line.draw(self.win)
                if self.south[y+1][x+1] == True:
                    #draw line
                    line = Line(Point(x*size,(y*size)+size),Point((x*size)+size,(y*size)+size))
                    line.setWidth(3)
                    line.setFill('blue')
                    line.draw(self.win)
                if self.west[y+1][x+1] == True:
                    #draw line
                    line = Line(Point(x*size,y*size),Point(x*size,(y*size)+size))
                    line.setWidth(3)
                    line.setFill('blue')
                    line.draw(self.win)

        
        p, r = self.exploreMazeKey(1,1)     #this explore is for finding the key!!
        self.exploreMazeExit(p,r)           #this one is for going from the key to the exit

        #The two are mostly the same but Key takes the start origin (i used 1,1 but if you change this, it can go from any location)
        #the Exit one, takes the returned vales from key(the random key location and uses that as the start x and start y
        

                    
        
    def exploreMazeExit(self,x,y):
        
            startx, starty = x,y    #it seems redundant but at the end of this function I used the startx and starty
                                    # to draw a bigger circle for where the start is


            self.x, self.y = x,y    #these will actually be used


            endx, endy = self.n, self.n     #the exit is in the top right always


                #goal is to get to the end location

            
            explore = [self.row[:] for i in range(self.n+2)]
            #resetting the explore lists so that it starts over


                   
                

                
            p = MyStack()
            #the stack lets me follow my trail backwards

            explore[self.y][self.x] = False

            #implement a while loop that checks that self.x and self.y are not endx,endy



            while (self.x,self.y) != (endx,endy):

            #for my options, in order to make the most direct method, I prioritize the South and East
            #directions because i know that no matter what, my end N,N exit is always in that direction
            #in all the trials, this has proven to be the most eloquent way (although im sure there is some
            #other way I have not thought of)

                if (self.south[self.y][self.x] == False) and (explore[self.y+1][self.x] == True):
                    #add to the stack
                       p.push((self.x,self.y))
                        #change self x and self y
                       self.x,self.y = self.x, self.y+1
                       explore[self.y][self.x] = False
                elif self.east[self.y][self.x] == False and explore[self.y][self.x+1] == True:
                        #change self x and self y
                    p.push((self.x,self.y))
                    self.x,self.y = self.x+1,self.y
                    explore[self.y][self.x] = False
                elif self.west[self.y][self.x] == False and explore[self.y][self.x-1] == True:
                        #change self x and self y
                    p.push((self.x,self.y))
                    self.x,self.y = self.x-1,self.y
                    explore[self.y][self.x] = False
                elif self.north[self.y][self.x] == False and explore[self.y-1][self.x] == True:
                        #change self x and self y
                    p.push((self.x,self.y))
                    self.x,self.y = self.x,self.y-1
                    explore[self.y][self.x] = False
                else:
                    if (self.x,self.y) == p.peek():
                        p.pop()
                        (self.x,self.y) = p.peek()
                        #like with the maze creation, we dont want to pop the value until we are sure we
                        #are backtracking past that value instead of backing up once and changing direction
                    else:
                        (self.x,self.y) = p.peek()
                        #the peek is handy so we dont lost that value from our stack
                

            

            for i in p.items:
                #iterating through the stack to draw the path
                start = Circle(Point((startx*700/self.n)-(700/self.n)/2,(starty*700/self.n)-(700/self.n)/2),(700/self.n)/4)
                start.setFill('orange') 
                start.draw(self.win)
                #key colour (this is consistent with the key function
                
                path = Circle(Point((i[0]*700/self.n)-(700/self.n)/2,(i[1]*700/self.n)-(700/self.n)/2),(700/self.n)/8)
                path.setFill('red')
                path.draw(self.win)
                #path from key to finish
                    
            
    
                finish = Circle(Point((endx*700/self.n)-(700/self.n)/2,(endy*700/self.n)-(700/self.n)/2),(700/self.n)/4)
                finish.setFill('red')
                finish.draw(self.win)
                #finish colour

            
                    

            p.push((endx,endy))
            #added after because I didnt want to draw this one the same (i drew the finish circle above instead)
                

            
                

    def exploreMazeKey(self,x,y):
                startx, starty = x,y
                
                self.x, self.y = x,y


                endx, endy = randint(1,self.n), randint(1,self.n)

                #goal is to get to the end location (key)
                
                #resets the explore table 
                explore = [self.row[:] for i in range(self.n+2)]

      

                    
                p = MyStack()
                explore[self.y][self.x] = False

                #implement a while loop that checks that self.x and self.y are not endx,endy

                #this one needs to prioritize the E/W side that is closer to the key
                #as well as check if it is north/south of the key

                while (self.x,self.y) != (endx,endy):
                    if (self.x >= endx) and (self.y >= endy):
                        #Go north WEst
                        if (self.north[self.y][self.x] == False) and (explore[self.y-1][self.x] == True):
                                #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x,self.y-1
                            explore[self.y][self.x] = False
                        elif (self.west[self.y][self.x] == False) and (explore[self.y][self.x-1] == True):
                            #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x-1,self.y
                            explore[self.y][self.x] = False
                        elif (self.east[self.y][self.x] == False) and (explore[self.y][self.x+1] == True):
                            #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x+1,self.y
                            explore[self.y][self.x] = False
                        elif (self.south[self.y][self.x] == False) and (explore[self.y+1][self.x] == True):
                                #add to the stack
                            p.push((self.x,self.y))
                                #change self x and self y
                            self.x,self.y = self.x, self.y+1
                            explore[self.y][self.x] = False
                        else:
                            if (self.x,self.y) == p.peek():
                                p.pop()
                                (self.x,self.y) = p.peek()
                            else:
                                (self.x,self.y) = p.peek()
                    elif (self.x >= endx) and (self.y <= endy):
                        #go South West
                        if (self.south[self.y][self.x] == False) and (explore[self.y+1][self.x] == True):
                                #add to the stack
                            p.push((self.x,self.y))
                                #change self x and self y
                            self.x,self.y = self.x, self.y+1
                            explore[self.y][self.x] = False
                        elif (self.west[self.y][self.x] == False) and (explore[self.y][self.x-1] == True):
                            #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x-1,self.y
                            explore[self.y][self.x] = False
                        elif (self.east[self.y][self.x] == False) and (explore[self.y][self.x+1] == True):
                            #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x+1,self.y
                            explore[self.y][self.x] = False
                        elif (self.north[self.y][self.x] == False) and (explore[self.y-1][self.x] == True):
                                #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x,self.y-1
                            explore[self.y][self.x] = False
                        else:
                            if (self.x,self.y) == p.peek():
                                p.pop()
                                (self.x,self.y) = p.peek()
                            else:
                                (self.x,self.y) = p.peek()
                    elif (self.x <= endx) and (self.y >= endy):
                        #go North East
                        if (self.east[self.y][self.x] == False) and (explore[self.y][self.x+1] == True):
                            #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x+1,self.y
                            explore[self.y][self.x] = False
                        elif (self.north[self.y][self.x] == False) and (explore[self.y-1][self.x] == True):
                                #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x,self.y-1
                            explore[self.y][self.x] = False
                        elif (self.south[self.y][self.x] == False) and (explore[self.y+1][self.x] == True):
                                #add to the stack
                            p.push((self.x,self.y))
                                #change self x and self y
                            self.x,self.y = self.x, self.y+1
                            explore[self.y][self.x] = False
                        elif (self.west[self.y][self.x] == False) and (explore[self.y][self.x-1] == True):
                            #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x-1,self.y
                            explore[self.y][self.x] = False

                        else:
                            if (self.x,self.y) == p.peek():
                                p.pop()
                                (self.x,self.y) = p.peek()
                            else:
                                (self.x,self.y) = p.peek()
                    else:
                        #go south East 
                        if (self.south[self.y][self.x] == False) and (explore[self.y+1][self.x] == True):
                                #add to the stack
                            p.push((self.x,self.y))
                                #change self x and self y
                            self.x,self.y = self.x, self.y+1
                            explore[self.y][self.x] = False
                        elif (self.east[self.y][self.x] == False) and (explore[self.y][self.x+1] == True):
                            #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x+1,self.y
                            explore[self.y][self.x] = False
                        elif (self.west[self.y][self.x] == False) and (explore[self.y][self.x-1] == True):
                            #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x-1,self.y
                            explore[self.y][self.x] = False
                        elif (self.north[self.y][self.x] == False) and (explore[self.y-1][self.x] == True):
                                #change self x and self y
                            p.push((self.x,self.y))
                            self.x,self.y = self.x,self.y-1
                            explore[self.y][self.x] = False
                        else:
                            if (self.x,self.y) == p.peek():
                                p.pop()
                                (self.x,self.y) = p.peek()
                            else:
                                (self.x,self.y) = p.peek()
                        





                for i in p.items:
                    start = Circle(Point((startx*700/self.n)-(700/self.n)/2,(starty*700/self.n)-(700/self.n)/2),(700/self.n)/4)
                    start.setFill('lime green') 
                    start.draw(self.win)

                    
                    path = Circle(Point((i[0]*700/self.n)-(700/self.n)/2,(i[1]*700/self.n)-(700/self.n)/2),(700/self.n)/8)
                    path.setFill('light green')
                    path.draw(self.win)
                        



                    
                    finish = Circle(Point((endx*700/self.n)-(700/self.n)/2,(endy*700/self.n)-(700/self.n)/2),(700/self.n)/4)
                    finish.setFill('orange')
                    finish.draw(self.win)

                


                        

                p.push((endx,endy))
                    
                
                return endx, endy
                #returns these to use as start coordinates for the exit explore function

            



def main():
    t = Maze(45)


main()








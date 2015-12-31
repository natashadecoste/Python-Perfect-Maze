class MyStack:
    """creates a stack, which is essentially an ordered list with a bunch of commands that
    are specific to it. It lets you check if the stack is empty (list is empty), push an item(add it to the end),
    pop the last item from the stack, and peek lets you return the last item from the stack
    without actually popping it. size lets you see the length of the stack (how many elements
    it contains and the __str__ makes it so you can print out the contents of the stack in a
    user friendly way!"""


    def __init__(self):
        self.items = []
        #initializes the stack to being an empty stack

        

    def isEmpty(self):
        return self.items == []
        #returns a boolean True if it stack is empty and False if it is not

    

    def push(self, item):
        self.items.append(item)
        #appends an item to the stack

        

    def pop(self):
        return self.items.pop()
        #returns the value of the last item and deletes it from the stack

    

    def peek(self):
        return self.items[len(self.items)-1]
        #shows the last item in the stack
        #help for this originated on the website below
        #http://interactivepython.org/runestone/static/pythonds/BasicDS/stacks.html

    

    def size(self):
        return len(self.items)
        #returns how many items in the list

    
    
    def __str__(self):
        return str(self.items)
        #prints out the stack in a user friendly way
        #used this in order to test my stack during the process of creating the maze




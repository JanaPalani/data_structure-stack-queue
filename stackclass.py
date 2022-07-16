
# raising the overflow and under folw error
class StackOverflowError(Exception):
    pass

class StackUnderflowError(Exception):
    pass

class QueueOverflowError(Exception):
    pass

class QueueUnderflowerror(Exception):
    pass

# creating a class stack 
class Stack:
    # sttign the parameterised constructor that get the size of the stack
    def __init__(self,length,stack_list):
        self.length = length
        self.stack_list = stack_list
    
    # method to push th e element 
    def push(self,element_push):
        if len(self.stack_list) > self.length :
            raise StackOverflowError
        else:
            self.stack_list.append(element_push)
    # method to pop the element 
    def pop(self):
        self.error = 0 
        if len(self.stack_list) == 0:
            raise StackUnderflowError
        else:
            return self.stack_list.pop()
    # method to check whether the stack is empty 
    def isempty(self):
        if len(self.stack_list) == 0 :
            print(True)
        else:
            print(False)
    # method to check whether the stack is full
    def isfull(self):
        if len(self.stack_list) == self.length:
            print(True)
        else:
            print(False)
    
    # method to know the top value of the stack 
    def top(self):
        self.top_value  = len(self.stack_list)-1

    # method to dispaly the stack 
    def display(self):
        print(self.stack_list)


# definign a class queue
class Queue:
    # constructor which get the size of the queue 
    def __init__(self,size):
        self.size = size
        self.queue = []
    
    #  method to push an element in the queue
    def push(self,element_push):
        if len(self.queue) > self.size :
            raise QueueOverflowError
        else:
            self.queue.append(element_push)
    #  method to pop an element in the queue
    def pop(self):
        if len(self.queue) == 0:
            raise QueueUnderflowerror
        else:
            return self.queue.pop(0)
    
    # method to check whether the queue is empty 
    def isempty(self):
        if len(self.queue) == 0 :
            print(True)
        else:
            print(False)
    
    # method to check whether the queue is full
    def isfull(self):
        if len(self.queue) == self.size:
            print(True)
        else:
            print(False)

    # method to find the front pointer of the queue 
    def frontpointer(self):
        if self.isempty():
            print(-1)
        else:
            print(0)

    # method to find the rear pointer of the queue 
    def rearpointer(self):
        if self.isfull():
            print(len(self.queue) - 1)
        else:
            print(-1)
    # method to display the queue 
    def dispaly(self):
        print(self.queue)





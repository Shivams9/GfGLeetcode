class Queue:
    def __init__(self):
        self.data = []
    def enque(self, value):
        self.data.append(value)
    def empty(self):
        if len(self.data) <= 0:
            return True
        else:
            return False

    def deque(self):
        if self.empty():
            return None
        else:
            return self.data.pop(0)


'''
0-Exit, 1-Enque, 2-Deque,3-All,


'''
q=Queue()
while True:
    choice = int(input('Option: 0=Exit/1=Enque/2=Deque/3=All\n'))
    if choice == 0:
        print('Exit\n')
        break
    elif choice == 1:
        a=int(input('Enter'))
        q.enque(a)
        print('Enque')
    elif choice == 2:
        x=q.deque()
        print(x)
        print('Deque')
    elif choice == 3:
        print(q.data)
        print('All')

    else:
        print('Invalid Number')

list=[1,2,3,4,5]
print(list)
#NODE 
class Node:
    def __init__(self,data):
        self.data=data()
        self.next=None()
        print("Node created with data:",self.data)

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self,value):
        new_value=Node(value=value)
        self.head=new_value
        self.tail=new_value
        self.length=1
    
    
    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def append(self,value):
        newNode=Node(value=value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
            
            


 
my_linked_list = LinkedList(4)


print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
print(my_linked_list.printLL())
my_linked_list.append(56)
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
print(my_linked_list.printLL())
# my_linked_list.append(56)
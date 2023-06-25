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
            
    def prepend(self,value):
        newNode=Node(value=value)
        if self.length==0:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.length+=1
        return True
        
                
    def pop(self):
        if self.head is None:
            return None
        else:
            pre=self.head
            temp=self.head
            while(temp.next is not None):
                pre=temp
                temp=temp.next


            self.tail=pre
            self.tail.next=None
            self.length-=1
            if self.length==0:
                self.head=None
                self.tail=None
            return temp.value

my_linked_list = LinkedList(4)

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
# print(my_linked_list.printLL())
# my_linked_list.append(56)
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
# my_linked_list.append(56)
# my_linked_list.append(76)
# my_linked_list.append(76)

# print(my_linked_list.printLL())
# print(my_linked_list.pop())
# print(my_linked_list.printLL())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.printLL())
# print(my_linked_list.pop())
print(my_linked_list.printLL())
my_linked_list.prepend(3)
print(my_linked_list.printLL())
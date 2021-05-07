'''
Cracking the coding interview
Chapter 2 - Linked List pg 92
Linked List
----------------------------------------
Summary: Learning linked list
Constraits or Questions you need to ask:

Solution notes:

'''
#Node class
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

#Wrapper class
class linked_list:
    def __init__(self):
        self.head = node()

    #Add a node to the end of a linked list
    def append(self,data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
    
    #Getting the length of the linked list
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    #Print all data in current linked list as an array
    def display(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)
    #Print all data in current linked list using standard printing 
    def printLinkedList(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)

    #Get data at paticular index within the linked list
    def get(self, index):
        if index >= self.length():
            print("ERROR: 'GET' Index out of bounds")
            return None

        current_index = 0
        current_node = self.head

        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1 

    def remove(self,index):
        if index >= self.length():
            print("ERROR: 'GET' Index out of bounds")
            return None

        current_index = 0
        current_node = self.head
        while True:
            lastNode = current_node
            current_node = current_node.next
            if current_index == index:
                lastNode.next = current_node.next
                return
            current_index += 1

    def removeAtData(self, d):
        cur_node = self.head
        
        while cur_node != None:
            last_node = cur_node
            if(cur_node.data == d):
                print(d)
                tempNode.next = cur_node.next
                return
            tempNode = last_node
            cur_node = cur_node.next
        print("Data was not found within list")

        





myList = linked_list()
#While list is empty
#myList.display()

#Adding elements to linked list
myList.append(2)
myList.append(4)
myList.append(5)
myList.append(2)
myList.append(8)
myList.append(7)
#Display after adding elements into linked 
#myList.display()
#Display linked list as regular print
#myList.printLinkedList()
myList.display()
myList.removeAtData(7)
myList.display()


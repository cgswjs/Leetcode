class Node:
  def __init__(self,data = None):
    self.data = data
    self.next = None
  
class LinkedList:
  def __init__(self):
    self.head = None

  # create a linked list by putting new node at the begining  
  def push(self,new_data):
    #create new node
    new_node = Node(new_data)
    #pointer to previous head
    new_node.next = self.head
    #update head to current head
    self.head = new_node

  def addTwo(self,num1,num2):
    #input num1 and num2 are the head of linked list
    prev = None 
    temp = None #use to store calculated value for current digit
    carry = 0 #used to add 1 to next digit if current digit is exceeding 10
    while num1 != None or num2 != None:
      # get current digit of linked list
      if num1 != None:
        n1 = num1.data
      else:
        n1  = 0

      if num2 != None:
        n2 = num2.data
      else:
        n2 = 0

      #calculation and check for carry
      curSum = carry + n1+ n2
      if curSum >= 10:
        curSum = curSum %10
        carry =1
      else:
        curSum = curSum
        carry = 0

      temp = Node(curSum)

      #check temp linked list
      if self.head is None:
        self.head = temp
      else:
        prev.next = temp
      
      #not understand!!!!!!?????
      prev = temp
  
      if num1 != None:
        num1 = num1.next
      if num2 != None:
        num2 = num2.next

    #when while loop breaks, if there is a carry =1 we need to give the result one more digit at the end of linked list
    if carry > 0:
      temp.next = Node(carry)
    
  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next


# initialize linklist
linklist1 = LinkedList()
linklist1.push(5)
linklist1.push(6)

linklist2 = LinkedList()
linklist2.push(7)
linklist2.push(9)

#adding
linklist3 = LinkedList()
linklist3.addTwo(linklist1.head,linklist2.head)
print(linklist3.printList())


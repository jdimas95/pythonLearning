class Node():
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def prepend(self, data):
        if (self.head == None):
            self.head = Node(data)
            return
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def appendAfterSpecific(self, appendedAfter, data):
        if (self.head == None):
            self.head = Node(data)
            return
        current = self.head
        while(current):
            if (current.value == appendedAfter):
                tempNode = Node(data)
                tempNode.next = current.next
                current.next = tempNode
                return
            current = current.next


    def appendAtEnd(self, data):
        if (self.head == None):
            self.head = Node(data)
            return
        lastval = self.head
        while (lastval.next != None):
            lastval = lastval.next
        lastval.next = Node(data)

    def printLinkedList(self):
        if (self.head == None):
            print("No values in list!")
            return
        printval = self.head
        try:
            while (printval.value != None):
                print(printval.value)
                printval = printval.next
        except AttributeError:
            pass
        #used for spacing
        print("\n")

newLinkedList = LinkedList()
newLinkedList.appendAtEnd(1)
newLinkedList.appendAtEnd(2)
newLinkedList.appendAtEnd(4)
newLinkedList.printLinkedList()
newLinkedList.prepend(0)
newLinkedList.printLinkedList()
newLinkedList.appendAfterSpecific(2,3)
newLinkedList.printLinkedList()
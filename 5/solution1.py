
class Node():
    def __init__(self, data, next = None, parent = None):
        self.data = data
        self.next = next
        self.parent = parent
    
    def __str__(self):
        return self.data

class PolymerList():
    def __init__(self, first = None, last = None):
        self.first = first
        self.last = last
        self.length = 0
        
    def __str__(self):
        res = ""
        n = self.first
        while n != None:
            res += n.data
            n = n.next
        return res
    
    def put(self, data):
        self.length += 1
        if self.last == None or self.first == None:
            n = Node(data)
            self.first = n
            self.last = n
        else:
            n = Node(data)
            if self.reacts(self.last, n):
                self.last = self.last.parent 
                if self.last == None:
                    self.first = None
                else:
                    self.last.next = None
            else:
                n.parent = self.last
                self.last.next = n
                self.last = self.last.next
            

    
    def get(self):
        self.length -= 1
        if self.first == self.last:
            n = self.last.data
            self.first = None
            self.last = None
        else:
            n = self.first.data
            self.first = self.first.next
        return n
    
    def reacts(self, a, b):
        return (abs(ord(a.data) - ord(b.data))) == 32

    def peek(self):
        return self.first.data

    def isEmpty(self):
        return self.length == 0
    

indata = open("indata_test.txt", "r")
poly = indata.readline().strip()
p = PolymerList()
for c in poly:
    p.put(c)
print(p)
indata.close()





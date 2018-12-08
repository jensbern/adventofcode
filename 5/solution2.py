
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
                self.length -= 2
                self.last = self.last.parent 
                if self.last == None:
                    self.first = None
                else:
                    self.last.next = None
            else:
                n.parent = self.last
                self.last.next = n
                self.last = self.last.next
    
    def reacts(self, a, b):
        return (abs(ord(a.data) - ord(b.data))) == 32
    

indata = open("indata_test.txt", "r")
poly = indata.readline().strip()

p = PolymerList()
for c in poly:
    p.put(c)
print(p.length)
indata.close()





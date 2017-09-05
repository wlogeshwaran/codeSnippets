class node:

        
    def __init__(self,data,next):
        self.data = data;
        self.next = next;



class create:        
    def __init__(self):
        self.head = None;

        
    def app(self, data):
        if self.head is None:
            self.no = node(data,None)
            self.head = self.no
            self.point = self.no

        else:
            self.no = node(data,None)
            self.point.next = self.no
        self.point = self.no
        
    def show(self):
        self.point = self.head
        while self.point.next is not None:
            print self.point.data
            self.point = self.point.next
        
        
a = create()
a.app(100)
a.app(200)
a.app(300)
a.app(400)
a.app(500)
a.app(600)
a.show()
            
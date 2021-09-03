class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item)
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;
    
    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def get_count(self): #harus di Print
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

    def urutkan(self):
        current = self.start_node
        index = None
        if(self.start_node == None):
            return
        else:  
            while(current is not None):   
                index = current.ref
                while(index is not None):  
                    if(current.item > index.item):  
                        x = current.item
                        current.item = index.item
                        index.item = x 
                    index = index.ref 
                current = current.ref       

    def jumlahan(self):
        tampung = []
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                tampung.append(n.item)
                n = n.ref
            return sum(tampung)

    def reverse(self):
        prev = None
        current = self.start_node
        while(current is not None):
            self.ref = current.ref
            current.ref = prev
            prev = current
            current = self.ref
        self.start_node = prev


    def akhiran(self):
        n = self.start_node
        while n.ref is not None:
            n = n.ref
            self.akhir = n
        return self.akhir
        
    def combine(self, linked2, x = 1):
        if x == 1:
            self.akhiran()
            self.akhir.ref = linked2.start_node
            
print("SOAL NOMOR 1")
print("="*30)
print("Anggota Listnya adalah [1,3,9]")
data1 = LinkedList()
data1.insert_at_start(3)
data1.insert_at_end(9)
data1.insert_at_start(1)
data1.traverse_list()
print("Jumlah keseluruan data ada {} angka".format(data1.get_count()))
print("Jumlah total data keseluruhan {}".format(data1.jumlahan()))

print("\n")

print("Anggota Listnya adalah [2,1,4]")
data2 = LinkedList()
data2.insert_at_start(1)
data2.insert_at_end(4)
data2.insert_at_start(2)
data2.traverse_list()
print("Jumlah keseluruan data ada {} angka".format(data2.get_count()))
print("Jumlah total data keseluruhan {}".format(data2.jumlahan()))

print("\n")

print("SOAL NOMOR 2")
print("="*60)
print("Gabungan dari linked list diatas yaitu = [1,3,9] dan [2,1,4]")
data1.combine(data2)
data1.traverse_list()

print("\n")

print("SOAL NOMOR 3")
print("="*32)
print("Anggota Listnya adalah [9,4,3,6]")
data4 = LinkedList()
data4.insert_at_start(4)
data4.insert_at_start(9)
data4.insert_at_end(3)
data4.insert_at_end(6)
print("Sebelum Terurut")
data4.traverse_list()
print("Sesudah Terurut")
data4.urutkan()
data4.traverse_list()

print("\n")

print("SOAL NOMOR 4")
print("="*30)
print("Anggota Listnya adalah [1,2,3]")
data5 = LinkedList()
data5.insert_at_start(2)
data5.insert_at_start(1)
data5.insert_at_end(3)
print("Sebelum Reverse")
data5.traverse_list()
print("Sesudah Reverse")
data5.reverse()
data5.traverse_list()

#pascalCase---> holaMundo
#

from ast import Not
from hashlib import new
from os import remove
from pickle import NONE


class CircularSingleLinkedList:
    #metodo inicializador clase singlelinkedlist
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    class Node:
        #metodo inicializador clase node
        def __init__(self,value):
            self.value=value
            self.next=None
        """ def __str__(self):
            return str(self.value) """
        
    def __str__(self):
        bandera=True
        current= self.head
        lista=[]
        while current != self.head or bandera:
            bandera=False
            lista.append(current.value)
            current=current.next
            
        return str(lista)
    def unshift_node(self,value):
        new_node=self.Node(value)
        #Caso en que no existan nodos en la lista
        if self.head is None and self.tail is None:
            self.head= new_node
            self.tail= new_node
            self.tail.next=self.head
        #casos en el que almenos exita un  nodo
        else:
            self.tail.next= new_node
            new_node.next= self.head
            self.head= new_node
            
        self.size+=1
        
    def append_node(self,value):
        new_node=self.Node(value)
        #Caso en que no existan nodos en la lista
        if self.head is None and self.tail is None:
            self.head= new_node
            self.tail= new_node
            self.tail.next=self.head
        #casos en el que almenos exita un  nodo
        else:
            self.tail.next= new_node
            new_node.next= self.head
            self.tail= new_node
        self.size+=1
        
        
    """   while node_counter!= 0:
            #Validamos si el nodo actual no es la cabeza 
            if current_node !=self.head or pivote :
                circular_list.append(current_node.value)
                #pasamos al siguiente nodo
                current_node= current_node.next
                pivote=False
                #disminuimos la cantidad de nodos
                node_counter-=1 """
    def pop_node(self):
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            counter = 1
            current_node = self.head
            new_tail = self.tail
            while counter < self.size:
                new_tail = current_node
                current_node = current_node.next
                counter+=1
            self.tail = new_tail
            self.tail.next = self.head
            self.size -= 1

    def get_node(self, index):
        if index < 1 and index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            counter = 1
            while counter != index:
                current_node = current_node.next
                counter += 1
            return current_node

    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            print(self.head.value)
        elif index == self.length:
            print(self.tail.value)
        else:
            urrent_node = self.head
            counter = 1
            while counter != index:
                current_node = current_node.next
                counter += 1
            print(current_node.value)

    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            search_node.value = new_value
        else:
            return None

    def remove_node(self, index):
        if index == 1:
            self.shift_node()
        elif index == self.length:
            self.pop_node()
        else:
            remove_node = self.get_node(index)
            if remove_node != None:
                previous_node = self.get_node(index - 1)
                previous_node.next = remove_node.next
                remove_node.next = None
                self.length -= 1
    
    def insert_node(self, index, value):
        if index <= 0  or index > self.length+1:
            print('posicion erronea')
        elif index == 1:
            self.unshift_node(value)
        elif index == self.length+1:
            self.push_node(value)
        else: 
            previous_node = self.get_node(index - 1)
            next_node = self.get_node(index)
            new_node = self.Node(value)
            previous_node.next = new_node
            new_node.next = next_node
            self.length += 1
    def shift_nodee(self):
        if self.size>0:
            remove_node=self.head
            self.head=remove_node.next
            self.tail.next=self.head
            remove_node.next=None
            self.size-=1
        else:
            self.head=None
            self.tail==None
            
        pass
    def shift_node(self):
        if self.length == 0: 
            self.head = None
            self.tail = None
        else:
            remove_node = self.head
            self.tail.next = remove_node.next
            self.head = remove_node.next
            self.length -= 1
    
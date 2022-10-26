from Circular_single_linked_list import CircularSingleLinkedList
import numpy as np
import pandas as pd



if __name__== '__main__':
    dict={}
    for j in range (1,100):
        d = np.power(j,1/j)
        x = d
        for i in range(1000):
            x = np.power(d,x)
        dict[j]=x
        print(j,x)
    
    print(dict)
    archivo="nume.csv"
    csv=open(archivo,"w")
    titulo="numero\tresultado\n"
    csv.write(titulo)
    for key in dict.keys():
        numero=key
        resultado=dict[key]
        filas=str(numero)+"\t"+str(resultado)+"\n"
        csv.write(filas)
    
    """ list=CircularSingleLinkedList()
    list.unshift_node(5)
    print(list)
    list.pop_node()
    print(list)
    pass """
    
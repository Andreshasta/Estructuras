
#!/usr/bin/python
# -*- coding: utf-8 -
from pila import *
from arbol import *


def convertir(lista, pila):

    if lista != []:


        if lista[0] in "+-*/=":
            pila.apilar(Nodo(lista[0]))
            #nodo_der = pila.desapilar()
            #nodo_izq = pila.desapilar()
            #pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
            print "Expresion: |", lista[0],"| ", lista[1:]
        else:
            pila.apilar(Nodo(lista[0]))
            print "Terminal: |", lista[0],"| ", lista[1:]

        return convertir(lista[1:],pila)


# def dibujar(lista):
#     if lista != []:
#         if lista[0] in "+-*/=":
#             pila.apilar(Nodo(lista[0]))
#             #nodo_der = pila.desapilar()
#             #nodo_izq = pila.desapilar()
#             #pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
#             print "Expresion: |", lista[0],"| ", lista[1:]
#         else:
#             pila.apilar(Nodo(lista[0]))
#             print "Terminal: |", lista[0],"| ", lista[1:]
        
#         return convertir(lista[1:],pila)


def apilarNuevo(lista,pila2):
   
    if lista != []:
        if lista[-1] in "+-*/=":
            nodo_der = pila2.desapilar()
            nodo_izq = pila2.desapilar()
          
            pila2.apilar(Nodo(lista[-1],nodo_izq,nodo_der))
        else:
            pila2.apilar(Nodo(lista[-1]))
        return apilarNuevo(lista[:-1],pila2)
        


def evaluar(arbol):

    if arbol.valor == "=":
        return evaluar(arbol.izq) 

    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    #print "este es el valor",int(arbol.valor)
    return int(arbol.valor)


exp = raw_input("ingrese l expresion en posfija: ").split(" ")

exprev=exp.reverse()

pila = Pila()
pila2=Pila()
#print "Esta es la pila:",pila.items



convertir(exp, pila2)
apilarNuevo(exp,pila2)

print "X es: ",evaluar(pila2.desapilar())


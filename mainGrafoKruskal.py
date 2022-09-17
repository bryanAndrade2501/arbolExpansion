from Grafo import Grafo

g = Grafo()

valores = ["a","b","c","d","e","f","g","h","i"]
for x in valores:
    g.agregarVertices(x)


g.agregarAristaNoDirigida("a","b",6)
g.agregarAristaNoDirigida("a","g",8)
g.agregarAristaNoDirigida("a","d",10)
g.agregarAristaNoDirigida("b","e",15)
g.agregarAristaNoDirigida("b","h",13)
g.agregarAristaNoDirigida("b","c",11)
g.agregarAristaNoDirigida("c","h",3)
g.agregarAristaNoDirigida("h","g",5)
g.agregarAristaNoDirigida("h","i",7)
g.agregarAristaNoDirigida("i","g",5)
g.agregarAristaNoDirigida("i","f",6)
g.agregarAristaNoDirigida("f","g",4)
g.agregarAristaNoDirigida("f","e",2)
g.agregarAristaNoDirigida("d","e",6)



#matriz = g.matrizCostos()
#for v in matriz:
#    print(f'{v}')

#print(g.devolverAristas())
#print(sorted(g.devolverAristas()))

print(g.kruskal())


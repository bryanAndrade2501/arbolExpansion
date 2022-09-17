from Grafo import Grafo

g = Grafo()

valores = ["1","2","3","4","5","6"]
for x in valores:
    g.agregarVertices(x)


g.agregarAristaNoDirigida("1","2",4)
g.agregarAristaNoDirigida("1","5",3)
g.agregarAristaNoDirigida("1","3",2)
g.agregarAristaNoDirigida("3","5",6)
g.agregarAristaNoDirigida("3","4",1)
g.agregarAristaNoDirigida("3","6",3)
g.agregarAristaNoDirigida("6","5",2)
g.agregarAristaNoDirigida("6","4",6)
g.agregarAristaNoDirigida("2","4",5)



matriz = g.matrizCostos()
print("   1, 2, 3, 4, 5, 6 ")
count = 1
for v in matriz:
    print(f'{count} {v}')
    count +=1
    
print(g.prim("5"))



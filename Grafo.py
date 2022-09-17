class nodo:
    def __init__(self,valor):
        self.id = valor #valor almacenado del nodo
        self.conexiones = {} # diccionario para almacenar conexiones(llave) y pesos
        self.grupo = 0 #kruskal

    def agregarVecino(self, id, peso):
        if id not in self.conexiones: # revisa que el vecino no exista en las conexiones
            self.conexiones[id] = peso 

    
class Grafo:

    def __init__(self):
        self.nodos={} #diccionario para que la llave sea el identificador 

    def agregarVertices(self, vertice):
        if vertice not in self.nodos:
            nuevoNodo = nodo(vertice)
            self.nodos[vertice] = nuevoNodo
            self.nodos[vertice].grupo = len(self.nodos) #cada nodo pertenesera a un grupo diferente (conjuntos disjuntos)
        
    def agregarAristaNoDirigida(self,inicio,fin,peso): 
        if inicio in self.nodos and fin in self.nodos:
            self.nodos[inicio].agregarVecino(fin,peso)
            self.nodos[fin].agregarVecino(inicio,peso)


    def matrizCostos(self):
        matriz = [] 
        filas = []
        inf = 9999
        if len(self.nodos) != 0: #verificar que el grafo  no esta vacio
            for v in self.nodos:
                for x in self.nodos:
                    if self.nodos[x].id in self.nodos[v].conexiones:
                        filas.append(self.nodos[v].conexiones[x])
                    else:
                        filas.append(inf)
                matriz.append(filas)
                filas=[]
        return matriz
    

    def posicion(self,id): #retorna la posicion de un nodo en la lista del grafo
        if id in self.nodos:
            count = 0
            for v in self.nodos:
                if id == self.nodos[v].id:
                    return count
                count += 1   
    
    def devuelveNodo(self,posicion): #segun la posicion retorna el identificador del grafo
        if posicion < len(self.nodos):
            count=0
            for v in self.nodos:
                if posicion == count:
                    return self.nodos[v].id
                count +=1

    def prim(self,NodoInicio):
        w = self.matrizCostos()
        n = len(self.nodos)
        s = self.posicion(NodoInicio)
        v=[] #almacenar nodos visitados o no (0 y 1)
        while (len(v) != n):
            v.append(0)
        v[s]=1
        E=[] #almacena aristas del arbol
        for i in range(0,n-1):
            minimo = 9999
            agregar_vertice=0 #almacena la posicion del nodo
            e = [] #arista
            for j in range (0,n): #itera filas
                if (v[j]==1):
                    for k in range(0,n): #itera columnas
                        if(v[k]==0 and w[j][k] < minimo):
                            agregar_vertice = k
                            e = [self.devuelveNodo(j),self.devuelveNodo(k)]
                            minimo = w[j][k]
            v[agregar_vertice]=1
            E.append(e)
        return E
    
    def kruskal(self):
        matriz = self.matrizCostos()
        n = len(self.nodos)
        min = 9999
        Jfinal = 0
        Kfinal = 0
        E=[]
        arista=[]

        for i in range (0,n+1):
            for j in range(0,n):
                for k in range (0,n):
                    if matriz[j][k] < min:
                        min = matriz[j][k]
                        arista= [self.devuelveNodo(j),self.devuelveNodo(k)]
                        #print(arista)
                        Jfinal = j
                        Kfinal = k
            #arista= [self.devuelveNodo(Jfinal),self.devuelveNodo(Kfinal)]
            if self.nodos[self.devuelveNodo(Jfinal)].grupo != self.nodos[self.devuelveNodo(Kfinal)].grupo:

                auxiliar = self.nodos[self.devuelveNodo(Jfinal)].grupo
                self.nodos[self.devuelveNodo(Jfinal)].grupo = self.nodos[self.devuelveNodo(Kfinal)].grupo

                for x in self.nodos:
                    if self.nodos[x].grupo == auxiliar:
                        self.nodos[x].grupo = self.nodos[self.devuelveNodo(Kfinal)].grupo
                
                matriz[Jfinal][Kfinal] = 9999
                matriz[Kfinal][Jfinal] = 9999

                min = 9999
                E.append(arista)

            else:

                matriz[Jfinal][Kfinal] = 9999
                matriz[Kfinal][Jfinal] = 9999
            
            print(f"\tciclo {i}")
            for t in self.nodos:
                print(f'{t} --> {self.nodos[t].grupo}')

            min = 9999
            arista=[]
        return E














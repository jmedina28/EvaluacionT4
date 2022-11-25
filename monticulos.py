class MonticuloMinimo():

    def __init__(self):
        self.vector, self.nelementos = [], 0

    def monticulo_nelementos(self):
        return self.nelementos        

    def monticulo_vacio(self):
        return self.nelementos == 0

    def monticulo_lleno(self):
        return self.nelementos == len(self.vector)

    def buscar(self, busqueda):
        
        for index, value in enumerate(self.vector):
            if value[0][0].informacion == busqueda:
                resultado = index
                return  resultado

    def aniadir(self, dato, prioridad=3):
        
        self.vector.append([dato, prioridad])
        self.flotar(self.nelementos)
        self.nelementos += 1

    def flotar(self, indice):
        
        padre = (indice -1) // 2
        while(indice > 0 and self.vector[indice][1] < self.vector[padre][1]):
            self.vector[indice], self.vector[padre] = self.vector[padre], self.vector[indice]
            indice = padre
            padre = (indice -1) // 2
    
    def hundir(self, indice = 0):
        
        h_izq = (indice * 2) + 1
        control = True
        while(control and h_izq < self.nelementos):
            mayor = h_izq
            h_der = h_izq + 1
            if h_der < self.nelementos:
                if self.vector[h_der][1] < self.vector[h_izq][1]:
                    mayor = h_der
            
            if self.vector[indice][1] > self.vector[mayor][1]:
                self.vector[indice], self.vector[mayor] = self.vector[mayor], self.vector[indice]
                indice = mayor
                h_izq = (indice * 2) + 1
            else:
                control = False

    def quitar(self, heapsort=False):
        
        x, prioridad = self.vector[0][0], self.vector[0][1]
        self.vector[0], self.vector[self.nelementos-1] = self.vector[self.nelementos-1], self.vector[0]
        self.nelementos -= 1
        self.hundir()
        if not heapsort:
            self.vector.pop()
        return x, prioridad

    def arribo(self, dato, prioridad):
        self.aniadir(dato, prioridad)
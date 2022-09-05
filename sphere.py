from collection import namedtuple

Vetor =namedtuple("Vetor", ['x', 'y', 'z'])

class Sphere:
    """
    Implemente a classe Sphere que possui os atributos
    x = corresponde a posição no eixo x
    y = corresponde a posição no eixo y
    z = corresponde a posição no eixo z
    
    r = raio da esfera (metros)
    m = massa da esfera em Kg
    v = corresponde a tupla do vetor de força (x,y,z) em Newton
    """
    
    def __init__(self, x=0, y=0, z=0, r=0.1, m=1, v=(10,0,0):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.m = m
        self.v = v
        
bola = Sphere()
bola.v.x

    """
    Implemente a lógica para que você
    possa lançar uma esfera submetida a um vetor de força
    
    Considere a gravidade constante 10m/s²
    """    
    if __name__ == '__main__':
        main()

    

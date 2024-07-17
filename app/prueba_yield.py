def prueba_yield():
    a = 1
    yield a
    a * 2
    yield a
    print(a)

def contador(palabra): return len(palabra.split())
print(contador("hola como estas"))
import random 

# random entre 1 25
# random entre 1 15
def numero_ancho():
    return random.randint(1, 15)

def numero_alto():
    return random.randint(1, 25)

# objetos aleatorios
objetos_random = [
    [numero_ancho(), numero_alto()],
    [numero_ancho(), numero_alto()],
    [numero_ancho(), numero_alto()],
    [numero_ancho(), numero_alto()],
]


# Bonus
Bonus_random = [
    [numero_ancho(), numero_alto()],
    [numero_ancho(), numero_alto()],
    [numero_ancho(), numero_alto()],
    [numero_ancho(), numero_alto()],
]
 
  
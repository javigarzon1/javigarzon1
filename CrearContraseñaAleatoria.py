import random
#crear una funcion que nos devuelva contraseñas aleatorias de 8 caracteres
def crear_contraseña_aleatoria(num):
    chars = "abcdefghijhklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num + 11
    c2 = num
    c3 = num - 2
    c4 = num + 5
    c5 = num + 32
    c6 = num + 8
    c7 = num - 13
    c8 = num + 3

    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{chars[c5]}{chars[c6]}{chars[c7]}{chars[c8]}{num*2}"
    return contraseña,num
aleatorio = random.randint(0, 9)

password,primer_numero = crear_contraseña_aleatoria(aleatorio)

#mostrando los resultados obtenidos y el numero usado para crearla
print(f"Tu contraseña nueva de 8 caracteres es: {password}")
print(f"El nùmero utilizado para crear la contraseña fue: {aleatorio}")




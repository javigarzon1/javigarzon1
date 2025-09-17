animales = ["perro", "gato", "hiena", "tigre", "elefante", "mono", "gallina", "oveja"]
unidades = [2, 5, 8, 10, 12, 15, 20, 7]  # misma cantidad que animales

# recorrer usando índice con range
for i in range(len(animales)):
    animal = animales[i]
    cantidad = unidades[i]

    # saltar si cantidad es 8
    if cantidad == 8:  
        print("Saltando porque la cantidad es 8")
        continue  # pasa al siguiente animal

    print(f'Mi animal es: {animal}')
    print(f'Y tengo {cantidad} {animal}s')

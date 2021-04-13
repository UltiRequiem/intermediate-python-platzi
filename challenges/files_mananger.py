def read():
    names = []
    with open("./../txt/name.txt", "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0:
                names.append(line.strip())
    if len(names) > 0:
        print(names)
    else:
        print("Archivo vacio")


def write():
    names = []
    with open("./../txt/name.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')


def agregar_nombre(nombre):
    with open("./../txt/name.txt", "a", encoding="utf-8") as f:
        f.write(nombre)
        f.write("\n")


def borrar_nombre(nombre):
    names = []
    with open("./../txt/name.txt", "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0 and line.strip() != nombre:
                names.append(line.strip())
    with open("./../txt/name.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    menu = """  
        ----------------------------------------------------------------------
        Seleccione un numero:
        1. Crear un nuevo archivo
        2. Agregar nombre
        3. Listar nombre
        4. Borrar nombre
        5. Salir del programa
        ----------------------------------------------------------------------
        """
    while True:
        try:
            print(menu)
            n = int(input("Ingrese una opción: "))
            if n == 1:
                write()
            elif n == 2:
                nombre = input("Ingrese el nombre a agregar: ")
                agregar_nombre(nombre)
            elif n == 3:
                read()
            elif n == 4:
                nombre = input("Ingrese el nombre a borrar: ")
                borrar_nombre(nombre)
            elif n == 5:
                exit()
        except ValueError:
            print("Error seleccione una opción correcta.")

if __name__ == '__main__':
    run()

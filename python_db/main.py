from connect import get_connection


def show_table():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profesores")
        profesores = cursor.fetchall()
        if not profesores:
            print("No hay profesores en la base de datos")
        for profe in profesores:
            print(profe)
        print("------------------------------------- Total: " + str(len(profesores)))
    finally:
        conn.close()


def insert_teacher():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        name = input("Dame el nombre del profe: ")
        cursor.execute("INSERT INTO profesores (name) VALUES (%s)", (name,))
        conn.commit()
    finally:
        conn.close()


def menu():
    print(" ==== Menu ==== ")
    print("1. Mostrar la lista de profesores")
    print("2. Insertar un profesor")
    print("3. Salir")

    option = input("Selecciona una opcion: ")
    if option == "1":
        show_table()
    elif option == "2":
        insert_teacher()
    elif option == "3":
        exit()
    else:
        print("Opcion no valida")


if __name__ == "__main__":
    while True:
        menu()

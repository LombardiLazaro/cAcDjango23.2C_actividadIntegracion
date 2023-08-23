#-5
def get_int_iterativo():
    while True:
        try:
            valor = int(input("(I)Ingrese un número entero: "))
            return valor
        except ValueError:
            print("(I)Lo ingresado no es válido.")

def get_int_recursivo():
    try:
        valor = int(input("(R)Ingrese un número entero: "))
        return valor
    except ValueError:
        print("(R)Lo ingresado no es válido.")
        return get_int_recursivo()

num_ite = get_int_iterativo()
num_recur = get_int_recursivo()
print("(I)El número entero ingresado es el:", num_ite)
print("(R)El número entero ingresado es el:", num_recur)


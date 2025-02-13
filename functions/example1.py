def construye(fname, lname):
    fname = fname.capitalize()
    lname = lname.capitalize()
    return fname + " " + lname

completo = construye("daniel", "bahena")

print(completo)

def suma(x, y):
    total = x + y
    return total

print(suma(2,4))

def resta(x, y):
    total = x - y
    return total

print(resta(9,5))

def div(x, y):
    total = x / y
    return total

print(div(234,23))

def mult(x, y):
    total = x * y
    return total

print(mult(23,98))

def cancion(name, age):
    print(f"estas son las mañanitas, para {name}")
    print("Y antes las cantaba al rey david")
    print(f"pero como ahora cumples {age} años, pues ya no porque estás viejo")
    print()

cancion("chucho", 40)

def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"You have an amount pending of ${amount} which is due on {due_date}")

display_invoice("Daniel",1001.01,"01/25")
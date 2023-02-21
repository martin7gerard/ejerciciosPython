# Por Martin Gerardo Casillas Sánchez
# 1 Preguntar los elementos de 2 conjuntos
datos = input("Dame los elementos del conjunto A separados por comas: ") # 1,2,3,4,5,6
lista = datos.split(",") # Split -> Separar
conjuntoA = set(lista) # creamos el conjunto set()

datos2 = input("Dame los elementos del conjunto B separados por comas: ") # 1,2,3,4,5,6
lista2 = datos2.split(",") # Split -> Separar
conjuntoB = set(lista2) # creamos el conjunto set()

# 2 Mostrar relaciones de igualdad
if conjuntoA == conjuntoB: # condicion
  print("Los conjuntos A y B son iguales")
else:
  print("Los conjuntos A y B NO son iguales")

# 3 Relación de subconjuntos
if conjuntoA.issubset(conjuntoB):
  print("El conjunto A es subconjunto de B")

if conjuntoB.issubset(conjuntoA):
  print("El conjunto B es subconjunto de A")

# 4 Realizar las operaciones (AUB) (AnB) (A-B) (B-A)
print("La operación AUB =", (conjuntoA | conjuntoB))
print("La operacion AnB =", (conjuntoA & conjuntoB))
print("La operacion A-B =", (conjuntoA - conjuntoB))
print("La operacion B-A =", (conjuntoB - conjuntoA))

# 5 Preguntar elemento y buscar pertenencia en conjuntos
elemento = input("Dame un elemento y lo busco en los conjuntos: ")

if elemento in conjuntoA:
  print("El elemento", elemento, "se encuentra dentro del conjunto A")

if elemento in conjuntoB:
  print("El elemento", elemento, "se encuentra dentro del conjunto B")

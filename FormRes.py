from math import sqrt

a = float(input("Argumento a: "))
b = float(input("Argumento b: "))
c = float(input("Argumento c: "))


delta = b ** 2 - 4 * a * c

if delta == 0:
    x = (-b) / (2 * a)
    print('x = {0}'.format(x))
elif delta < 0:
    print('Não existe uma raiz real.')
else:
    x_1 = ((-b) + sqrt(delta)) / (2 * a)
    x_2 = ((-b) - sqrt(delta)) / (2 * a)
    print(("x = %s ou x = %s") % (x_1, x_2))

input("Aperta 'enter' para sair.")

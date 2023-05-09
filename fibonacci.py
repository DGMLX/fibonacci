a=0
b=1
c=0
contador=0
print(0)
while contador < 3:
    c = a + b
    b = c + a
    a = b + c
    print(f"{c} - {b} - {a}")
    contador = contador +1
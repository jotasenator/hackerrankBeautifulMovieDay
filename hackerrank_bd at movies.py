
lista_numeros=[20,21,22,23]

print(lista_numeros)

lista=[]
for n in lista_numeros:

    residuo=n%10
    revertir=0
    while n > 0:
            residuo = n% 10
            revertir = (revertir * 10) + residuo
            n //= 10
    lista.append(revertir)
contador=0
for i,j in zip(lista_numeros,lista):
    if (i-j)%6==0:
        contador+=1

print(lista)
print(contador)


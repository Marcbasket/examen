n=input('Dame el numero de linea que desees.')
lista = [[1],[1,1]]
for i in range(1,n):
    linea=[1]
    for j in range(0,len(lista[i])-1):
        linea.extend([lista[i][j]+lista[i][j+1]])
    linea+=[1]
    lista.append(linea)
print lista[n]

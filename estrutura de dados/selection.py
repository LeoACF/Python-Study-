#selection sort
#encontra o menor valor em um array e o coloca na base do array

my_array = [12,4,7,1,0,9]

print(my_array)
n = len(my_array)
for i in range(n-1):
    minimo_index = i
    for j in range(i+1,n):
        if my_array[j] < my_array[minimo_index]:
            minimo_index = j
    menor_valor = my_array.pop(minimo_index)
    my_array.insert(i, menor_valor)
    
print(my_array)
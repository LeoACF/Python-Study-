#um bubblesort
my_array = [12,9,15,7,13]
print(my_array)

n = len(my_array)
for i in range(n-1):
    trocado = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j+1], my_array[j] = my_array[j], my_array[j+1]
            trocado = True
print(my_array)

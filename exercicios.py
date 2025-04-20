#1-palindromo:
a = input("insert a word")

def isPalindromo(a):
    contrario = a[::-1]
    if contrario == a:
        print(a + " é palindromo")
    else:
        print("não é")
        
isPalindromo(a)

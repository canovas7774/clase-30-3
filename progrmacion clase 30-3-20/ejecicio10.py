n = int(input("pone un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " son primo")
else: 
    print(str(n) + " no son primos")
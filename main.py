import math
n,k= input().split(" ")
n = int(n)
k = int(k)

if n == 0 or k == 0 or k > n :
  print(1)
else: 
  silniaN = math.factorial(n)
  silniaK = math.factorial(k)
  silniaNK = math.factorial(n-k)
  wynik = silniaN//(silniaK * silniaNK)
  print(wynik)  
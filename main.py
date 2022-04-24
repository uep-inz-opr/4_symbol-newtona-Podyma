import math
dane = input()
n = int(dane[0])
k = int(dane[2])

if n == 0 or k == 0 or k > n :
  print(1)
else: 
  silniaN = math.factorial(n)
  silniaK = math.factorial(k)
  silniaNK = math.factorial(n-k)
  wynik = silniaN//(silniaK * silniaNK)
  print(wynik)  
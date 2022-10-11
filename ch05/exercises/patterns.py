n = int(input("Enter a number: "))

def star_pyramid(n):
  for i in range(0, n):
    for j in range(0, i+1):
      print("* ", end = "")
    print("\n")
star_pyramid(5)

def rstar_pyramid(n):
  for i in range(n, 0, -1):  
    for j in range(0, i):  
      print("* ", end = "")  
    print("\n")
rstar_pyramid(5)
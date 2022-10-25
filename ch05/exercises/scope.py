def multiply(x, y):
  result = 0
  for i in range(x):
    result += y
  return result
x = multiply(5, 6)
print(x)

def exponent(x, y):
  result = 1
  x = 2
  y = 3
  for i in range(y):
    result *= x
  return result
x = exponent(2, 3)
print(x)

def root(x):
  for i in range(x):
    if (i * i == x):
      return i
  else:
    return -1
x = root(16)
print(x)
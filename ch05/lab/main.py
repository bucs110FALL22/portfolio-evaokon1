def np1(n):
  while n != 1:
    count = 1
    print(n)
    if n % 2 == 0:
      n = n // 2
      count += 1
    else:
      n = n * 3 + 1
      count += 1
  print(n)
  print(count, "times")
np1(3)

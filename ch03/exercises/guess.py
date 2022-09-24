import random
num = random.randint(1, 10)
for i in range(3):
  guess = int(input("Enter a number: "))
  if guess == num:
    print("Correct")
  if guess < num:
    print("Too low")
  if guess > num:
    print("Too high")
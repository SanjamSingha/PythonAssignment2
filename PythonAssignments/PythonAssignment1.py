#Exercise 1: Cube Number Test  
#Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
for value in range (0,11):
    cube=value**3
    if cube<=1000:
        print(cube)
    else:
        break

#Exercise 2: Get first prime numbers up to 100
def is_prime(num):
    if num < 2:
        return False
    for value in range(2, int(num**0.5) + 1):
        if num % value == 0:
            return False
    return True
for number in range(2, 101):
    if is_prime(number):
        print(number)

#Exercise Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
Age=input("How old are you?")
Age=int(Age)
if Age<18:
    print("Kids")
elif Age<=18 and Age>=65:
    print("Adults")
else:
    print("Seniors")

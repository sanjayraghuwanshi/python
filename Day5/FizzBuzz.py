#Day5

# Code to print Fizz Buzz in place of numbers when :
#  i % 3 == 0 ; print Fizz 
#  i % 5 == 0 ; print Buzz  
#  i % 3 == 0 and i % 5 == 0 ; print FizBuzz
# https://en.wikipedia.org/wiki/Fizz_buzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
            print("Buzz")
    else:
        print(i)

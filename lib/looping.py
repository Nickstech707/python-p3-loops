#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i in range(10, 0, -1):
        print(i)
        i -= 1
    print("Happy New Year!")

happy_new_year()    

def square_integers(int_list):
    return [int(i ** 2) for i in int_list]

square_integers( [1, 2, 3, 4, 5] )

def fizzbuzz():
   for i in range(1, 101):
       if i % 15 == 0: print("FizzBuzz")
       elif i % 3 == 0: print("Fizz")
       elif i % 5 == 0: print("Buzz")
       else: print(i)

fizzbuzz()



# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# player_heights = [h * 7920 for h in player_heights]

# print(player_heights)
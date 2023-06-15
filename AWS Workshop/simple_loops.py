# Iterate items in list
# Make a counter

import time

numbers = [1,2,3]
numbers.reverse()

for number in numbers:
    print(number)
    time.sleep(1)
print('Liftoff!')

for i in range(101): # prints numbers 0 through 100
    print(i)
print()
    
for i in range(1,101): # prints numbers 1 through 100
    print(i)
# To increment by different value

for number in range(2,101,2): # Prints even number through 100
    print(number)


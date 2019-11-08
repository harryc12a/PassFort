# Code to find the first Fibonacci Number with 1001 digits
F1 = 1
F2 = 1
# First two Fibonacci Numbers
F3 = 2
# F3 Represents the next Fibonacci Number after F1 and F2
while F3 < 10**1000:
    # The first Fibonacci Number with more than 1000 digits must have 1001 digits. First smallest number with 1001
    # is 10^1000. So we go until we reach this point
    F3 = F1 + F2
    # Next Fibonacci Number is the sum of the previous 2
    F1 = F2
    F2 = F3
    # Here we have just labelled

print('The first Fibonacci Number with 1001 digits is: \n%d' % F3)

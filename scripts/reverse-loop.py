#!/usr/bin/python3
def reverse_for_loop(s):
    sl = ''
    for c in s:
        sl = c + sl 
    return sl

input_str = 'ABcDEf'

if __name__ == "__main__":
    print ('Reverse string using for loop =', reverse_for_loop(input_str))

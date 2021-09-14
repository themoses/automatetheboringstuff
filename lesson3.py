#!/usr/bin/env python3

print('What is your name?')

name = input()

print(f'Hi {name}')
print('How old are you?')

age = input()

print('you will be {:s} soon'.format(str(int(age) + 1)))

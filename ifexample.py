#!/usr/bin/env python3

from getpass import getpass

print('Enter password')
password = getpass()

if password == 'swordfish':
  print('Access granted')
elif password == 'admin':
  print('Nice try')
elif password == '':
  print('Please enter a password') 
else:
  print('Access denied')

print('done')

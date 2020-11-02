# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:03:30 2020

@author: vites
"""

def map():
    import pyperclip
    import webbrowser
    address = input('Enter street address: ')
    address = str(address)
    webbrowser.open('www.google.com/maps/dir//'+str(address))

def earth():
    import webbrowser
    location=input('enter address: ').split()
    webloc='+'.join(location)
    print(webloc)
    webbrowser.open('https://earth.google.com/web/search/'+str(webloc))
    
for i in range(1,10000):
    print('\n'+'LOCATE'.center(20,'-'))
    
    option = input('1. Earth, 2. Maps:  ')
    _maps = ['Maps', 'Map', 'maps', 'map', '2', 'm', 'M']
    _earth = ['Earth', 'earth', '1', 'e', 'E']
    _end = ['end', 'clear', 'off', 'exit', 'break']
    
    if option in _maps:
        map()
        
    elif option in _earth:
        earth()
        
    elif option in _end:
        print('goodbye :(')
        break
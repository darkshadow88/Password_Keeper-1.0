# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:16:09 2018

@author: Darkshadow
"""

'''pw.py a insequre password keeper
#its a simple password keeper,hope yoy like it! plug and play! :)
# this is the dictionary that stores passwords'''

PASSWORDS={'gmail':'icaneat',
           'blog':'1235po',
           'facemash':'oikianu89'}

'''import the sys or system module to intract with system
 sys.argv[0]=file name and sus.argv[1]=account name'''
import sys
if len(sys.argv)<2:
    print('Usage: python pw.py[account]-copy account password')#error messege
    sys.exit()
account=sys.argv[1]

'''import the pyperclip module to copy the password to clipboard'''
import pyperclip
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])#password is copied
    print('Password for '+account+' copied to clipboard')
else:
    print('There is no account name account'+account)#error messege
    
    
'''you can code it. or just copy and paste the code,uddate the PASSWORD Dictionary'''
'''then open note pad'''
'''copy this code'''
'''@py.exe C:\Python34\pw.py %*
    @pause
    
save it as pw.bat'''
'''open WIN+R then type pw <account>'''
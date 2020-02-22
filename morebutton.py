import os
from time import sleep
a = '\x1b[92m'                                                         
b = '\x1b[91m'                                                         
c = '\x1b[0m'
os.system('clear')
print (a + '\t  More Button for Termux ')
print (a + '\t  UP,Down,right,Left, CTRL ')                            
print ('\t web : writersantuy.blogspot.com')                             
print ('\t Facebook : fb.me/s1s4ntuy')
print ('\t Github : https://github.com/writersantuy')
print (a + ('+' * 40))
print ('\nPlease Wait..')                                                
sleep(1)                                                               
print (b + '\n[!] Get File Default Termux')
sleep(1)                                                               
try:
    os.mkdir('/data/data/com.termux/files/home/.termux')               
except:                                                                    
              pass

print (a + '[!]Success !')                           
sleep(1)
print (b + '\n[!] Added More Button..')                        
sleep(1)
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
santuy = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
santuy.write(key)
santuy.close()
sleep(1)
print (a + '[!] Processing..  !')
sleep(1)
print (b + '\n[!] Please Wait..')
sleep(2)
os.system('termux-reload-settings')
print (a + '[!] Done !!' + c + '\n\nCall me : +62895361164306 or from my Web\n\n')
sleep(2)
os.system('clear')
os.system('login')
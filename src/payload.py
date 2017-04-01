import os
from cripto import crihos
from cripto import pacript

if os.path.exists(pacript):    
    file = open(pacript+crihos, 'a')    
    file.write('127.0.0.1 vk.com')
    file.close() 

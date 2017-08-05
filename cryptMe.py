from cryptography.fernet import Fernet
import sys
import pyscrypt
import getpass
#-----------------------
#This method will will parse command line arguments
#----------------------- 
list_of_args = ['-h','-e', '-d','-g']

def parse_args():
    
#     list_of_args = ['-h','-e', '-d','-g']
    
    if len(sys.argv)==1:
        print(
'''Usage: cryptMe.py -e [encrypt message], -d [decrypt message]
                -e, will start script and encrypt message
                -d, will start script and decrypt message
                -g, generate secret key
              ''')
    if len(sys.argv)>1:
        if sys.argv[1]==list_of_args[0]:
            print(
'''Usage: cryptMe.py -e [encrypt message], -d [decrypt message]'
                -e, will start script and encrypt message
                -d, will start script and decrypt message
                -g, generate secret key
''')
        
        if sys.argv[1]==list_of_args[1]:
            encrypt()
        if sys.argv[1]==list_of_args[2]:
            decrypt()
        if sys.argv[1]==list_of_args[3]:
            generate_sec_key()
            
            
        if sys.argv[1] != '-e' and sys.argv[1] != '-d' and sys.argv[1] != '-g' and sys.argv[1] != '-h':
            print(
'''Wrong command line argument 
             
    Usage: cryptMe.py -e [encrypt message], -d [decrypt message]
                -e, will start script and encrypt message
                -d, will start script and decrypt message
                -g, generate secret key
''')
            
#-----------------------
#This method will generate secret key
#-----------------------    

def generate_sec_key():  
                                       
#     key = Fernet.generate_key()                            #generate key using Fernet class         
    password = getpass.getpass()                                    
    hashed = pyscrypt.hash(password = userMesgToBytes(password), 
                       salt = b"seasalt", 
                       N = 1024, 
                       r = 1, 
                       p = 1, 
                       dkLen = 32) 
    if len(sys.argv)>1:
        if sys.argv[1]==list_of_args[3]:
            print(str(hashed)[2:-1])
    return(str(hashed)[2:-1])
#     print(str(key)[2:-1])


#-----------------------
#This method will decrypt message and print it as IJpOVKXqM4HbRY-quFzi....
#-----------------------


def encrypt():
#     print('Please set the path to key file : ')
    
#-------------------
#Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.
#Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.
#Fernet also has support for implementing key rotation via MultiFernet.
#-------------------

#     path = input()                                         #user input for path to key               
#     file = open(path,'r',encoding='utf-8')                 #open file with your key
#     key = file.read()                                      #read file 
    f = Fernet(generate_sec_key())                                        #use fernet     
                                         
    print('Your message :')
    
    token = f.encrypt(userMesgToBytes(input()))            #encrypt message  
    
    print('Your message have been encrypted : \n')
    print(str(token)[2:-1],'\n')                                #delete first two and last symbols(b'.....')
    

#-----------------------
#This method will decrypt message and print it as text that your friend sended to you
#-----------------------

def decrypt():
#     print('Please set the path to friend key file : ')
#     
#     path = input()                                         #user input for path to friend key
#     file = open(path,'r',encoding='utf-8')                 #open file with friend key
#     friend_key = file.read()                               #read file
    f = Fernet(generate_sec_key())                                 #use fernet
    
    print('Please insert message of your friend below :')

    decrypted_token = f.decrypt(userMesgToBytes(input()))  #decrypt message
    converted_to_unicode = decrypted_token.decode("utf-8") #decode kirilic symbols
    
    print('\n',converted_to_unicode)
    
#-----------------------
#This method will convert string to bytes
#-----------------------
    
def userMesgToBytes(user_message):
    convert = bytes(user_message, 'utf-8')                 #convert string to bytes
    
    return convert
# 
# def decodeToBase64(value):
#     
#     return base64.b64decode(value)

def Main():
    parse_args()                                          #parse arguments from command line 
    
if __name__=='__main__':
    Main()








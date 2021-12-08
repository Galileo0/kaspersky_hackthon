# kaspersky 
# Author: Ahmed Zakaria Mohamed
# Bio Protected Image
# User module
import socket
import bpi
import numpy as np
import pickle

print('''
    This is Owner module 
        script v2
''')

l_port = 43470
r_port = 43471
t_port = 43472
tx_port = 43473

bpi_obj = bpi.bio_protected_image() #object

def lithen():
    s = socket.socket() 
    s.bind(('127.0.0.1', l_port))
    s.listen(5) # put the socket into listen mode
    while True:

        c, addr = s.accept()

        data = c.recv(1024).decode("utf-8") # This data is received from the client script
        print('ip: ',addr[0],' need access on Image: ',data)
        c.close()
        print('[Y] , [N]')
        op = str(input('-> '))
        if op == 'Y' or op =='y':
            send(b'Y')
            cp = rec_corrupted_px()
            dec_image = bpi_obj.decrypt_api(cp)
            #print(dec_image)
            send_image(dec_image)
        else:
            send(b'N')
        
def send_image(data):
    #corrupted_image = pickle.dumps(data)
    uncorrupted_image = str(data)
    uncorrupted_image = uncorrupted_image.encode()
    s = socket.socket()
    s.connect(('127.0.0.1', tx_port)) 
    s.send(uncorrupted_image)
    s.close()
    print('unCorrupted Pixel sent to reciver')

def rec_corrupted_px():
    s = socket.socket() 
    s.bind(('127.0.0.1', t_port))
    s.listen(5) # put the socket into listen mode
    data = ''
    while True:

        c, addr = s.accept()
        print('Reciving Data.....')
        #data = c.recv(1024).decode("utf-8") # This data is received from the client script
        while True:
            part = c.recv(4096)
            part = part.decode('utf-8')
            #print(part)
            data += part
            if not part: 
                break
            
        #data = data.decode('utf-8') 
        data = eval(data)
        print('data Recived.')
        #print(np.frombuffer(data))
        return data
        
    


def send(data):
    s = socket.socket()
    s.connect(('127.0.0.1', r_port)) 
    s.send(data)
    s.close()

def cap():
    
    image = bpi_obj.capture_image()
    #print(image)
    bpi_obj.view_image(image)
    bpi_obj.load_image(image)
    bpi_obj.protect_image()
    

def main():
    while True:
        print('''
        Select Operation
        1- Capture
        2- Lithen
        0- Exit''')

        selected_option = input ('-> ')
        if selected_option == '1':
            cap()
        elif selected_option == '2':
            lithen()
        elif selected_option == '0':
            break
        else:
            print('Wrong Option')


#script exe
main()










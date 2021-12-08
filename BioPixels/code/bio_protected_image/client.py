# Author: Ahmed Zakaria Mohamed
# Bio Protected Image
# User module
import socket
import os
import glob
import bpi
import numpy as np
import pickle

print('''
    This is client module 
        script v2
''')


import socket

s = socket.socket()
l_port = 43471          
r_port = 43470 # Use the same port number here as you did in the server script.
t_port = 43472
tx_port = 43473

def lithen():
    s = socket.socket() 
    s.bind(('127.0.0.1', l_port))
    s.listen(5) # put the socket into listen mode
    while True:

        c, addr = s.accept()

        data = c.recv(1024).decode("utf-8") # This data is received from the client script
        #print(data)
        c.close()
        return data

def send(data):
    data = bytes(data,'utf-8')
    s = socket.socket()
    s.connect(('127.0.0.1', r_port)) 
    s.send(data)
    s.close()
    


def send_image(data):
    #corrupted_image = pickle.dumps(data)
    corrupted_image = str(data)
    corrupted_image = corrupted_image.encode()
    s = socket.socket()
    s.connect(('127.0.0.1', t_port)) 
    s.send(corrupted_image)
    s.close()
    print('Corrupted Pixel sent')

def access_request(data):
    s = socket.socket()
    s.connect(('127.0.0.1', r_port)) 
    data = bytes(data,'utf-8')
    s.send(data)
    #s.send(b"Message from user")
    s.close()
    rec = lithen()
    if rec == 'Y':
        return True

    else:
        return False

def rec_uncorrupted_px():
    s = socket.socket() 
    s.bind(('127.0.0.1', tx_port))
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

def auth(file_name):
    full_file_name = 'export/'+file_name
    bpi_obj = bpi.bio_protected_image()
    px_list,owner_hash = bpi_obj.read_bpi_api(file_name)
    print('--- Auth ---')
    print('connecting to Image Owner: ',owner_hash)
    if access_request(file_name):
        send_image(px_list)
        print('---- Waiting for uncorupted Image ----')
        image = rec_uncorrupted_px()
        bpi_obj.reshape(image)
    else:
        print('Access Denied1')
    
    

def main():
    print('---- BPI Files -----')
    os.chdir(r'export/')
    myFiles = glob.glob('*.bpi')
    counter = 0
    for f in myFiles:
        file_name = str(counter)+'- '+f
        print(file_name)
        counter += 1 
    
    selected_file = str(input('Image_name: '))
    auth(selected_file)

#exe
main()
    
    

import threading 
import socket
import sys
import time
import keyboard


host = ''
port = 9000
locaddr = (host,port) 


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.1.13', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print('Python Tello Keyboard Controler.')

print('Controls: W: Forward S: Backward A: Fly Left D: Fly Right')
print('Arrow Left: Flip Left   Arrow Right: Flip Right    Up Arrow: Fly Upward    Down Arrow: Fly Downward')
print('T: Takeoff   L: Land   Space: Flip Forward   E: Turn Right   Q: Turn Left')

#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

def sendmsg(msg):
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg,tello_address)

def start():
    sendmsg('command')
def takeoff():
    sendmsg('takeoff')
def land():
    sendmsg('land')
def forward():
    sendmsg('forward 20')
def back():
    sendmsg('back 20')
def up():
    sendmsg('up 20')
def down():
    sendmsg('down 20')
def cw():
    sendmsg('cw 45')
def ccw():
    sendmsg('ccw 45')
def flipf():
    sendmsg('flip f')
#if keyboard.is_pressed('w'):
   #wpressed = true

while True:
    try:

        if keyboard.is_pressed('w'):
            #wpressed = True
            #while wpressed == True:
            print("forward 20")
            forward()
        elif keyboard.is_pressed('s'):
            #spressed = True
            #while spressed == True:
            print('back 20')
            back()
        elif keyboard.is_pressed('up'):
            print('up 20')
            up()
        elif keyboard.is_pressed('down'):
            print('down 20')
            down()
        elif keyboard.is_pressed('right'):
            print('cw 5')
            cw()
        elif keyboard.is_pressed('left'):
            print('ccw 5')
            ccw()
        elif keyboard.is_pressed('t'):
            print('takeoff')
            takeoff()
        elif keyboard.is_pressed('l'):
            print('land')
            land()
        elif keyboard.is_pressed('q'):
            print("flip l")
            start("l")
        elif keyboard.is_pressed('e'):
            print("flip r")
            flipr()
        elif keyboard.is_pressed('spacebar'):
            print("flip f")
            flipf()
        elif keyboard.is_pressed('c'): 
            print('command')
            start()
        
        else:
            pass
    except:
        break



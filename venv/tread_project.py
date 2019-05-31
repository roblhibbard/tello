import tkinter as tk
import threading
import socket
import sys
import time



host = ''
port = 9000
locaddr = (host,port)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.1.18', 8889)

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
def send(message, delay):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))
  time.sleep(delay)

def close(event):
    command.withdraw()
    sys.exit()

def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)

    if key_press == 'c':
        sendmsg('command')
    elif key_press == 't':
        sendmsg('takeoff')
    elif key_press == 'l':
        sendmsg('land')
    elif key_press == 'w':
        sendmsg('forward 25')

    elif key_press == 's':
        sendmsg('back 25')
    elif key_press == 'right':
        sendmsg('cw 25')
    elif key_press == 'left':
        sendmsg('ccw 25')
    elif key_press == 'up':
        sendmsg('up 25')
    elif key_press == 'down':
        sendmsg('down 25')
    elif key_press == 'space':
        sendmsg('flip f')
    elif key_press == 'e':
        sendmsg('flip r')
    elif key_press == 'q':
        sendmsg('flip f')
    elif key_press == 'm':
        send('flip f', 5)
        send('flip r', 5)
        send('flip l', 5)
        send('flip l', 5)
        send('flip r', 5)
        send('forward 50', 5)
        send('flip b', 5)
        send('flip b', 5)

command = tk.Tk()
command.bind_all('<Key>', key_input)
command.bind('<Escape>', close)
command.mainloop()

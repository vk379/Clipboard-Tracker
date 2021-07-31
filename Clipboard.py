import keyboard
import pyautogui as pya
import pyperclip  
import time
import os
from os import path
from time import sleep
from datetime import datetime

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  
    return pyperclip.paste()

now = datetime.now()
current_date = now.strftime("%m/%d/%Y")
realDate = current_date.replace('/','.');
print(realDate);

cwd = os.path.dirname(os.path.abspath("__file__"))
cwd = cwd + "//";
if(path.exists(cwd + realDate + ".txt")): 
    print("Exists");
else: 
    with open(cwd + realDate + ".txt", "w") as f: 
        print("Created")
    f.close();

while True:
    sleep(0.05)
    if keyboard.is_pressed('ctrl+c'):
        now = datetime.now()
        currentTime = now.strftime("%I:%M:%S %p")
        print('Copying the selected')
        sleep(0.1)  
        var = copy_clipboard()
        out = var.replace("\r\n"," ")
        with open(cwd+realDate+".txt", "a+", encoding= 'utf-8') as f: 
            f.write(currentTime + " -------- " + out + '\n'); 
        f.close();
        print(out)
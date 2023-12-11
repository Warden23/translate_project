import tkinter as tk
from tkinter import ttk
import time
import pyautogui
from pynput import keyboard
from PIL import ImageGrab
import cv2 as cv
from googletrans import Translator
import numpy as np
import pytesseract
import pyperclip
import keyboard as kb


script_running = False


class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translate_project")

        
        image = cv.imread('./изображение.png', 1)
        img_gray = cv.cvtColor(np.array(image), cv.COLOR_BGR2GRAY)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        custom_config = r'--oem 3 --psm 6 -l rus+eng'
        initial_text = pytesseract.image_to_string(img_gray, config=custom_config, lang='rus')

        
        self.input_text = tk.Text(root, wrap='word', width=40, height=10)
        self.input_text.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

        
        self.input_text.insert("1.0", initial_text)

        
        self.output_text = tk.Text(root, wrap='word', width=40, height=10, state='disabled')
        self.output_text.grid(row=0, column=2, padx=10, pady=10, rowspan=2)

       
        self.languages = ['русский', 'английский']
        self.language_var = tk.StringVar()
        self.language_var.set(self.languages[1])
        self.language_menu = ttk.Combobox(root, textvariable=self.language_var, values=self.languages, state='readonly')
        self.language_menu.grid(row=0, column=1, padx=10, pady=10)

        
        self.translate_button = ttk.Button(root, text="Перевести", command=self.translate_text)
        self.translate_button.grid(row=1, column=1, pady=10)

       
        self.copy_input_button = ttk.Button(root, text="Copy", command=self.copy_input_text)
        self.copy_input_button.grid(row=2, column=0, pady=10)

        
        self.copy_output_button = ttk.Button(root, text="Copy", command=self.copy_output_text)
        self.copy_output_button.grid(row=2, column=2, pady=10)

        
        self.translate_text()

    def translate_text(self):
        
        text = self.input_text.get("1.0", "end-1c")

        
        translator = Translator()
        target_language = self.language_var.get()

        if target_language == 'русский':
            destination_language = 'ru'
        elif target_language == 'английский':
            destination_language = 'en'
        else:
            destination_language = 'en'

        translation = translator.translate(text, dest=destination_language)

        
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", translation.text)
        self.output_text.config(state='disabled')

    def copy_input_text(self):
        
        self.root.clipboard_clear()
        self.root.clipboard_append(self.input_text.get("1.0", "end-1c"))
        self.root.update()

    def copy_output_text(self):
        
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output_text.get("1.0", "end-1c"))
        self.root.update()



def for_canonical(f):
    return lambda k: f(l.canonical(k))





def take_screenshot():
    global script_running 
    image = ImageGrab.grabclipboard()

    if image:
        image.save("изображение.png")
        pyperclip.copy('')
        print("Изображение успешно сохранено в файл 'изображение.png'")
        if __name__ == "__main__":
            root = tk.Tk()
            app = TranslatorApp(root)
            root.mainloop()
    else:
        print("Не удалось получить изображение из буфера обмена.")
    
    
    script_running = False  


def on_activate():
    pyperclip.copy('')
    # Continue executing the code only if the Alt key is not pressed
    while kb.is_pressed('alt') and kb.is_pressed('r'):
        pass
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('winleft')
    pyautogui.keyDown('s')
    time.sleep(0.2)
    pyautogui.keyUp('s')
    pyautogui.keyUp('winleft')
    pyautogui.keyUp('shiftleft')
    time.sleep(5)
    take_screenshot()

        

hotkey = keyboard.HotKey(keyboard.HotKey.parse('<alt>+r'), on_activate)

with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()

from objects import get_text , translater
import tkinter as tk
from tkinter import filedialog
import os


ob = get_text ()
ob2 = translater (target='fa')

def insert_words(): #enter the word in the docWord_enter Text box 
    docText_entry.insert(tk.END , " ")
    #
    text = docText_entry.get('1.0' , tk.END)
    text = text.split(' ')
    text.pop()
    text = ob.similare_word_deleter(text)
    print (text)
    text = ' '.join(text)
    #print (text)
    docWords_entry.delete(1.0 , tk.END)
    word = ob.remove_extra_character(text)
    #
    if not translate_all.get() :
        with open ('saved_words.txt' , 'r' , encoding='utf-8') as file :
            content = file.read()
            for i in word :
                if i not in content:
                    docWords_entry.insert(tk.END , f"{i}\n")
                else :
                    continue
    else :
        for i in word :
            docWords_entry.insert(tk.END , f"{i}\n")
    docText_entry.delete(1.0 , tk.END)
    docText_entry.insert(tk.END , text)

def translate ():#translate the word of in the docWord_enter Text box
    insert_words()
    os.system('cls')
    text = docWords_entry.get('1.0' , tk.END).split('\n')
    text = ob.similare_word_deleter(text)
    docWords_entry.delete(1.0 , tk.END)
    percent = 0
    for i in text :
        txt_translate = f"{i} = {ob2.translate(i)}\n"
        if not clear_terminal.get():
            os.system('cls')
        if print_translated_word_in_terminal.get():
            print(txt_translate)
        percent += 1
        print (f'{(percent / len(text)) * 100}% is translated')
        docWords_entry.insert(tk.END , txt_translate)

def save (): #save words (it don't save similare words)
    make_list = ob.fix_text_saving(docWords_entry.get('1.0' , tk.END)).split('\n')
    make_list = ob.similare_word_deleter(make_list)
    ob.saving_words(make_list , 'saved_words.txt')


def open_file_dialog(): #  open file explorer and open a text file to show its content in the docWord_enter Text box 
    # باز کردن پنجره‌ی انتخاب فایل
    file_path = filedialog.askopenfilename()
    # نمایش مسیر فایل در تکست باکس اولی
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)
    make_list = ob.fix_text_saving(docWords_entry.get('1.0' , tk.END)).split('\n')
    make_list = ob.similare_word_deleter(make_list)
    ob.saving_words(make_list , file_path)

def set_window_size(root, width_ratio, height_ratio): # this take our monitor siza and make a window with our monitor details 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * width_ratio)
    window_height = int(screen_height * height_ratio)

    root.geometry(f"{window_width}x{window_height}")

def open_saved_words (): # this is a new window for show words we saved 
    def open_file():
        # باز کردن پنجره‌ی انتخاب فایل
        file_path = filedialog.askopenfilename()
        # نمایش مسیر فایل در تکست باکس اولی
        entry_path2.delete(0, tk.END)
        entry_path2.insert(0, file_path)
        savedWords_entry.delete(1.0, tk.END)
        with open (file_path , 'r' , encoding='utf-8') as file :
            content = file.read()
            savedWords_entry.insert(tk.END , content)
    def open_default_file():
        entry_path2.delete(0, tk.END)
        savedWords_entry.delete(1.0, tk.END)
        with open ('saved_words.txt' , 'r' , encoding='utf-8') as file :
            content = file.read()
            savedWords_entry.insert(tk.END , content)
    root2 = tk.Tk()
    root2.title("Saved words")
    set_window_size (root2, width_ratio=0.385, height_ratio=0.8)
    savedWords_entry = tk.Text(root2, width=70 , height=39)
    savedWords_entry.place (x = 10 , y = 50)
    with open ('saved_words.txt' , 'r' , encoding='utf-8') as file :
        content = file.read()
        savedWords_entry.insert(tk.END , content)
    #
    button_open_savedWords = tk.Button (root2, text="Open file", command = open_file)
    button_open_savedWords.place (x = 10 , y = 10)
    entry_path2 = tk.Entry (root2, width=50) #text box to enter files adress
    entry_path2.place (x = 80 , y = 13)
    #
    button_open_savedDefault = tk.Button (root2, text="Open Defaulte words", command =open_default_file)
    button_open_savedDefault.place (x = 400 , y = 10)
    root2.mainloop()

root = tk.Tk()
root.title("DocWords Translator")

set_window_size(root, width_ratio=0.385, height_ratio=0.8)

docText_entry = tk.Text(root, width=70 , height=10)
docText_entry.place (x = 10 , y = 10)

docWords_entry = tk.Text(root, width=30 , height=30 )
docWords_entry.place (x = 10 , y = 190)

button_getWords = tk.Button (root, text="Get words  ", command=insert_words)
button_getWords.place (x = 300 , y = 190)

button_translate = tk.Button (root, text="Translate    ", command=translate)
button_translate.place (x = 300 , y = 225)

button_saveWords = tk.Button (root, text="Save words", command=save)
button_saveWords.place (x = 300 , y = 260)

translate_all = tk.BooleanVar()
checkbox_Translate_all = tk.Checkbutton ( text = "Get all words" , variable = translate_all , font = ('' , 12))
checkbox_Translate_all.place (x = 295 , y = 295)

print_translated_word_in_terminal = tk.BooleanVar()
checkbox_print_translated_word_in_terminal = tk.Checkbutton ( text = "Print translated word in terminal" , variable = print_translated_word_in_terminal , font = ('' , 12))
checkbox_print_translated_word_in_terminal.place (x = 295 , y = 320)

clear_terminal = tk.BooleanVar()
checkbox_clear_terminal = tk.Checkbutton ( text = "Don't Clear terminal after any procces" , variable = clear_terminal , font = ('' , 12))
checkbox_clear_terminal.place (x = 295 , y = 345)

button_save_words_as = tk.Button (root, text="Save words as", command=open_file_dialog)
button_save_words_as.place (x = 300 , y = 380)

entry_path = tk.Entry (root, width=50) #text box to enter files adress
entry_path.place (x = 390 , y = 383)

button_open_savedWords = tk.Button (root, text="open saved words", command = open_saved_words)
button_open_savedWords.place (x = 300 , y = 415)

root.mainloop()





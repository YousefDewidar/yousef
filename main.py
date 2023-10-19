import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI


lt = LibreTranslateAPI("https://translate.argosopentech.com/")

lang_data = lt.languages()
lang_names = [var["name"] for var in lang_data]
lang_codes = {var['name']: var['code'] for var in lang_data}

#print(lang_names)

app = tk.Tk()
app.title("Yousef Translator")
app.geometry('660x350')
app.config(bg="black")

app_name = tk.Label(app, text=" ترجمة " ,font="arial 25 bold",bg='orange' ,padx=25)
app_name.place(x=260 ,y=25)
#--------------------------------------------
#inputs
input_label = tk.Label(app, text="Enter Text")
input_label.place(x=85 ,y=65)

input_lang = ttk.Combobox(app, width=19, values=lang_names)
input_lang.place(x=55 ,y=87)
input_lang.set("Select the lang")


input_text = tk.Text(app,height=11,width=30 , bg="#00ffff" )
input_text.place(x=15,y=110)
#----------------------------------------------
#outputs
output_label = tk.Label(app, text="Output")
output_label.place(x=490 ,y=55)

output_lang = ttk.Combobox(app, width=19, values=lang_names)
output_lang.place(x=440 ,y=87)
output_lang.set("Select the lang")

output_text = tk.Text(app,height=11,width=30 ,bg="#00ffff")
output_text.place(x=400,y=110)
#------------------------------------------
def tran():
    trans_pross = lt.translate(input_text.get("1.0", tk.END),
    lang_codes[input_lang.get()], lang_codes[output_lang.get()])
    output_text.insert("1.0",trans_pross)

def clear():
    output_text.delete("1.0", tk.END)
    input_text.delete("1.0", tk.END)

translate_btn = tk.Button(app,text="Translate" ,command=tran ,width=10)
translate_btn.place(x=293, y=190)

clear_btn = tk.Button(app,text="Clear" ,command=clear ,width=10 )
clear_btn.place(x=293, y=220)




def answer():
    mb.showerror("Answer", "Sorry, no answer available")


tk.mainloop()
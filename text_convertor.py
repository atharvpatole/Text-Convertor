from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from tkinter import *

def clearAll():
    text1.delete(1.0, END)
    text2.delete(1.0, END)

def convert():
    input_text = text1.get("1.0", "end")[:-1]
    output_text = transliterate(input_text, sanscript.ITRANS, sanscript.DEVANAGARI)
    text2.insert('end -1 chars', output_text)


root = Tk()
root.configure(background='#f2f2f2')
root.geometry("400x350")
root.title("Text Converter")

#Label
headlabel = Label(root, text='English to Devnagiri', font=('arial bold', 12), fg='black')
label1 = Label(root, text=" Enter Text ", fg='black')
label2 = Label(root, text=" Devnagiri Text", fg='black')

headlabel.grid(row=0, column=1)
label1.grid(row=1, column=0, padx=10, pady=10)
label2.grid(row=3, column=0, padx=10, pady=10)

#TextBox
text1 = Text(root, height=5, width=25, font="arial 13")
text2 = Text(root, height=5, width=25, font="arial 13")
text1.grid(row=1, column=1, padx=10, pady=10)
text2.grid(row=3, column=1, padx=10, pady=10)

#Button
button1 = Button(root, text="Convert into Devnagiri text", activebackground='#ccff99', fg="black", command=convert)
button1.grid(row=2, column=1)
button2 = Button(root, text="Clear", activebackground='#ffb3b3', fg="black", command=clearAll)
button2.grid(row=4, column=1)

root.mainloop()
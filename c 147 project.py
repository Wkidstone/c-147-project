from tkinter import *

root=Tk()
root.title("ASCII")
 
root.geometry("400x400")
root.configure(background='purple1')

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root,text = 'Name in Ascii : ' )
label1= Label(root, text="encrpted name : ")

def ac():
    input_word = str(enter_word.get())
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  " 
        ascii = int(ord(letter))
        encrypted= ascii-1
        label1["text"] += str(chr(encrypted))  
        
btn=Button(root,text = "Show name in ascii",command=ac,)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
label1.place(relx=0.5,rely=0.7,anchor=CENTER)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()
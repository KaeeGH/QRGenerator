import qrcode
import random
import tkinter as tk



def RandomLetter():
    number = random.randint(0, 23)
    if(number == 0):
       letter = "a"
       return letter
    elif(number == 1):
       letter = "b"
       return letter
    elif(number == 2):
       letter = "c"
       return letter
    elif(number == 3):
       letter = "e"
       return letter
    elif(number == 4):
       letter = "f"
       return letter
    elif(number == 5):
       letter = "g"
       return letter
    elif(number == 6):
       letter = "h"
       return letter
    elif(number == 7):
       letter = "i"
       return letter
    elif(number == 8):
       letter = "j"
       return letter
    elif(number == 9):
       letter = "k"
       return letter
    elif(number == 10):
       letter = "l"
       return letter
    elif(number == 11):
       letter = "m"
       return letter
    elif(number == 12):
       letter = "n"
       return letter
    elif(number == 13):
       letter = "o"
       return letter
    elif(number == 14):
       letter = "p"
       return letter
    elif(number == 15):
       letter = "q"
       return letter
    elif(number == 16):
       letter = "r"
       return letter
    elif(number == 17):
       letter = "s"
       return letter
    elif(number == 18):
       letter = "t"
       return letter
    elif(number == 19):
       letter = "u"
       return letter
    elif(number == 20):
       letter = "w"
       return letter
    elif(number == 21):
       letter = "x"
       return letter
    elif(number == 22):
       letter = "y"
       return letter
    elif(number == 23):
       letter = "z"
       return letter

def QrGenerate(event):
    RandomLetter()
    lett = RandomLetter()
    a = lett
    b = lett
    c = lett
    d = lett
    e = lett
    f = lett

    qrimg = qrcode.make(a + b + c + d + e + f)
    qrimg.show()

root = tk.Tk()
root.title(u'QrGenerator')
root.geometry('400x300')


button = tk.Button(text=u'QR生成')
button.bind('<Button-1>', QrGenerate)
button.pack()


root.mainloop()




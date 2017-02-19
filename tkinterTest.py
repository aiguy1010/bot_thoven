from Tkinter import *
import bot_Toven
from sine_wave_test_1 import *
from PIL import ImageTk, Image
fields = ('Note 1', 'Note 2', 'Note 3', 'Duration 1', 'Duration 2', 'Duration 3')

def fetch(entries):
   anRay = []
   for entry in entries:
      anRay.append(entry[1].get())
   callPasser(anRay)

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=10, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
    root = Tk()
    root.title("bot_thoven")

    img = ImageTk.PhotoImage(Image.open("bot_thoven_art_smol.png"))
    panel = Label(root, image = img)
    panel.pack()

    Label(root, text="Choose 3 notes A through G").pack()
    Label(root, text="No sharps or flats").pack()
    Label(root, text="Duration is in seconds").pack()

    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Create',command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()

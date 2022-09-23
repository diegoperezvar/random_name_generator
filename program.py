from tkinter import *
import tkinter as tk
from names import spanishNames
from names import englishNames
from names import frenchNames
from names import spanishSurnames
from names import englishSurnames
from names import frenchSurnames
import random

def create_window():
  new_window = Toplevel()
  

window = Tk()
window.title("Name Generator 1.0.0")

#getting screen width and height of display
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.configure(bg='#292929')
label = tk.Label(window, text="Random name generator \n 1 for spanish name \n 2 for english name \n 3 for french name",height= 4,width= 20)
label.pack()

e = Entry(window)
e.pack()
e.focus_set()

class nameGenerator:
   def __init__(self,):
     pass
   #names methods
   def spanishNameGiver(spanishNames):
     return(spanishNames)
   def englishNameGiver(englishNames):
     return(englishNames)
   def frenchNameGiver(frenchNames):
     return(frenchNames)
   
   # surnames methods
   def spanishSurnameGiver(spanishSurnames):
     return(spanishSurnames)
   def englishSurnameGiver(englishSurnames):
     return(englishSurnames)
   def frenchSurnameGiver(frenchSurnames):
     return(frenchSurnames)


def callback():
  
  canvas= Canvas(window, width= 1000, height= 750, bg="#292929",)
 
  if e.get() == "1":
    canvas.create_text(100, 50, text= nameGenerator.spanishNameGiver(random.choice(spanishNames)) +" "+ nameGenerator.spanishSurnameGiver(random.choice(spanishSurnames))  ,fill="black",font=('Helvetica 15 bold'))
  elif e.get() == "2":
    canvas.create_text(100, 50, text= nameGenerator.englishNameGiver(random.choice(englishNames)) +" "+ nameGenerator.englishSurnameGiver(random.choice(englishSurnames))  ,fill="black",font=('Helvetica 15 bold'))
  elif e.get() == "3":
    canvas.create_text(100, 50, text=  nameGenerator.frenchNameGiver(random.choice(frenchNames)) +" "+ nameGenerator.frenchSurnameGiver(random.choice(frenchSurnames))  ,fill="black",font=('Helvetica 15 bold'))
  else:
    canvas.create_text(100, 50, text= "invalid number"  ,fill="red",font=('Courier 15 bold'))
  canvas.pack()
  
b = Button(window, text = "Generate name", width = 12, command = callback)
b.pack()

canvas= Canvas(window, width= 1000, height= 750, bg="#292929")























#
#class nameGenerator:
#    def __init__(self,):
#      pass
#    #names methods
#    def spanishNameGiver(spanishNames):
#      print(spanishNames)
#
#    def englishNameGiver(englishNames):
#      print(englishNames)
#
#    def frenchNameGiver(frenchNames):
#      print(frenchNames)
#    
#    # surnames methods
#    def spanishSurnameGiver(spanishSurnames):
#      print(spanishSurnames)
#
#    def englishSurnameGiver(englishSurnames):
#      print(englishSurnames)
#
#    def frenchSurnameGiver(frenchSurnames):
#      print(frenchSurnames)
##nameGenerator.spanishNameGiver(random.choice(spanishNames))
##nameGenerator.englishNameGiver(random.choice(englishNames))
##nameGenerator.frenchNameGiver(random.choice(frenchNames))
##genera una pregunta y recibe una respuesta

##
#if question == "1":
#  nameGenerator.spanishNameGiver(random.choice(spanishNames))
#  nameGenerator.spanishSurnameGiver(random.choice(spanishSurnames))
#
#elif question == "2":
#  nameGenerator.englishNameGiver(random.choice(englishNames))
#  nameGenerator.englishSurnameGiver(random.choice(englishSurnames))
#
#elif question == "3":
#  nameGenerator.frenchNameGiver(random.choice(frenchNames))
#  nameGenerator.frenchSurnameGiver(random.choice(frenchSurnames))
#
#else:
#  print("invalid number")
 



window.mainloop()
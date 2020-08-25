from tkinter import *
from tkinter.ttk import *
import secrets #for the really good random generator

window=Tk()
window.title("Rock_Paper_Scissors")
Label(window, text = 'Rock_Paper_Scissors', font =('Comic Sans', 12)).pack(side = TOP, pady = 10) 
rock=PhotoImage(file = r"C:\Users\cathe\Desktop\Terminal_RPS\GUI_RPS\rock.png")
paper=PhotoImage(file=r"C:\Users\cathe\Desktop\Terminal_RPS\GUI_RPS\paper.png")
scissor=PhotoImage(file=r"C:\Users\cathe\Desktop\Terminal_RPS\GUI_RPS\scissors.png")

rockimage=rock.subsample(3,3)
paperimage=paper.subsample(3,3)
scissorsimage=scissor.subsample(3,3)
Button(window,text="Rock",image=rockimage,compound=RIGHT).pack(side=TOP)
Button(window,text="Paper",image=paperimage,compound=LEFT).pack(side=TOP)
Button(window,text="Scissors",image=scissorsimage,compound=LEFT).pack(side=TOP)


mainloop()

def play_game():
	pass
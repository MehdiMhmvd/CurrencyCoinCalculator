#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import StringVar
class Converter:
    

    def __init__(self, master):
        master.geometry("640x480")
        #master.maxsize (640,480)
        notebook = ttk.Notebook(master)
        notebook.pack(side = TOP ,fill  = BOTH, expand = True , anchor = "nw")
        #---------------------------------------------------------------------------------------------------------------------------------
        self.f1 =  ttk.Frame(notebook, height = 320 , width = 240, relief = RIDGE,padding = (10,10))  #
        self.f2 = ttk.Frame(notebook,  relief = RIDGE,padding = (10,10))
        #self.f1.pack()
        notebook.add(self.f1 , text = "Currency")
        notebook.add(self.f2 , text = "Coin")
        #ttk.LabelFrame(self.f1, height = 640 , width = 480, text = "Main Frame ").pack()
#*-----------------currency tab-----------------------------------------------------------------------------------------------------------
        self.dvar= StringVar()
        self.evar = StringVar()
        self.ounce = StringVar()
        self.USD = ttk.Label(self.f1,text = "$ = ", font = 18).grid (row = 3 , column = 0,sticky = "E")
        self.EU = ttk.Label(self.f1,text = "€ =",font = 18).grid (row = 4 , column = 0,sticky = "E")
        self.AED = ttk.Label(self.f1,text = "AED Price in Iran =").grid (row = 0 , column = 0,sticky = "W")
        self.ounce = ttk.Label(self.f1,text = "Ounce =").grid (row = 2 , column = 0,sticky = "E")
        #-----------------------------------------------------------------------------------------------------------------------
        self.euro  = ttk.Label(self.f1,text = "euro ",textvariable = self.evar).grid (row = 4 , column = 1,sticky = "W")
        self.dollar = ttk.Label(self.f1,text = "dollar",textvariable = self.dvar).grid (row = 3 , column = 1,sticky = "W")

        self.entry_AED = ttk.Entry(self.f1, width = 10)
        self.entry_ounce = ttk.Entry(self.f1, width =10)
        
        self.entry_AED.grid (row = 0 , column = 1)
        self.entry_ounce.grid(row= 2 , column = 1)
        b_convert=ttk.Button(self.f1, text = "Press to Convert" , command = self.convert1).grid (row = 5 , column = 0)
  #####################################################################################
        #Coin tab
        self.qvar =StringVar()
        self.hvar =StringVar()
        self.cvar = StringVar()

        self.q = ttk.Label(self.f2, text = "Quarter coin = ").grid (row = 0 , column = 0 ,sticky = "W")
        self.h = ttk.Label(self.f2, text = "Half coin = ").grid (row = 1 , column = 0,sticky = "W")
        self.c = ttk.Label(self.f2, text = "Complate coin = ").grid (row = 2 , column = 0,sticky = "W")

        self.qprice = ttk.Label(self.f2, textvariable= self.qvar, font = 14).grid (row = 0 , column = 1,sticky = "E")
        self.hprice = ttk.Label(self.f2, textvariable= self.hvar, font = 14).grid (row = 1 , column = 1,sticky = "E")
        self.cprice = ttk.Label(self.f2, textvariable= self.cvar, font = 14).grid (row = 2 , column =1,sticky = "E")
        


  

    def convert1 (self) :
        
        self.dvar.set(round(int(self.entry_AED.get() ) * 3.67)   )
        self.evar.set(round(int(self.entry_AED.get() )* 4.32)   )
        self.gram_1 = round((( ( int(self.entry_ounce.get()) / 31.103431)* .900) * int(self.dvar.get() )))
        print(self.gram_1)
        self.cvar.set(round(self.gram_1 * 8.133) )
        self.hvar.set(round(self.gram_1 * 4.066 ))
        self.qvar.set(round(self.gram_1 * 2.033 ))

            
def main():            
    
    root = Tk()
    feedback = Converter(root)
    
    root.mainloop()
    
if __name__ == "__main__": main()











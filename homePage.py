from tkinter import *

class Home_page(Frame):
   def __init__(self, master, word_search, sudoku, crossword):
       """Initialize Frame."""
       self.word_search = word_search
       self.sudoku = sudoku
       self.crossword=crossword
       super(Home_page, self).__init__(master,background="orange2")
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       """Create widgets to get story information and to display story."""
       # create instruction label
       Label(self, text="",bg="orange2"
             ).grid(row=0, column=0, sticky=N)

       Label(self, text="Brain Games", font="Courier 40 bold", bg="orange2",
             fg="firebrick3").grid(row=0, column=1, sticky=N)

       Label(self, text="", bg="orange2",
             ).grid(row=0, column=2, sticky=N)

       Label(self,
             text="and", font="Courier 40 bold",bg="orange2",
             fg="firebrick3").grid(row=1, column=1, sticky=N)

       Label(self,
             text="Puzzles", font="Courier 40 bold",bg="orange2",
             fg="firebrick3").grid(row=2, column=1, sticky=N)

       Label(self,
             text="Slogan", font="Courier 20",bg="orange2",
             fg="firebrick4").grid(row=3, column=1, sticky=N)

       Button(self, text="Word Search",
              font="Courier 18", bd=5, command=self.wordSearch
              ).grid(row=4, column=1, sticky=N)

       Button(self, text="Sudoku",
              font="Courier 18", bd=5, command=self.Sudoku
              ).grid(row=5, column=1, sticky=N)

       Button(self, text="Crossword",
              font="Courier 18", bd=5, command=self.cross_word
              ).grid(row=6, column=1, sticky=N)

   def wordSearch(self):
       pass
   def Sudoku(self):
       pass
   def cross_word(self):
       pass


       # Button(self, text="Play",
       #        font="Courier 23", bd=5, command=self.single_player
       #        ).grid(row=3, column=1, sticky=N)
       #
       # Label(self, text="", bg = "LightSteelBlue2"
       #       ).grid(row=4, column=1, sticky=N)
       #
       # Button(self, text="Instructions",
       #        font="Courier 23", bd=5,
       #        command=self.instructions
       #        ).grid(row=5, column=1, sticky=N)
       #
       # Label(self, text="", bg="LightSteelBlue2"
       #       ).grid(row=6, column=1, sticky=N)
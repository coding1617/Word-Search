from tkinter import *
import random


class Word_Search2(Frame):
   def __init__(self, master, text_file, end_screen):
       """Initialize Frame."""
       self.end_screen = end_screen
       self.text_file = text_file
       super(Word_Search2, self).__init__(master, background="coral")
       self.grid()
       self.create_widgets()

   def create_widgets(self):

       self.letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                       "S",
                       "T", "U", "V", "W", "X", "Y", "Z"]
       letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                  "T", "U", "V", "W", "X", "Y", "Z"]
       lowerr_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                  "t", "u", "v", "w", "x", "y", "z"]

       self.letter_dict = {}

       for pos in range(len(letter_list)):
           self.letter_dict[letter_list[pos]] = lowerr_list[pos]
       line_list = []
       self.actual_answer = []
       story = ""
       for line in self.text_file:
           for char in line:
               if char != " " and char != "\n":
                   self.actual_answer.append(char)
           self.char_per_line = 0
           for char in line:
               if char == ".":
                   random_char = random.choice(letter_list)
                   line_list.append(random_char)
                   self.char_per_line += 1
               elif char == " ":
                   line_list.append(char)
               else:
                   line_list.append(char)
                   self.char_per_line += 1
           for char in line_list:
               story += char
           line_list = []
       self.story_txt = Text(self, width=46, height=17, wrap=WORD, font="Courier 18", bg="light salmon")
       self.story_txt.grid(row=0, column=0, columnspan=4)
       self.story_txt.insert(0.0, story)

       Label(self, text="", bg="coral", font="Courier 12"
             ).grid(row=16, column=0, sticky=W)
       Button(self, text="Check", bg="tomato", fg="black",
              font="Courier 15 bold", bd=5, command=self.check
              ).grid(row=17, column=1, sticky=E)
       Button(self, text="Quit", bg="tomato", fg="black",
              font="Courier 15 bold", bd=5, command=self.quit
              ).grid(row=17, column=2, sticky=W)

       if self.actual_answer[2] == "P":
           self.word_list = ["phoenix", "prophecy", "evil", "thestral", "darkness"]
       if self.actual_answer[17] == "M":
           self.word_list = ["avox", "bow and arrow", "district twelve", "forcefield", "hunger games", "jabberjay",
                             "mockingjay", "muttation", "nightlock berry", "panem"]
           self.char_per_line -= 1
       if self.actual_answer[31] == "O":
           self.word_list = ["ashes", "inferno", "phoenix", "blaze", "ignite", "burn", "flame", "kindle", "spark",
                             "smolder", "smoke", "combust", "pyrokinetic", "incandescent", "heat"]

       Label(self, text=" ", bg="coral").grid(row=0, column=50, sticky=E)
       row_count = 2
       column_count = 0
       for word in self.word_list:
           if column_count == 5:
               row_count += 1
               column_count = 0
           Label(self, text=word, bg="coral", font="Courier 12"
                 ).grid(row=row_count, column=column_count, sticky=W)
           column_count += 1

   def check(self):
       story = ""

       answer_list = []
       answers = self.story_txt.get(0.0, END)
       for thing in answers:
           if thing != " " and thing != "\n":
               answer_list.append(thing)
       char_count = 0
       for pos in range(len(answer_list)):
           if char_count == self.char_per_line:
               story += "\n"
               char_count = 0
           if answer_list[pos] == "*":
               if self.actual_answer[pos] != ".":
                   story += (self.letter_dict[self.actual_answer[pos]])
                   story += " "
                   char_count += 1

               else:
                   story += random.choice(self.letter_list)
                   story += " "
                   char_count += 1

           else:
               story += answer_list[pos]
               story += " "
               char_count += 1
       self.story_txt.delete(0.0, END)
       self.story_txt.insert(0.0, story)

   def quit(self):
       self.end_screen()
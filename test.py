#source for the code: 
    #C:\Users\kaiba\OneDrive\Asztali gép\Final Project\project-benedek-kaibas\src\test.py

#importing all the important liraries that I need
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Button
import random
#from tkinter import *
import json 


class Pictures:

    print("Nadal is playing with the Babolat Pure Aero\nFederer is playing with the Wilson Pro Staff\nDjokovic is playing with the Head Speed\nMurray is playing with the Head Radical")

    #init file to access all the pictures
    def __init__(self, root):
        #getting the root in self
        self.root = root
        #displaying the name of the project
        self.root.title("Picture Match Game")
        #setting the index one and two for the buttons - this contribute to the code that is switching the pictures based on button press
        self.current_image_index_one = 0
        self.current_image_index_two = 0

        #list of rackets that has to match the players
        self.images = [
            Image.open("Pictures/wilson.jpg"),
            Image.open("Pictures/babolat.jpg"),
            Image.open("Pictures/head.jpg"),
            Image.open("Pictures/radical.jpg")
        ]

        #list of players that has to match the rackets
        self.new_images = [
            Image.open('Pictures/nadal.png'),
            Image.open('Pictures/djokovic.png'),
            Image.open('Pictures/federer.png'),
            Image.open('Pictures/murray.png')
        ]

        #with this we can display all the images in order. For that we have to use them inside the button one and two functions.
        self.button_one_steps = [0,1,2,3]
        self.button_two_steps = [0,1,2,3]

        #counting how many times the buttons get pressed
        self.counting_button_one = 0
        self.counting_button_two = 0 
    #displaying the application so user can see it 
    def display_images(self):
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))

        # Display the current image above button one 
        ax[0].imshow(self.images[self.current_image_index_one])
        ax[0].axis('off')

        # Display the current image above button two 
        ax[1].imshow(self.new_images[self.current_image_index_two])
        ax[1].axis('off')

        # Add a button one 
        button_one = tk.Button(self.root, text='Press One', command=self.button_click_one)
        button_one.grid(row = 1, column = 0)
        #add button two 
        button_two = tk.Button(self.root, text = 'Press Two', command = self.button_click_two)
        button_two.grid(row = 1, column = 2)
        #here we have to add another button for saving the inputs
        button_save = tk.Button(self.root, text = "Save", command = self.button_save)
        button_save.grid(row = 1, column = 1)

        # Canvas and Matplotlib library are needed for displaying pictures and the application
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        #this shows the display of the program
        canvas.draw()
        #making a grid so we can place the buttons 
        canvas.get_tk_widget().grid(row = 0, column = 0, columnspan = 3) 

    #this function getting self to access buttons and prints button pressed after user prints the button
    def button_click_one(self):
        #print("Button One Pressed!")
        self.current_image_index_one = (self.current_image_index_one + 1) % (len(self.button_one_steps))
        self.counting_button_one += 1
        text = (f"Button one was klicked {self.counting_button_one} times")
        #print(text)
        self.display_images()

    #this function does the same with button two 
    def button_click_two(self):
        #print("Button Two Pressed!")
        self.current_image_index_two = (self.current_image_index_two + 1) % (len(self.button_two_steps))
        self.counting_button_two += 1
        text = (f"Button two was klicked {self.counting_button_two} times")
        #print(text) 
        self.display_images()

    #this function does save the users input and stores it
    def button_save(self):
        print(self.counting_button_one, self.counting_button_two)
        store = self.counting_button_one

        data = store
        with open('data.json', 'w') as fh:
            data = json.dump(data, fh)
            
        with open('data.json', 'r') as fh:
            saved_data = json.load(fh)

        result = saved_data
        
        if result <= 4:
            print(f"Congratulation your score is: {result} below 4 and that means you picked all the pictures correctly for the first time")
        elif 4 <= result <= 6:
            print(f"Congratulation your score is: {result}. You did not get it for the first time, but you still scored an A")
        elif 6 <= result <= 8:
            print(f"Congratulation your score is: {result}. You did good and your grade is a B")
        elif 8 <= result <= 10:
            print(f"Congratulation your score is: {result}. You did good and your grade is a C")
        else:
            print(f"Your score is {result}. Better luck next time ;)")
    
        


#calling the main class and the pics to display it. Without this code would work, but we wouldn't see anything
if __name__ == "__main__":
    root = tk.Tk()
    pics = Pictures(root)
    pics.display_images()
    root.mainloop()

from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack(side='top')

my_label["text"] = "This is a New Text"
my_label.config(text = "This is a New Text")

# Button

def button_clicked():
    print("Clicked")
    new_text = input.get()
    # my_label.config(text = "Button got clicked")
    my_label.config(text = new_text)

button = Button(text="Click Me", command=button_clicked,)
button.pack()


# Entry

input = Entry(width=10)
input.pack()
print(input.get())


# import turtle

# tim = turtle.Turtle()
# tim.write("Sujan Pradhan",font=("Times New Roman", 80,"bold"))



 
window.mainloop()
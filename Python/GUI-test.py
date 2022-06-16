from tkinter import *

# Create a window with a title and a size of 400x400 pixels
root = Tk()
root.title("GUI-test")
root.geometry("400x400")

# Create a label with the text "Hello World"
label = Label(root, text="Hello World")
label.pack()

# Create a button with the text "Click me"
button = Button(root, text="Click me")
button.pack()

# Create a text field with a default value "Hello World"
text_field = Entry(root)
text_field.insert(0, "Hello World")
text_field.pack()

# Create a checkbox with the text "Check me"
check_box = Checkbutton(root, text="Check me")
check_box.pack()

root.mainloop()

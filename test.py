#import and make window
import tkinter as tk
window = tk.Tk()

#custom pf window
window.title("My Window")  # Set the title
window.geometry("400x300")  # Set the size (width x height)

#widget
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()
button = tk.Button(window, text="Click Me")
button.pack()

#keep it running
window.mainloop()

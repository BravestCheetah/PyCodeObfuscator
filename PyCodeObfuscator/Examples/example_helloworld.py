import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World App")
root.geometry("300x150")

# Create a label with "Hello, World!"
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

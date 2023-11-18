import tkinter as tk
from tkinter import ttk

def create_palindrome_frame(parent, colors):
    def update_theme(colors):
        frame.config(background=colors['bg'])
        entry.config(background=colors['text_bg'], foreground=colors['text_fg'])
        find_button.config(background=colors['bg'], foreground=colors['text_fg'])
        result_label.config(background=colors['bg'], foreground=colors['text_fg'])

    # Function to find palindromes in a given line of text
    def find_palindromes():
        # Get the text from the entry widget
        text = entry.get()
        # Split the text by spaces and check for palindromes
        palindromes = [word for word in text.split() if word == word[::-1]]
        # Display the palindromes in the label
        result_label.config(text=f"Palindromes: {', '.join(palindromes)}")

    # Create a frame for the entry, button, and label
    frame = ttk.Frame(parent, padding="10")

    # Create the entry widget
    entry = ttk.Entry(frame, width=50)
    entry.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N))

    # Create the find button
    find_button = ttk.Button(frame, text="Find Palindromes", command=find_palindromes)
    find_button.grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E, tk.N))

    # Create a label to display the result
    result_label = ttk.Label(frame, text="Palindromes will be shown here.", padding="10")
    result_label.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

    # Initialize the theme
    update_theme(colors)

    # Return the frame and the theme update function
    return frame, update_theme

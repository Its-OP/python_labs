import tkinter as tk
from tkinter import ttk


def set_palindrome_frame(parent, theme_styles):
    # Function to find palindromes in a given line of text
    def find_palindromes():
        # Get the text from the entry widget
        text = entry.get()
        # Split the text by spaces and check for palindromes
        palindromes = [word for word in text.split() if word == word[::-1]]
        # Display the palindromes in the label
        result_label.config(text=f"Palindromes: {', '.join(palindromes)}")

    frame = ttk.Frame(parent, padding="10", style=theme_styles['frame'] + '.TFrame')
    frame.grid_columnconfigure(0, weight=1)  # Make the Entry expand with the column
    frame.grid_rowconfigure(1, weight=1)  # Make the Label expand with the row

    # Create the entry widget with the theme style
    entry = ttk.Entry(frame, width=50)
    entry.grid(row=0, column=0, sticky=(tk.W, tk.E))

    # Create the find button with the theme style
    find_button = ttk.Button(frame, text="Find Palindromes", command=find_palindromes)
    find_button.grid(row=0, column=1, padx=5, sticky=(tk.E, tk.N))

    # Create a label to display the result with the theme style
    result_label = ttk.Label(frame, text="Palindromes will be shown here.", padding="10",)
    result_label.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.S))

    # Function to update the theme
    def change_scenario_frame_theme(theme_styles):
        frame.config(style=theme_styles['frame'] + '.TFrame')

    return frame, change_scenario_frame_theme

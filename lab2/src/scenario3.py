import tkinter as tk
from tkinter import ttk

def set_sentence_frame(parent, theme_styles):
    def invert_even_words():
        # Get the sentence from the entry widget
        sentence = entry_sentence.get()
        # Split the sentence into words
        words = sentence.split()
        # Invert every even word (considering even as 0-based indexing)
        inverted_sentence = ' '.join(word if index % 2 == 0 else word[::-1] for index, word in enumerate(words))
        # Display the result in the label
        result_label.config(text=f"Inverted Sentence: {inverted_sentence}")

    frame = ttk.Frame(parent, padding="10", style=theme_styles['frame'] + '.TFrame')
    frame.grid_columnconfigure(0, weight=1)

    # Entry for the sentence
    ttk.Label(frame, text="Enter a sentence:").grid(row=0, column=0, sticky=tk.W)
    entry_sentence = ttk.Entry(frame, width=50)
    entry_sentence.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=5)

    # Invert button
    invert_button = ttk.Button(frame, text="Invert Even Words", command=invert_even_words)
    invert_button.grid(row=2, column=0, sticky=(tk.E, tk.W), pady=5)
    invert_button['takefocus'] = False  # Prevent the button from receiving focus

    # Label to display the result
    result_label = ttk.Label(frame, text="The result will be shown here.", padding="10")
    result_label.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.S))

    # Function to update the theme
    def change_scenario_frame_theme(theme_styles):
        frame.config(style=theme_styles['frame'] + '.TFrame')

    return frame, change_scenario_frame_theme

import tkinter as tk
from tkinter import ttk

def set_sentence_frame(parent, theme_styles):
    def invert_even_words():
        # Отримуємо речення з поля вводу
        sentence = entry_sentence.get()
        # Розбиваємо речення на слова
        words = sentence.split()
        # Інвертуємо кожне слово на непарних позиціях
        inverted_sentence = ' '.join(word if index % 2 == 0 else word[::-1] for index, word in enumerate(words))
        # Виводимо результат в поле виводу
        result_label.config(text=f"Inverted Sentence: {inverted_sentence}")

    # Створюємо фрейм
    frame = ttk.Frame(parent, padding="10", style=theme_styles['frame'] + '.TFrame')
    # Змушуємо першу колонку (з полями вводу речення) займати все доступне місце по горизонталі
    frame.grid_columnconfigure(0, weight=1)
    # Змушуємо 3 колонку (з полем виводу) займати все доступне місце по вертикалі
    frame.grid_rowconfigure(3, weight=1)

    # Ініціалізуємо поле вводу речення
    ttk.Label(frame, text="Enter a sentence:").grid(row=0, column=0, sticky=tk.W)
    entry_sentence = ttk.Entry(frame, width=50)
    entry_sentence.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=5)

    # Ініціалізуємо кнопку для обробки речення
    invert_button = ttk.Button(frame, text="Invert Even Words", command=invert_even_words)
    invert_button.grid(row=2, column=0, sticky=(tk.E, tk.W), pady=5)

    # Ініціалізуємо поле для виводу результату
    result_label = ttk.Label(frame, text="The result will be shown here.", padding="10")
    result_label.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.S))

    # Ініціалізуємо функцію для оновлення теми
    def change_scenario_frame_theme(theme_styles):
        frame.config(style=theme_styles['frame'] + '.TFrame')

    return frame, change_scenario_frame_theme

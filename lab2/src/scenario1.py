import tkinter as tk
from tkinter import ttk


def set_palindrome_frame(parent, theme_styles):
    # Ініціалізуємо функцію для знаходження паліндромів в тексті
    def find_palindromes():
        # Отримуємо текст з поля вводу
        text = entry.get()
        # Розбиваємо текст за пробілами
        palindromes = [word for word in text.split() if word == word[::-1]]
        # Виводимо паліндроми в полі виводу
        result_label.config(text=f"Palindromes: {', '.join(palindromes)}")

    # Ініціалізуємо Фрейм сценарію
    frame = ttk.Frame(parent, padding="10", style=theme_styles['frame'] + '.TFrame')
    # Змушуємо нульову колонку займати все доступне місце зліва направо (щоб елементи могли масштабуватись горизонтально)
    frame.grid_columnconfigure(0, weight=1)
    # Змушуємо нульовий рядок займати все доступне місце згори вниз (щоб елементи могли 'приліпати' до нижньої границі)
    frame.grid_rowconfigure(1, weight=1)

    # Створюємо віджет для ввода тексту
    entry = ttk.Entry(frame, width=50)
    entry.grid(row=0, column=0, sticky=(tk.W, tk.E))

    # Створюємо кнопку для знаходження паліднромів в рядку
    find_button = ttk.Button(frame, text="Find Palindromes", command=find_palindromes)
    find_button.grid(row=0, column=1, padx=5, sticky=(tk.E, tk.N))

    # Створюємо поле виводу для знайдених паліндромів
    result_label = ttk.Label(frame, text="Palindromes will be shown here.", padding="10",)
    result_label.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.S))

    # Ініціалізуємо функцію для оновлення теми
    def change_scenario_frame_theme(theme_styles):
        frame.config(style=theme_styles['frame'] + '.TFrame')

    return frame, change_scenario_frame_theme

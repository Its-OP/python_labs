import tkinter as tk
from tkinter import ttk
from cmath import sqrt


def set_equation_frame(parent, theme_styles):
    def solve_quadratic():
        try:
            # Беремо введені значення коефіцієнтів
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            # Перевіряємо що коефіцієнт a не дорівнює 0 (адже інакше ми маємо справу з лінійним рівнянням)
            if a == 0:
                result_label.config(text="Coefficient 'a' cannot be zero for a quadratic equation.")
                return

            # Рахуємо дискримінант
            discriminant = b**2 - 4*a*c

            # Перевіряємо значення дискримінанту
            if discriminant < 0:
                result_label.config(text='No real solutions exist.')
            elif discriminant == 0:
                x = -b / (2*a)
                result_label.config(text=f'One real solution: {x:.2f}')
            else:
                sol1 = (-b - sqrt(discriminant).real) / (2*a)
                sol2 = (-b + sqrt(discriminant).real) / (2*a)
                result_label.config(text=f'Real solutions: {sol1:.2f} and {sol2:.2f}')
        except ValueError:
            result_label.config(text='Please enter valid coefficients.')

    # Створюємо фрейм
    frame = ttk.Frame(parent, padding="10", style=theme_styles['frame'] + '.TFrame')
    # Змушуємо першу колонку (з полями вводу коефіцієнтів) займати все доступне місце по горизонталі
    frame.grid_columnconfigure(1, weight=1)
    # Змушуємо 4 колонку (з полем виводу) займати все доступне місце по вертикалі
    frame.grid_rowconfigure(4, weight=1)

    # Ініціалізуємо поле вводу для коефіцієнту a
    ttk.Label(frame, text="a:").grid(row=0, column=0, sticky=(tk.W, tk.N), pady=5)
    entry_a = ttk.Entry(frame, width=10)
    entry_a.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N), padx=5, pady=5)

    # Ініціалізуємо поле вводу для коефіцієнту b
    ttk.Label(frame, text="b:").grid(row=1, column=0, sticky=(tk.W, tk.N), pady=5)
    entry_b = ttk.Entry(frame, width=10)
    entry_b.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N), padx=5, pady=5)

    # Ініціалізуємо поле вводу для коефіцієнту c
    ttk.Label(frame, text="c:").grid(row=2, column=0, sticky=(tk.W, tk.N), pady=5)
    entry_c = ttk.Entry(frame, width=10)
    entry_c.grid(row=2, column=1, sticky=(tk.W, tk.E, tk.N), padx=5, pady=5)

    # Ініціалізуємо кнопку для вирішення рівняння
    solve_button = ttk.Button(frame, text="Solve", command=solve_quadratic)
    solve_button.grid(row=3, column=1, sticky=(tk.E, tk.W, tk.N), pady=5)

    # Ініціалізуємо поле для виведення результату
    result_label = ttk.Label(frame, text="Enter coefficients and click Solve.", padding="10")
    result_label.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.S))

    # Ініціалізуємо функцію для оновлення теми
    def change_scenario_frame_theme(theme_styles):
        frame.config(style=theme_styles['frame'] + '.TFrame')

    return frame, change_scenario_frame_theme

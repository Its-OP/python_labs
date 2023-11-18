import tkinter as tk
from tkinter import ttk
from cmath import sqrt


def set_equation_frame(parent, theme_styles):
    def solve_quadratic():
        try:
            # Retrieve values for a, b, and c from the Entry widgets
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            # Check if a is zero
            if a == 0:
                result_label.config(text="Coefficient 'a' cannot be zero for a quadratic equation.")
                return

            # Calculate the discriminant
            discriminant = b**2 - 4*a*c

            # Discriminant check before finding the roots
            if discriminant < 0:
                result_label.config(text='No real solutions exist.')
            elif discriminant == 0:
                x = -b / (2*a)
                result_label.config(text=f'One real solution: {x:.2f}')
            else:
                # Calculate two real solutions
                sol1 = (-b - sqrt(discriminant).real) / (2*a)
                sol2 = (-b + sqrt(discriminant).real) / (2*a)
                result_label.config(text=f'Real solutions: {sol1:.2f} and {sol2:.2f}')
        except ValueError:
            result_label.config(text='Please enter valid coefficients.')

    frame = ttk.Frame(parent, padding="10", style=theme_styles['frame'] + '.TFrame')
    frame.grid_columnconfigure(1, weight=1)

    # Entry for coefficient a
    ttk.Label(frame, text="a:").grid(row=0, column=0, sticky=tk.W)
    entry_a = ttk.Entry(frame, width=10)
    entry_a.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)

    # Entry for coefficient b
    ttk.Label(frame, text="b:").grid(row=1, column=0, sticky=tk.W)
    entry_b = ttk.Entry(frame, width=10)
    entry_b.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5)

    # Entry for coefficient c
    ttk.Label(frame, text="c:").grid(row=2, column=0, sticky=tk.W)
    entry_c = ttk.Entry(frame, width=10)
    entry_c.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5)

    # Solve button
    solve_button = ttk.Button(frame, text="Solve", command=solve_quadratic)
    solve_button.grid(row=3, column=1, sticky=(tk.E, tk.W, tk.N), pady=5)

    # Label to display the result
    result_label = ttk.Label(frame, text="Enter coefficients and click Solve.", padding="10")
    result_label.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.S))

    # Function to update the theme
    def change_scenario_frame_theme(theme_styles):
        frame.config(style=theme_styles['frame'] + '.TFrame')

    return frame, change_scenario_frame_theme

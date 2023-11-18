import tkinter as tk
from tkinter import ttk


# Створюємо клас вікна, наслідуючи його від кореневого віжета Tkinter
class ApplicationWindow(tk.Tk):
    def __init__(self, set_scenario_frame, theme='light'):
        # Ініціалізуємо батьківський клас
        super().__init__()

        # Задаємо початковий розмір вікна
        self.geometry('600x400')

        # Ініціалізуємо поле з кольорами для темної та світлої тем
        self.themes = {
            'light': {'bg': 'white', 'text_bg': 'white', 'text_fg': 'black', 'frame': 'LightFrame', 'label': 'LightLabel', 'button': 'LightButton', 'entry': 'LightEntry'},
            'dark': {'bg': 'gray32', 'text_bg': 'gray32', 'text_fg': 'white', 'frame': 'DarkFrame', 'label': 'DarkLabel', 'button': 'DarkButton', 'entry': 'DarkEntry'}
        }

        # Інінціалізуємо поле зі стислою інформацією про автора
        self._author_info_text = ('''Автор програми:
Простаков Олег, КП-02
ФПМ, ПЗКС, НТУУ "КПІ"''')

        # Інінціалізуємо поле зі значенням обраної кольоровї теми
        self.theme = theme

        # Інінціалізуємо поле з функцією, що повертає Фрейм з заданими сценарієм елементами
        self.set_scenario_frame = set_scenario_frame

        self.create_styles()
        self.create_widgets()
        self.apply_theme()

    # Ініціалізуємо функцію для створення кольорів різних тем
    def create_styles(self):
        style = ttk.Style()
        style.theme_use('default')

        # Стилі світлої теми
        style.configure('LightFrame.TFrame', background='white')
        style.configure('LightLabel.TLabel', background='grey', foreground='black')
        style.configure('LightButton.TButton', background='white', foreground='black')
        style.configure('LightEntry.TEntry', background='white', foreground='black')

        # Стилі темної теми
        style.configure('DarkFrame.TFrame', background='gray32')
        style.configure('DarkLabel.TLabel', background='white', foreground='white')
        style.configure('DarkButton.TButton', background='gray32', foreground='white')
        style.configure('DarkEntry.TEntry', background='gray32', foreground='white')

    def create_widgets(self):
        # Ініціалізуємо Фрейм всередині вікна
        self.main_frame = ttk.Frame(self)
        # Робимо так щоб Фрейм займав все вільне місце у вікні та масштабувався відповідно до змін вікна
        self.main_frame.pack(fill='both', expand=True)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Рахуємо висоту текстового поля з інформацією об авторі
        author_info_lines = self._author_info_text.count('\n') + 1
        # Ініціалізуємо інформаційне поле
        self.author_info = tk.Text(self.main_frame, height=author_info_lines, wrap='word', pady=4)
        # Заповнюємо поле текстом
        self.author_info.insert('end', self._author_info_text)
        # Додаємо границю до поля і робимо його read-only
        self.author_info.configure(state='disabled', borderwidth=1, relief='groove')
        # Розмішуємо поле в сітці розмітки, задаємо padding,
        # змушуємо його займати все доступне місце зліва направо
        self.author_info.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='ew')

        # Отримуємо стилі відповідно до обраної теми
        theme_styles = self.themes[self.theme]
        # Ініціалізуємо Фрейм з елементами сценарію та функцію оновлення теми для елементів всередині Фрейму
        self.scenario_frame, self.change_scenario_frame_theme = self.set_scenario_frame(self.main_frame, theme_styles)
        # Задаємо стилі Фрейму
        self.scenario_frame.configure(style=theme_styles['frame'] + '.TFrame', relief='groove', borderwidth=1)
        # Розмішуємо Фрейм в сітці розмітки, задаємо padding,
        # змушуємо його займати все доступне місце зліва направо та згори вниз
        self.scenario_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Додаємо кнопку для зміни кольорової теми
        self.toggle_button = ttk.Button(self.main_frame, text='Toggle Theme', command=self.toggle_theme)
        # Розмішуємо кнопку в сітці розмітки, задаємо padding
        self.toggle_button.grid(row=2, column=0, pady=10)

    # Ініціалізуємо функцію для задання імені вікна
    def set_title(self, title):
        self.title(title)

    # Ініціалізуємо функцію для перемикання кольорової теми
    def toggle_theme(self):
        self.theme = 'light' if self.theme == 'dark' else 'dark'
        self.apply_theme()

    # Ініціалізуємо функцію для застосування стилів кольорової теми для елементів головного вікна
    def apply_theme(self):
        # Дістаємо кольори відповідно до обраної теми
        colors = self.themes[self.theme]
        # Викликаємо функцію зміни стилів вікна сценарію та передаємо їй кольори теми як аргумент
        self.change_scenario_frame_theme(colors)

        # Змінюємо кольори елементів головного вікна
        # Оскільки деякі елементи належать до бібліотеки tk, а деякі - до ttk, їхні стилі змінюються трохи по-різному
        s = ttk.Style()
        s.configure('skeleton.TFrame', background=colors['bg'])
        self.configure(bg=colors['bg'])
        self.main_frame.configure(style='skeleton.TFrame')
        self.author_info.configure(bg=colors['text_bg'], fg=colors['text_fg'])
        self.scenario_frame.configure(style='skeleton.TFrame')

import tkinter as tk
from tkinter import ttk

class ApplicationWindow(tk.Tk):
    def __init__(self, set_scenario_frame, theme='light'):
        super().__init__()
        self.geometry('600x400')  # Default size
        self.themes = {
            'light': {'bg': 'white', 'text_bg': 'white', 'text_fg': 'black', 'frame': 'LightFrame', 'label': 'LightLabel', 'button': 'LightButton', 'entry': 'LightEntry'},
            'dark': {'bg': 'gray32', 'text_bg': 'gray32', 'text_fg': 'white', 'frame': 'DarkFrame', 'label': 'DarkLabel', 'button': 'DarkButton', 'entry': 'DarkEntry'}
        }

        self._author_info_text = ('''Автор програми:
Простаков Олег, КП-02
ФПМ, ПЗКС, НТУУ "КПІ"''')

        self.theme = theme
        self.set_scenario_frame = set_scenario_frame

        self.create_styles()
        self.create_widgets()
        self.apply_theme()

    def create_styles(self):
        style = ttk.Style()
        style.theme_use('default')

        # Light theme styles
        style.configure('LightFrame.TFrame', background='white')
        style.configure('LightLabel.TLabel', background='grey', foreground='black')  # Background for the label
        style.configure('LightButton.TButton', background='white', foreground='black')
        style.configure('LightEntry.TEntry', background='white', foreground='black')

        # Dark theme styles
        style.configure('DarkFrame.TFrame', background='gray32')
        style.configure('DarkLabel.TLabel', background='white', foreground='white')  # Background for the label
        style.configure('DarkButton.TButton', background='gray32', foreground='white')
        style.configure('DarkEntry.TEntry', background='gray32', foreground='white')

    def create_widgets(self):
        # Create a frame within the main window that can expand and fill
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill='both', expand=True)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)  # For the scenario-specific container

        # Calculate the number of lines in the author info text to set the height of the Text widget
        author_info_lines = self._author_info_text.count('\n') + 1

        # Add a text widget for author information, which is read-only
        self.author_info = tk.Text(self.main_frame, height=author_info_lines, wrap='word', pady=4)
        self.author_info.insert('end', self._author_info_text)
        self.author_info.configure(state='disabled', borderwidth=1, relief='groove')
        self.author_info.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='ew')  # Top padding 10, bottom padding 0

        # Create an empty frame to house scenario-specific elements with a thin border
        theme_styles = self.themes[self.theme]
        self.scenario_frame, self.change_scenario_frame_theme = self.set_scenario_frame(self.main_frame, theme_styles)
        self.scenario_frame.configure(style=theme_styles['frame'] + '.TFrame', relief='groove', borderwidth=1)
        self.scenario_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Add a button to toggle the color theme
        self.toggle_button = ttk.Button(self.main_frame, text='Toggle Theme', command=self.toggle_theme)
        self.toggle_button.grid(row=2, column=0, pady=10)

    def set_title(self, title):
        self.title(title)

    def toggle_theme(self):
        self.theme = 'light' if self.theme == 'dark' else 'dark'
        self.apply_theme()

    def apply_theme(self):
        colors = self.themes[self.theme]
        self.change_scenario_frame_theme(colors)
        s = ttk.Style()
        s.configure('skeleton.TFrame', background=colors['bg'])

        self.configure(bg=colors['bg'])
        self.main_frame.configure(style='skeleton.TFrame')
        self.author_info.configure(bg=colors['text_bg'], fg=colors['text_fg'])
        self.scenario_frame.configure(style='skeleton.TFrame')

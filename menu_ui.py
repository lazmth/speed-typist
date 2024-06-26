import tkinter as tk
from tkinter import ttk

from highscores_ui import Highscores
from game_ui import Game


def start_game():
    menu = Menu()
    menu.launch()


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()

        self.bg_colour = "slategrey"

        self.set_window_geometry(300, 300)
        self.title("Speed Typist")
        self.configure(bg=self.bg_colour)

        self.create_title()
        self.create_buttons()

        self.grid_rowconfigure(index=(0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(index=(0,), weight=1)

    def launch(self):
        self.mainloop()

    def set_window_geometry(self, window_width, window_height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = screen_width // 2 - window_width // 2
        y = screen_height // 2 - window_height // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_title(self):
        title = tk.Label(master=self,
                         text="Speed Typist!",
                         bg=self.bg_colour,
                         font=("arial", 20, "bold underline"))
        title.grid(row=0, column=0)
        return title

    def create_buttons(self):
        play_game_btn = self.create_play_game_btn()
        highscores_btn = self.create_highscore_btn()
        quit_btn = self.create_quit_btn()

        play_game_btn.grid(row=1, column=0)
        highscores_btn.grid(row=2, column=0)
        quit_btn.grid(row=3, column=0)

    def create_play_game_btn(self):
        def play_game():
            Game(self)

        return ttk.Button(master=self, text="Play", command=play_game)

    def create_highscore_btn(self):
        def show_highscores():
            Highscores(self)

        return ttk.Button(master=self, text="Highscores", command=show_highscores)

    def create_quit_btn(self):
        def quit_game():
            self.destroy()

        return ttk.Button(master=self, text="Quit", command=quit_game)


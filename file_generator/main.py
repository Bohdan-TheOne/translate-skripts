import tkinter as tk


class Void:
    pass


class FileGeneratorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry()

    def create_components(self):
        self.grid = Void()
        self.grid.heigt = 5
        self.grid.width = 5

        self.l_name = tk.Label(self.root, text='Photoshop File Generator')
        self.l_tname = tk.Label(self.root, text='Template:')
        self.l_template = tk.Label(self.root, text='Not choosen')
        self.b_choose_temlate = tk.Button(self.root, text='Choose',
                                          command=self.change_geometry)

    def draw_components(self):
        self.l_name.grid(row=0, column=0, columnspan=self.grid.width)
        self.l_tname.grid(row=1, column=0)
        self.l_template.grid(row=1, column=1, columnspan=self.grid.width-2)
        self.b_choose_temlate.grid(row=1, column=self.grid.width-1)

    def start(self):
        self.create_components()
        self.draw_components()
        self.root.mainloop()

    def change_geometry(self):
        self.root.geometry('1000x800')


if __name__ == '__main__':
    app = FileGeneratorApp()
    app.start()

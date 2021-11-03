import tkinter as tk
from tkinter.ttk import Progressbar
from shutil import copyfile
from photoshop import Session
from os import mkdir
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename
from pathlib import Path


class Void:
    pass


class FileGeneratorApp(tk.Tk):
    txt = {
        'name': 'Photoshop File Generator',
        'file': 'Template : ',
        'chap': 'Genereate chapters in range : '
    }

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x300')

        self.grid_rowconfigure(0, weight=15)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=10)
        self.grid_rowconfigure(3, weight=500)
        self.grid_columnconfigure(0, weight=20)
        self.grid_columnconfigure(1, weight=20)
        self.grid_columnconfigure(2, weight=20)
        self.grid_columnconfigure(3, weight=20)
        self.grid_columnconfigure(4, weight=20)

        self.create_components()
        self.draw_components()

        self.istset = False
        self.ischset = False

    def create_components(self):
        self.griding = Void()
        self.griding.heigt = 5
        self.griding.width = 4

        self.l_name = tk.Label(self, text=self.txt['name'],
                               font=("Arial", 22, "bold"))
        self.l_tname = tk.Label(self, text=self.txt['file'],
                                font=("Arial", 14))
        self.e_template = tk.Entry(self, width=50)
        self.b_choose_temlate = tk.Button(self, text='Choose', command=self.set_template,
                                          font=("Arial", 10), width=13)

        self.l_chapters = tk.Label(self, text=self.txt['chap'],
                                   font=("Arial", 14))
        self.e_ch_start = tk.Entry(self, font=("Arial", 10), width=15)
        self.e_ch_end = tk.Entry(self, font=("Arial", 10), width=15)
        self.b_set_chapters = tk.Button(self, text='Preset', command=self.add_rows,
                                        font=("Arial", 10), width=13)

        self.f_gen = tk.Frame(self, pady=10)

        self.b_generate = tk.Button(self, text='Generate', command=self.start_generation,
                                    font=("Arial", 10), width=13, state=tk.DISABLED)

    def draw_components(self):
        self.l_name          .grid(row=0, column=0, columnspan=5)
        self.l_tname         .grid(row=1, column=0, sticky=tk.W)
        self.e_template      .grid(row=1, column=1, columnspan=3)
        self.b_choose_temlate.grid(row=1, column=4, sticky=tk.E)

        self.l_chapters.grid(row=2, column=0, columnspan=2, sticky=tk.W)
        self.e_ch_start.grid(row=2, column=2)
        self.e_ch_end  .grid(row=2, column=3, sticky=tk.E)
        self.b_set_chapters.grid(row=2, column=4, sticky=tk.E)

        self.f_gen.grid(row=3, column=0, columnspan=5)
        self.b_generate.grid(row=4, column=4)

    def set_template(self):
        filename = Path(askopenfilename())
        try:
            self.template_ref = filename.relative_to(Path.cwd())
        except ValueError:
            self.template_ref = filename

        self.e_template.delete(0, tk.END)
        self.e_template.insert(0, self.template_ref)

        self.istset = True
        if self.ischset:
            self.b_generate['state'] = tk.NORMAL

    def add_rows(self):
        try:
            self.chap.destroy()
        except:
            pass
        self.chap = tk.Frame(self.f_gen)
        self.chap.pack()

        try:
            start = int(self.e_ch_start.get())
            end = int(self.e_ch_end.get())
        except ValueError:
            raise ValueError('Write proper values for start and end')

        self.chapters = []
        for i in range(end - start + 1):
            row = Void()
            row.id = i + start
            row.label = tk.Label(self.chap, text=f'chapter {start + i}')
            row.label.grid(row=i, column=0, padx=5)
            row.entry = tk.Entry(self.chap)
            row.entry.grid(row=i, column=1, padx=15)
            row.progress = Progressbar(self.chap, orient=tk.HORIZONTAL,
                                       length=300, mode='determinate')
            row.progress.grid(row=i, column=2)
            self.chapters.append(row)

        self.ischset = True
        if self.istset:
            self.b_generate['state'] = tk.NORMAL

    def start_generation(self):
        try:
            chapters = [(ch.id, int(ch.entry.get())) for ch in self.chapters]
        except ValueError:
            raise ValueError("Not all page numbers are filled coorectly")

        for k, (ch, pgnum) in enumerate(chapters):
            try:
                mkdir(f'{ch:03}')
            except FileExistsError:
                pass

            for pg in range(1, pgnum, 5):
                progress = 100 // pgnum

                expg = pg + 4 if pg + 4 <= pgnum else pgnum
                new_file_name = f'{ch:03}/Aot-{ch:03}-st({pg:02}-{expg:02}).psd'
                copyfile(self.template_ref, new_file_name)
                new_file_name = str(Path(new_file_name).resolve())

                with Session(new_file_name, action="open") as ps:
                    for i, num in enumerate(range(pg, expg+1)):
                        ps.active_document.layers[i].name = f'{num:02}'
                        self.chapters[k].progress['value'] += progress
                        self.update_idletasks()
                    ps.active_document.saveAs(new_file_name,
                                              ps.PhotoshopSaveOptions(), True)
                    ps.active_document.close()

                self.chapters[k].progress['value'] = 100
                self.update_idletasks()

    def report_callback_exception(self, exc, val, tb):
        showerror("Error", message=str(val))


if __name__ == '__main__':
    app = FileGeneratorApp()
    app.mainloop()

import tkinter as tk
from ttkbootstrap import Style  # Importiere Style aus ttkbootstrap
from ttkbootstrap import ttk  # Importiere ttk aus ttkbootstrap

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.style = Style(theme='litera')  # Erstelle Style nach Tk Objekt
        self.root.geometry('300x300')
        self.root.title('Taschenrechner')
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.lZahl1 = ttk.Label(self.root, text='Zahl 1:')
        self.lZahl1.place(x=8, y=13)
        
        self.entry1 = ttk.Entry(self.root)
        self.entry1.place(x=96, y=8)
        
        self.lZahl2 = ttk.Label(self.root, text='Zahl 2:')
        self.lZahl2.place(x=8, y=45)
        
        self.entry2 = ttk.Entry(self.root)
        self.entry2.place(x=96, y=40)
        
        self.radiobuttonGroup1 = ttk.LabelFrame(self.root, text='Rechenoperation')
        self.radiobuttonGroup1.place(x=8, y=72, width=288, height=100)
        
        self.operation = tk.StringVar()
        self.operation.set('Addition')
        
        ttk.Radiobutton(self.radiobuttonGroup1, text='Addition', variable=self.operation, value='Addition').place(x=8, y=4)
        ttk.Radiobutton(self.radiobuttonGroup1, text='Subtraktion', variable=self.operation, value='Subtraktion').place(x=8, y=28)
        ttk.Radiobutton(self.radiobuttonGroup1, text='Multiplikation', variable=self.operation, value='Multiplikation').place(x=8, y=52)
        ttk.Radiobutton(self.radiobuttonGroup1, text='Division', variable=self.operation, value='Division').place(x=144, y=4)
        ttk.Radiobutton(self.radiobuttonGroup1, text='Potenz', variable=self.operation, value='Potenz').place(x=144, y=28)
        ttk.Radiobutton(self.radiobuttonGroup1, text='Modulo', variable=self.operation, value='Modulo').place(x=144, y=52)
        
        self.bBerechnen = ttk.Button(self.root, text='Berechnen', style='primary')
        self.bBerechnen.place(x=8, y=190)
        self.bBerechnen['command'] = self.bBerechnen_Command
        
        self.lErgebnis = ttk.Label(self.root, text='Ergebnis:')
        self.lErgebnis.place(x=8, y=245)
        
        self.entry3 = ttk.Entry(self.root)
        self.entry3.place(x=96, y=240)

    def bBerechnen_Command(self):
        zahl1 = float(self.entry1.get())
        zahl2 = float(self.entry2.get())
        operation = self.operation.get()

        if operation == 'Addition':
            result = zahl1 + zahl2
        elif operation == 'Subtraktion':
            result = zahl1 - zahl2
        elif operation == 'Multiplikation':
            result = zahl1 * zahl2
        elif operation == 'Division':
            result = zahl1 / zahl2 if zahl2 != 0 else "Cannot divide by zero"
        elif operation == 'Potenz':
            result = zahl1 ** zahl2
        elif operation == 'Modulo':
            result = zahl1 % zahl2 if zahl2 != 0 else "Cannot modulo by zero"
        
        self.entry3.delete(0, tk.END)
        self.entry3.insert(0, str(result))

if __name__ == "__main__":
    App()
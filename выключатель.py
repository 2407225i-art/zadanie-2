import tkinter as tk

class LightSwitch:
    def __init__(self, root):
        self.root = root
        self.root.title("Выключатель света")
        self.root.geometry("300x400")
        self.root.configure(bg='black')
        
        # Состояние света
        self.light_on = False
        
        # Индикатор
        self.indicator = tk.Canvas(root, width=200, height=200, bg='black', highlightthickness=0)
        self.indicator.pack(pady=50)
        
        # Рисуем выключенную лампочку
        self.draw_light(False)
        
        # Кнопка
        self.button = tk.Button(
            root,
            text="ВКЛЮЧИТЬ",
            font=('Arial', 14, 'bold'),
            bg='#444',
            fg='white',
            activebackground='#666',
            activeforeground='white',
            relief='flat',
            width=15,
            height=2,
            command=self.toggle
        )
        self.button.pack()
        
        # Статус
        self.status = tk.Label(
            root,
            text="Свет: ВЫКЛЮЧЕН",
            font=('Arial', 12),
            fg='white',
            bg='black'
        )
        self.status.pack(pady=20)
    
    def draw_light(self, on):
        self.indicator.delete("all")
        
        if on:
            # Свечение
            for i in range(5, 0, -1):
                size = 80 + i * 10
                alpha = 50 - i * 10
                color = f'#{255:02x}{255:02x}{150:02x}'
                self.indicator.create_oval(
                    100 - size//2, 100 - size//2,
                    100 + size//2, 100 + size//2,
                    fill=color, outline=''
                )
            
            # Лампочка включена
            self.indicator.create_oval(50, 50, 150, 150, fill='yellow', outline='gold', width=2)
            self.indicator.create_line(100, 70, 100, 130, fill='orange', width=3)
            self.indicator.create_rectangle(90, 150, 110, 170, fill='gray', outline='darkgray')
        else:
            # Лампочка выключена
            self.indicator.create_oval(50, 50, 150, 150, fill='gray', outline='darkgray', width=2)
            self.indicator.create_line(100, 70, 100, 130, fill='darkgray', width=3)
            self.indicator.create_rectangle(90, 150, 110, 170, fill='darkgray', outline='black')
    
    def toggle(self):
        self.light_on = not self.light_on
        
        if self.light_on:
            self.draw_light(True)
            self.button.configure(text="ВЫКЛЮЧИТЬ", bg='#cc3300')
            self.status.configure(text="Свет: ВКЛЮЧЕН", fg='yellow')
            self.root.configure(bg='#111')
        else:
            self.draw_light(False)
            self.button.configure(text="ВКЛЮЧИТЬ", bg='#444')
            self.status.configure(text="Свет: ВЫКЛЮЧЕН", fg='white')
            self.root.configure(bg='black')

# Запуск
if __name__ == "__main__":
    root = tk.Tk()
    app = LightSwitch(root)
    root.mainloop()
import tkinter as tk
from tkinter import ttk

class SimpleLightControl:
    def __init__(self, root):
        self.root = root
        self.root.title("Яркость света")
        self.root.geometry("300x200")
        
        # Сделаем окно всегда поверх других
        self.root.attributes('-topmost', True)
        
        # Запретим изменение размера
        self.root.resizable(False, False)
        
        # Темная тема
        self.root.configure(bg='#1a1a1a')
        
        # Создаем виджеты
        self.create_widgets()
        
    def create_widgets(self):
        # Заголовок
        title_label = tk.Label(
            self.root, 
            text="🔆 Регулятор яркости",
            font=("Arial", 16, "bold"),
            bg='#1a1a1a',
            fg='white'
        )
        title_label.pack(pady=(20, 10))
        
        # Большой процент яркости
        self.brightness_label = tk.Label(
            self.root,
            text="50%",
            font=("Arial", 48, "bold"),
            bg='#1a1a1a',
            fg='white'
        )
        self.brightness_label.pack(pady=10)
        
        # Ползунок
        self.slider = ttk.Scale(
            self.root,
            from_=0,
            to=100,
            orient='horizontal',
            length=250,
            command=self.update_brightness
        )
        self.slider.set(50)  # Начальное значение
        self.slider.pack(pady=10)
        
        # Стилизуем ползунок
        style = ttk.Style()
        style.configure(
            "TScale",
            background='#1a1a1a',
            troughcolor='#333333',
            sliderlength=30
        )
        
        # Кнопка выключения
        off_button = tk.Button(
            self.root,
            text="Выключить свет",
            font=("Arial", 10),
            bg='#ff4444',
            fg='white',
            relief='flat',
            command=self.turn_off
        )
        off_button.pack(pady=10)
        
    def update_brightness(self, value):
        """Обновление яркости при движении ползунка"""
        brightness = int(float(value))
        self.brightness_label.config(text=f"{brightness}%")
        
        # Можно добавить логику для реального управления светом
        print(f"Установлена яркость: {brightness}%")
    
    def turn_off(self):
        """Выключение света"""
        self.slider.set(0)
        self.brightness_label.config(text="0%")
        print("Свет выключен")

def main():
    root = tk.Tk()
    app = SimpleLightControl(root)
    root.mainloop()

if __name__ == "__main__":
    main()
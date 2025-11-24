import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()
root.title("Каганер Артем Денисович")
root.geometry("500x350")

notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Калькулятор")

tk.Label(tab1, text="Число 1:").pack(pady=5)
entry1 = tk.Entry(tab1)
entry1.pack()

tk.Label(tab1, text="Операция:").pack(pady=5)
op = ttk.Combobox(tab1, values=["+", "-", "*", "/"], state="readonly")
op.pack()
op.current(0)

tk.Label(tab1, text="Число 2:").pack(pady=5)
entry2 = tk.Entry(tab1)
entry2.pack()

result_label = tk.Label(tab1, text="", fg="blue", font=("Arial", 12))

def calc():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        if op.get() == "+": res = n1 + n2
        elif op.get() == "-": res = n1 - n2
        elif op.get() == "*": res = n1 * n2
        elif op.get() == "/": res = n1 / n2 if n2 != 0 else "Ошибка"
        result_label.config(text=f"Результат: {res}")
    except:
        result_label.config(text="Ошибка ввода")

tk.Button(tab1, text="=", command=calc).pack(pady=10)
result_label.pack()

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Чекбоксы")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

tk.Checkbutton(tab2, text="Первый", variable=var1).pack(anchor="w", padx=20, pady=5)
tk.Checkbutton(tab2, text="Второй", variable=var2).pack(anchor="w", padx=20, pady=5)
tk.Checkbutton(tab2, text="Третий", variable=var3).pack(anchor="w", padx=20, pady=5)

def show_choice():
    selected = []
    if var1.get(): selected.append("Первый")
    if var2.get(): selected.append("Второй")
    if var3.get(): selected.append("Третий")
    msg = f"Вы выбрали: {', '.join(selected)}" if selected else "Ничего не выбрано"
    messagebox.showinfo("Выбор", msg)

tk.Button(tab2, text="Показать", command=show_choice).pack(pady=20)

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Текст")

text_area = tk.Text(tab3, height=12, width=50)
text_area.pack(padx=10, pady=10)

def load():
    file = filedialog.askopenfilename(filetypes=[("Text", "*.txt"), ("All", "*.*")])
    if file:
        with open(file, 'r', encoding='utf-8') as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, f.read())

tk.Button(tab3, text="Загрузить файл", command=load).pack(pady=5)
tk.Button(tab3, text="Очистить", command=lambda: text_area.delete(1.0, tk.END)).pack(pady=5)

root.mainloop()

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# по інакшому не працює
data = pd.read_csv('D:/python VS/python_programming/MODULE/Module_/module.csv')
print(data)

def add_book():
    name = entry_name.get()
    author = entry_author.get()
    year = entry_year.get()
    janre = entry_janre.get()
    count = entry_count.get()

    try:
        year = int(year)
        count = int(count)
        data.loc[len(data)] = [name, author, year, janre, count]
        messagebox.showinfo( f"Книгу '{name}' додано!")
        update_data()
    except ValueError:
        messagebox.showerror("Помилка")
def redact_book():
    name = entry_name.get()
    count = entry_count.get()

    try:
        count = int(count)
        if name in data['Назва'].values:
            data.loc[data['Назва'] == name, 'Кількість примірників'] = count
            messagebox.showinfo("Успіх", f"Кількість '{name}' змінена на {count}")
            update_data()
        else:
            messagebox.showerror("Помилка", f"Книга '{name}' не знайдена.")
    except ValueError:
        messagebox.showerror("Помилка")

def delete_item():
    name = entry_name.get()
    if name in data['Назва'].values:
        data.drop(data[data['Назва'] == name].index, inplace=True)
        messagebox.showinfo("Успіх", f"Книгу '{name}' видалено!")
        update_data()
    else:
        messagebox.showerror("Помилка", f"Книга '{name}' не знайдена.")

def update_data():
    text_data.delete(1.0, tk.END)
    text_data.insert(tk.END, data.to_string(index=False))

def calculate():
    total_count = data['Кількість примірників'].sum()
    messagebox.showinfo("Результат", f"Загальна кількість книг: {total_count}")

def most_popular_janres():
    janre_counts = data['Жанр'].value_counts()
    most_popular_janre = janre_counts.idxmax()
    messagebox.showinfo("Результат", f"Найпопулярніший жанр: {most_popular_janre}")

def circe_graph():
    janre_counts = data.groupby('Жанр')['Кількість примірників'].sum()
    plt.pie(janre_counts, labels=janre_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Розподіл книг за жанрами')
    plt.show()

def bar_graph():
    year_counts = data.groupby('Рік видання')['Кількість примірників'].sum()
    year_counts.plot(kind='bar', color='blue')
    plt.xlabel('Рік видання')
    plt.ylabel('Кількість примірників')
    plt.title('Гістограма за роками видання')
    plt.show()

root = tk.Tk()
root.title("Управління книгами")

label_name = tk.Label(root, text="Назва книги:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_author = tk.Label(root, text="Автор:")
label_author.pack()

entry_author = tk.Entry(root)
entry_author.pack()

label_year = tk.Label(root, text="Рік видання:")
label_year.pack()

entry_year = tk.Entry(root)
entry_year.pack()

label_janre = tk.Label(root, text="Жанр:")
label_janre.pack()

entry_janre = tk.Entry(root)
entry_janre.pack()

label_count = tk.Label(root, text="Кількість примірників:")
label_count.pack()

entry_count = tk.Entry(root)
entry_count.pack()

button1 = tk.Button(root, text='Обчислити загальну кількість книг', command=calculate)
button1.pack()

button2 = tk.Button(root, text='Найпопулярніший жанр', command=most_popular_janres)
button2.pack()

button_add = tk.Button(root, text="Додати книгу", command=add_book)
button_add.pack()

button_redact = tk.Button(root, text="Змінити кількість книг", command=redact_book)
button_redact.pack()

button_delete = tk.Button(root, text="Видалити книгу", command=delete_item)
button_delete.pack()

button_graph1 = tk.Button(root, text='Розподіл книг за жанрами', command=circe_graph)
button_graph1.pack()

button_graph2 = tk.Button(root, text='Гістограма за роками видання', command=bar_graph)
button_graph2.pack()

text_data = tk.Text(root, height=10, width=100)
text_data.pack()

update_data()

root.mainloop()

import json
import requests
from tkinter import *
def start():
    s = txt.get()
    url = f"https://api.github.com/users/{s}"
    repository_url = requests.get(url).json()
    try:
        repository_url['company']
        repository_url['email']
    except KeyError:
        repository_url['company'] = None
        repository_url['email'] = None
    with open("vivod.txt", "a+") as f:
        f.write(f"'company': '{repository_url['company']}'\n")
        f.write(f"'created_at': '{repository_url['created_at']}'\n")
        f.write(f"'email': '{repository_url['email']}'\n")
        f.write(f"'id': '{repository_url['id']}'\n")
        f.write(f"'name': '{repository_url['name']}'\n")
        f.write(f"'url': '{repository_url['url']}'\n")
        f.write("\n")
window = Tk()
window.title('json')
window.geometry('500x200')
lbl = Label(window, text='Введите имя репозитория')
lbl.grid(padx=50, pady=20)
txt = Entry(window, width=30)
txt.grid(padx=170, pady=0)
btn = Button(window, text = "Нажать", command=start)
btn.grid(padx=100, pady=10)
window.mainloop()

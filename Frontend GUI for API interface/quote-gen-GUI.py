import tkinter as tk
import requests
import json

def generate_quote():
    response = requests.get('http://127.0.0.1:8080/generate/' + e1.get() + '&' + str(w1.get()) + '&' + e2.get()).text
    data = json.loads(response)
    text_out.delete('1.0', 'end')
    for n in range(len(data['data'])):
        text_out.insert('end', data['data'][n] + '\n\n\n')

master = tk.Tk()
temp = tk.DoubleVar()

tk.Label(master, text="Length").grid(row=0)
tk.Label(master, text="Number of Quotes").grid(row=1)
tk.Label(master, text="Temperature").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
w1 = tk.Scale(master, from_=0.7, to=1.0, resolution=0.01, orient='horizontal', variable=temp)
w1.set(0.85)
button = tk.Button(master, text='Generate', width=25, command=generate_quote)
text_out = tk.Text(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
w1.grid(row=2, column=1)
button.grid(row=3)
text_out.grid(row=3, column=1)

master.mainloop()
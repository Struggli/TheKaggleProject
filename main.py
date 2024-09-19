# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import kaggle
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk

kaggle.api.authenticate()
kaggle.api.dataset_download_files('aungpyaeap/supermarket-sales', path=".", unzip=True)


def searchCustomersFromCity(event=NONE):
    meters.set(len(df1[(df1['City'] == str(cityName.get())) & (df1['Gender'] == str(genderType.get()))]))


city = "Yangon"
gender = "Male"
df1 = pd.read_csv('supermarket_sales - Sheet1.csv', delimiter=",")
df1 = df1[['Invoice ID', 'City', 'Gender', 'Total']]
df1.dropna()
options = df1['City'].unique().tolist()
genders = df1['Gender'].unique().tolist()
# Simple UI to interact with table
root = Tk()
root.title("Data filter")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

cityName = StringVar()
cityName.set(options[0])
cityName_entry = ttk.OptionMenu(mainframe, cityName, options[0], *options)
cityName_entry.grid(column=2, row=1, sticky=(W, E))

genderType = StringVar()
genderType_entry = ttk.OptionMenu(mainframe, genderType,genders[0],*genders)
genderType_entry.grid(column=2, row=2, sticky=(W, E))
meters = StringVar()
meter_entry = ttk.Entry(mainframe, textvariable=meters).grid(column=3, row=3, sticky=W)

ttk.Button(mainframe, text="Find", command=searchCustomersFromCity).grid(column=4, row=4, sticky=W)

ttk.Label(mainframe, text="City").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Gender").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Customers:").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", searchCustomersFromCity)

root.mainloop()

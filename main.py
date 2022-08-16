import requests
from tkinter import *

def Erase_All():
  amont_curr1.delete(0, END)
  lbl5.configure(text='')

def Curr_Conv():
  currency1=var1.get()
  currency2=var2.get()
  n=float(amont_curr1.get())
  url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency2}&from={currency1}&amount={n}"
  payload = {}
  headers= {
    "apikey": "FQFiHpuq6S8yh8LHvDMEEE23Tlv2rF0b"
  }
  response = requests.request("GET", url, headers=headers, data = payload)
  result=response.json()
  lbl5.configure(text=f"{n}{currency2}={round(result['result'],2)}{currency1}")

wnd = Tk()
wnd.geometry('800x400')
wnd.title('Currency converter')

hdlbl=Label(wnd, text='Currency converter',font=('Vernada',18))
hdlbl.grid(column=0, row=0)

dummy1=Label(wnd)
dummy1.grid(row=1, column=0)

var1=StringVar(wnd)
var2=StringVar(wnd)
var1.set('Выберите валюту')
var2.set('Выберите валюту')

Curr_list = ['RUB','USD','EUR','JPY','AUD','CAD','CHF','GBP','KZT']

lbl1=Label(wnd, text='Исходная валюта:', font=('Vernada',13))
lbl1.grid(column=0, row=2)
Curr1=OptionMenu(wnd, var1, *Curr_list)
Curr1.grid(row=2, column=1, ipadx=10)

dummy2 = Label(wnd)
dummy2.grid(row=3, column=0)

lbl2 = Label(wnd, text='Конечная валюта:', font=('Vernada',13))
lbl2.grid(column=0, row=4)
Curr2=OptionMenu(wnd, var2, *Curr_list)
Curr2.grid(row=4, column=1, ipadx=10)

dummy3 = Label(wnd)
dummy3.grid(row=5, column=0)

lbl3 = Label(wnd, text='Количество единиц исходной валюты:', font=('Vernada',13))
lbl3.grid(column=0, row=6)
amont_curr1 = Entry(wnd)
amont_curr1.grid(row=6, column=1)

dummy4 = Label(wnd)
dummy4.grid(row=7, column=0)

btn1 = Button(wnd, text='Конвертировать!', width='30', height='2', bg='light green', command=Curr_Conv)
btn1.grid(row=8,column=1)

dummy5 = Label(wnd)
dummy5.grid(row=9, column=0)

lbl4 = Label(wnd, text='Результат конвертации:', font=('Vernada',13))
lbl4.grid(column=0, row=10)

lbl5 = Label(wnd, font=('Vernada',13))
lbl5.grid(column=1, row=10)

dummy6 = Label(wnd)
dummy6.grid(row=11, column=0)

btn2 = Button(wnd, text='Очистить', width='30', height='2', bg='light blue', command=Erase_All)
btn2.grid(row=12,column=1)

wnd.mainloop()

# import requests

# url = "https://api.apilayer.com/exchangerates_data/symbols"

# payload = {}
# headers= {
#   "apikey": "FQFiHpuq6S8yh8LHvDMEEE23Tlv2rF0b"
# }

# response = requests.request("GET", url, headers=headers, data = payload)

# status_code = response.status_code
# result = response.text
# print(result)

# import json 
# import requests

# url = "https://api.apilayer.com/exchangerates_data/convert?to=rub&from=usd&amount=1"

# payload = {}
# headers= {
#   "apikey": "FQFiHpuq6S8yh8LHvDMEEE23Tlv2rF0b"
# }

# response = requests.request("GET", url, headers=headers, data = payload)

# status_code = response.status_code
# result = response.text
# print(result)
# res=result.json()
# res=float(res['result'])
# print(res)

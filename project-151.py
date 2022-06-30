from tkinter import *
import random

root=Tk()
root.title("sales application")
root.geometry("700x500")

label_month = Label(root)
label_profit = Label(root)
label_max_profit = Label(root)
label_min_profit = Label(root)

month = ("January","February","March","April","May","June","July","August","September","October","November","December")

profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

label_month["text"]="months are :"+str(month)
label_profit["text"]="profits :"+str(profits)

def max_profits():
    max_profits = max(profits)
    index_max = profits.index(max_profits)
    month_max = month[index_max]
    label_max_profit["text"]="The maximum profit was made in the month of: "+month_max+" and it was "+str(max_profits)

def min_profits():
    min_profits = min(profits)
    index_min = profits.index(min_profits)
    month_min = month[index_min]
    label_min_profit["text"]="The minimum profit was made in the month of: "+month_min+" and it was "+str(min_profits)

label_month.place(relx=0.5,rely=0.2, anchor=CENTER)
label_profit.place(relx=0.5,rely=0.3, anchor=CENTER)

btn_max = Button(root,text="Show max Profit Every Month",command=max_profits)
btn_max.place(relx=0.5,rely=0.4, anchor=CENTER)

label_max_profit.place(relx=0.5,rely=0.5, anchor=CENTER)


btn_min = Button(root,text="Show min Profit Every Month",command=min_profits)
btn_min.place(relx=0.5,rely=0.6, anchor=CENTER)


label_min_profit.place(relx=0.5,rely=0.7, anchor=CENTER)









root.mainloop()
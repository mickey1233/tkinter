import os
import tkinter as tk
from tkinter import ttk #ttk包含tkinter, 較美觀的視窗
import tkinter.filedialog as fd
global mywin

def select_file():
    global file_names #儲存所有選擇的檔案(包含路徑)
    file_names=fd.askopenfilenames(initialdir='d:\\',filetypes=[('excel , csv files','*.xlsx *.xls *.csv'),('excel files','*.xlsx *.xls'),('csv files','*.csv'),('All files','*.*')])
    print("files selected is:",file_names)
    mywin.destroy()
    
#def close():
#    mywin.destroy()

mywin=tk.Tk()
mywin.title("Select Files")
mywin.geometry("300x100+1400+100") #視窗大小及x(1400),y(100)位置
mywin.resizable(0,0) #視窗不可拖曳變更大小
    
s=ttk.Style()
s.configure("btn.TButton",font=("標楷體",24),foreground="slategrey") #設定button樣式
btn1_select=ttk.Button(mywin,text="請選擇目錄及檔案",style="btn.TButton",command=select_file) #按此button會呼叫select_file()
btn1_select.pack(fill='both',expand=True) #button定位方式(擴充填滿整個視窗)
#btn1_select.grid(row=0,column=0,ipadx=55,ipady=55) #button另一種定位方式
#btn2_exit=ttk.Button(mywin,text="關閉視窗",style="btn.TButton",command=close)
#btn2_exit.grid(row=0,column=1,ipadx=55,ipady=55)
#btn2_exit.pack(fill='both',expand=True)
mywin.mainloop()

dict={} #用dictionary儲存所有主檔名及副檔名
for files in file_names:
    route=os.path.split(files) #將檔案分割為路徑及檔名, result[0] 為路徑, result[1]為檔名
    name_extention=os.path.splitext(route[1]) #將檔名分割為主檔名及副檔名, name_extention[0]為主檔名, name_extention[1]為副檔名
    dict[name_extention[0]]=name_extention[1] #將主檔名及副檔名加入dictionary
print(dict)


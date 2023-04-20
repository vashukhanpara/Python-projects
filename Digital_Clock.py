from re import I
from tkinter import *    
import datetime


def date_time():
    time = datetime.datetime.now()
    hr=time.strftime('%I')   
    min=time.strftime('%M')  
    sec=time.strftime('%S')  
    ampm=time.strftime('%p') 
    date=time.strftime('%d')  
    month=time.strftime('%m') 
    year=time.strftime('%y')  
    day=time.strftime('%a')   


    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_ampm.config(text=ampm)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

 
    lab_hr.after(200,date_time)




clock = Tk()
clock.title('Digital clock')
clock.geometry('1000x500')
clock.config(bg='yellow')


#HOUR(1ST ROW)
lab_hr=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')
lab_hr.place(x=120,y=40,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_hr_txt=Label(clock,text='HOUR' , font=('times new roman',25,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6
lab_hr_txt.place(x=120,y=180,height=40,width=100)



#MINUTE(1ST ROW)
lab_min=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')
lab_min.place(x=340,y=40,height=110,width=100)
#(2ND ROW)
lab_min_txt=Label(clock,text='MIN.' , font=('times new roman',25,'bold'),bg='red',fg='white')
lab_min_txt.place(x=340,y=180,height=40,width=100)



#SECOND(1ST ROW)
lab_sec=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')
lab_sec.place(x=560,y=40,height=110,width=100)
#(2ND ROW)
lab_sec_txt=Label(clock,text='SEC.' , font=('times new roman',25,'bold'),bg='red',fg='white')
lab_sec_txt.place(x=560,y=180,height=40,width=100)



#AM/PM(1ST ROW)
lab_ampm=Label(clock,text='00' , font=('times new roman',50,'bold'),bg='red',fg='white')
lab_ampm.place(x=780,y=40,height=110,width=100)
#(2ND ROW)
lab_ampm_txt=Label(clock,text='AM/PM' , font=('times new roman',21,'bold'),bg='red',fg='white')
lab_ampm_txt.place(x=780,y=180,height=40,width=100) 















#DATE(1ST ROW)
lab_date=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')
lab_date.place(x=120,y=280,height=110,width=100)
#(2ND ROW)
lab_date_txt=Label(clock,text='DATE' , font=('times new roman',25,'bold'),bg='red',fg='white')
lab_date_txt.place(x=120,y=420,height=40,width=100)


#MONTH(1ST ROW)
lab_month=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')
lab_month.place(x=340,y=280,height=110,width=100)
#(2ND ROW)
lab_month_txt=Label(clock,text='MONTH' , font=('times new roman',17,'bold'),bg='red',fg='white')
lab_month_txt.place(x=340,y=420,height=40,width=100)


#YEAR(1ST ROW)
lab_year=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')
lab_year.place(x=560,y=280,height=110,width=100)
#(2ND ROW)
lab_year_txt=Label(clock,text='YEAR' , font=('times new roman',25,'bold'),bg='red',fg='white')
lab_year_txt.place(x=560,y=420,height=40,width=100)


#DAY(1ST ROW)
lab_day=Label(clock,text='00' , font=('times new roman',45,'bold'),bg='red',fg='white')
lab_day.place(x=780,y=280,height=110,width=100)
#(2ND ROW)
lab_day_txt=Label(clock,text='DAY' , font=('times new roman',25,'bold'),bg='red',fg='white')
lab_day_txt.place(x=780,y=420,height=40,width=100)




date_time()


clock.mainloop()

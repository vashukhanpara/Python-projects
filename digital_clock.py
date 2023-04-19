from re import I
from tkinter import *     #ahiya from tkinter import * etla mate lakhyu 6 k varmvar apde tkinter lakvu na pade and e badha modulo and method autometic call karide
import datetime

# print(datetime.datetime.now())#current time batave


def date_time():
    time = datetime.datetime.now()
    hr=time.strftime('%I')# ano mean k badha tipinkme mathi khali hour j le    ,    ahiya hr e new variable banavyo 6 and e variable function ma 6 have jya sudhi e function ma banavela variable ne call na karvama ave tya sudhi eno color dark re and call kari lidha pa6i color light thai jai
    min=time.strftime('%M')# ano mean k badha time mathi khali minute j le    ,    ahiya min e new variable banavyo 6 and e variable function ma 6 have jya sudhi e function ma banavela variable ne call na karvama ave tya sudhi eno color dark re and call kari lidha pa6i color light thai jai
    sec=time.strftime('%S')# ano mean k badha time mathi khali second j le    ,    ahiya sec e new variable banavyo 6 and e variable function ma 6 have jya sudhi e function ma banavela variable ne call na karvama ave tya sudhi eno color dark re and call kari lidha pa6i color light thai jai
    ampm=time.strftime('%p')# ano mean k badha time mathi khali ampm j le ama p small avse    ,    ahiya ampm e new variable banavyo 6 and e variable function ma 6 have jya sudhi e function ma banavela variable ne call na karvama ave tya sudhi eno color dark re and call kari lidha pa6i color light thai jai
    date=time.strftime('%d')# ano mean k badha time mathi khali date j le ama d small avse
    month=time.strftime('%m')# ano mean k badha time mathi khali month j le ama m small avse
    year=time.strftime('%y')# ano mean k badha time mathi khali year j le ama y small avse
    day=time.strftime('%a')# ano mean k badha time mathi khali day j le ama a small avse


    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_ampm.config(text=ampm)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    # ahiya sudhi data save thai gaya but jo niche no program na lakhie to everytime change na thai
    lab_hr.after(200,date_time)# ahiya lab_hr.after() nu work e 6 k every second ma j graphic banavyu 6 tene change kare (200 no meaning k every 200 milisecond ni andar hour na data change thava joie    ,    date_time no meaning k date_time module change karse em)




clock = Tk()#tk class no call karyo 6
clock.title('Digital clock')
clock.geometry('1000x500')
clock.config(bg='yellow')


#HOUR(1ST ROW)
lab_hr=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6    ,    fg etle color of text tema color nu name pan lakhi sakie and color code pan lakhi sakie
lab_hr.place(x=120,y=40,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_hr_txt=Label(clock,text='HOUR' , font=('times new roman',25,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6
lab_hr_txt.place(x=120,y=180,height=40,width=100)#x refers to verticle position and y refers to horizontal position 



#MINUTE(1ST ROW)
lab_min=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')
lab_min.place(x=340,y=40,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_min_txt=Label(clock,text='MIN.' , font=('times new roman',25,'bold'),bg='red',fg='white')
lab_min_txt.place(x=340,y=180,height=40,width=100)#x refers to verticle position and y refers to horizontal position 



#SECOND(1ST ROW)
lab_sec=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')
lab_sec.place(x=560,y=40,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_sec_txt=Label(clock,text='SEC.' , font=('times new roman',25,'bold'),bg='red',fg='white')
lab_sec_txt.place(x=560,y=180,height=40,width=100)#x refers to verticle position and y refers to horizontal position 



#AM/PM(1ST ROW)
lab_ampm=Label(clock,text='00' , font=('times new roman',50,'bold'),bg='red',fg='white')
lab_ampm.place(x=780,y=40,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_ampm_txt=Label(clock,text='AM/PM' , font=('times new roman',21,'bold'),bg='red',fg='white')
lab_ampm_txt.place(x=780,y=180,height=40,width=100)#x refers to verticle position and y refers to horizontal position 















#DATE(1ST ROW)
lab_date=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6    ,    fg etle color of text
lab_date.place(x=120,y=280,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_date_txt=Label(clock,text='DATE' , font=('times new roman',25,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6
lab_date_txt.place(x=120,y=420,height=40,width=100)#x refers to verticle position and y refers to horizontal position 


#MONTH(1ST ROW)
lab_month=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6    ,    fg etle color of text
lab_month.place(x=340,y=280,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_month_txt=Label(clock,text='MONTH' , font=('times new roman',17,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6
lab_month_txt.place(x=340,y=420,height=40,width=100)#x refers to verticle position and y refers to horizontal position 


#YEAR(1ST ROW)
lab_year=Label(clock,text='00' , font=('times new roman',60,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6    ,    fg etle color of text
lab_year.place(x=560,y=280,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_year_txt=Label(clock,text='YEAR' , font=('times new roman',25,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6
lab_year_txt.place(x=560,y=420,height=40,width=100)#x refers to verticle position and y refers to horizontal position 


#DAY(1ST ROW)
lab_day=Label(clock,text='00' , font=('times new roman',45,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6    ,    fg etle color of text
lab_day.place(x=780,y=280,height=110,width=100)#x refers to verticle position and y refers to horizontal position 
#(2ND ROW)
lab_day_txt=Label(clock,text='DAY' , font=('times new roman',25,'bold'),bg='red',fg='white')#clock lakhvu jaruri j 6
lab_day_txt.place(x=780,y=420,height=40,width=100)#x refers to verticle position and y refers to horizontal position 




date_time()#akha function ne call karyu ana vagar data autometicly chage na thai


clock.mainloop()#mainloop() class no use e 6 aa graphics no on karse and on karya pa6i e on j rese
# badha graphics tk() and mainloop() ni vachhe lagse

#pa6i ama apde amuk changes kari sakie jem k text-color , bg-color , text-size , etc
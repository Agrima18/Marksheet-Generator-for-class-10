#School     Marksheet
from tkinter import*
from tkinter.messagebox import askokcancel

def get_data():
    
    hindi=hindi_name_1.get()
    English=English_name_1.get()
    sst=sst_name_1.get()
    science=science_name_1.get()
    math=math_name_1.get()
    total=hindi+English+sst+science+math
    percent=(total/500)*100
    div=""
    if percent>=65:
        div="1st Div"
    elif percent<65 and percent>=50:
        div="2nd Div"
    elif percent<50 and percent>=33:
        div="3rd Div"
    else:
        div="Fail"
    messagebox(total,percent,div)
def messagebox(*data):
    print_1=f"""
    Total:{data[0]}
    Percentage: {data[1]}
    Division: {data[2]}
    """
    askokcancel(title="DELHI PUBLIC SCHOOL",message=print_1)
    
win=Tk()
win.title("DELHI PULIC SCHOOL")
win.config(bg="yellow")
win.geometry("600x700")

school_name=Label(win,text="DELHI PUBLIC SCHOOL,BHILAI,(C.G)",font=("times new roman",20,"bold"),bg="yellow")
school_name.place(x=100,y=50,height=50,width=700)
st_name_1=Label(win,text="NAME",font=("Times New ROman",20,"bold"))
st_name_1.place(x=10,y=100,height=50,width=200)
st_name_Entry=Entry(win,font=("times new roman",40,"bold"),textvariable='st_name_1')
st_name_Entry.place(x=250,y=100,height=40,width=200)
l=("hindi","english","sst","maths","science")
subject_name=Label(win,text="Marks",font=("times new roman",40,"bold"),bg="yellow")
subject_name.place(x=10,y=150,height=40,width=400)
math_name_1=DoubleVar()
hindi_name_1=DoubleVar()
English_name_1=DoubleVar()
sst_name_1=DoubleVar()
science_name_1=DoubleVar()
math_name=Label(win,text="MATHS",font=("Times New ROman",20,"bold"))
math_name.place(x=10,y=300,height=60,width=200)
math_name_Entry=Entry(win,font=("times new roman",40,"bold"),textvariable=math_name_1)
math_name_Entry.place(x=250,y=300,height=40,width=300)
sst_name=Label(win,text="SOCIAL",font=("Times New ROman",20,"bold"))
sst_name.place(x=10,y=350,height=60,width=200)
sst_name_Entry=Entry(win,font=("times new roman",40,"bold"),textvariable=sst_name_1)
sst_name_Entry.place(x=250,y=350,height=40,width=300)
hindi_name=Label(win,text="THIRD LANG",font=("Times New ROman",20,"bold"))
hindi_name.place(x=10,y=400,height=60,width=200)
hindi_name_Entry=Entry(win,font=("times new roman",40,"bold"),textvariable=hindi_name_1)
hindi_name_Entry.place(x=250,y=400,height=40,width=300)
science_name=Label(win,text="SCIENCE",font=("Times New ROman",20,"bold"))
science_name.place(x=10,y=450,height=60,width=200)
science_name_Entry=Entry(win,font=("times new roman",40,"bold"),textvariable=science_name_1)
science_name_Entry.place(x=250,y=450,height=40,width=300)
English_name=Label(win,text="ENGLISH",font=("Times New ROman",20,"bold"))
English_name.place(x=10,y=500,height=60,width=200)
English_name_Entry=Entry(win,font=("times new roman",40,"bold"),textvariable=English_name_1)
English_name_Entry.place(x=250,y=500,height=40,width=300)
button=Button(win,text="DONE",font=("Times New Roman",20,"bold"),command=get_data)
button.place(x=250,y=650,height=60,width=200)

mainloop()

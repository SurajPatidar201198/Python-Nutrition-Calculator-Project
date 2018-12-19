from tkinter import *
from tkinter import messagebox

def newGUI():
    pk=Tk()
    pk.title("REPORT")
    pk.config(bg="#a1dbcd")
    '''icona = PhotoImage(file='images3.png')
    pk.tk.call('wm', 'iconphoto', pk._w, icona)'''
    label41=Label(pk,text="REPORT",fg="#383a39",font=("Arial Black",30),bg="#AEEEEE")
    label41.grid(row=0,column=1, padx=30, pady=20)
    def names():
        label309.config(text="Name:"+str(var10.get()),font=("Times 16 bold",12))
        '''name=str(var10.get())
        for letter in name:
            try:
                if letter.isdigit():
                    messagebox.showerror('Error','Invalid Name')
                    break
	    except:
                label309.config(text="Name:"+str(var10.get()),font=("Times 16 bold",12))'''
        
            
    def Pulse():
       try:
          if(var1.get()<=17):
             try:
                if(1<=float(var14.get())<70):
                   label52.config(text="Pulse Rate : LOW",font=("Times 16 bold",12))
                elif(70<=float(var14.get())<=100):
                   label52.config(text="Pulse Rate : NORMAL",font=("Times 16 bold",12))
                else:
                   label52.config(text="Pulse Rate : HIGH",font=("Times 16 bold",12))
             except:
                 #label52.config(text="Pulse Rate: Enter a Numeric Value",font=("Times 16 bold",12))
                 messagebox.showerror('Error','Invalid Name')
                
          else:
             try:
                if(1<=float(var14.get())<60):
                   label52.config(text="Pulse Rate : LOW",font=("Times 16 bold",12))
                elif(60<=float(var14.get())<=100):
                   label52.config(text="Pulse Rate : NORMAL",font=("Times 16 bold",12))
                else:
                   label52.config(text="Pulse Rate : HIGH",font=("Times 16 bold",12))
             except:
                #label52.config(text="Pulse Rate: Enter a Numeric Value",font=("Times 16 bold",12))
                 messagebox.showerror('Error','Invalid Entry')
                
       except:
          #label52.config(text="Age: Enter a Numeric Value",font=("Times 16 bold",12))
           messagebox.showerror('Error','Invalid Entry')
    def BP():
       try:
          if(1<=float(var12.get())<=90 and 1<=float(var13.get())<=60):
             label51.config(text="Blood Pressure : LOW",font=("Times 16 bold",12))
          elif(90<float(var12.get())<=130 and 60<float(var13.get())<=85):
             label51.config(text="Blood Pressure : NORMAL",font=("Times 16 bold",12))
          elif(130<=float(var12.get()) and 85<=float(var13.get())):
             label51.config(text="Blood Pressure : HIGH",font=("Times 16 bold",12))
       except:
          #label51.config(text="Blood Pressure : Enter a Numeric or correct Value",font=("Times 16 bold",12))
           messagebox.showerror('Error','Invalid Entry')
          
    def RBC():
       if(int(var.get()==1)):
          try:
             if(1<=float(var15.get())<4.7):
                label53.config(text="RBC Count : LOW",font=("Times 16 bold",12))
             elif(4.7<=float(var15.get())<=6.1):
                label53.config(text="RBC Count : NORMAL",font=("Times 16 bold",12))
             elif(6.1<=float(var15.get())):
                 label53.config(text="RBC Count : HIGH",font=("Times 16 bold",12))
          except:
             #label53.config(text="RBC Count : Enter a Numeric Value",font=("Times 16 bold",12))
              messagebox.showerror('Error','Invalid Entry')
              
       elif(int(var.get()==2)):
          try:
             if(1<=float(var15.get())<4.2):
                label53.config(text="RBC Count : LOW",font=("Times 16 bold",12))
             elif(4.2<=float(var15.get())<=5.4):
                label53.config(text="RBC Count : NORMAL",font=("Times 16 bold",12))
             else:
                label53.config(text="RBC Count : HIGH",font=("Times 16 bold",12))
          except:
             #label53.config(text="RBC Count : Enter a Numeric Value",font=("Times 16 bold",12))
              messagebox.showerror('Error','Invalid Entry')
              
                 
    def WBC():
       if(var1.get()<=2):
          try:
             if(1<=float(var16.get())<6200):
                label54.config(text="WBC Count : LOW",font=("Times 16 bold",12))
             elif(6200<=float(var16.get())<=17000):
                label54.config(text="WBC Count : NORMAL",font=("Times 16 bold",12))
             else:
                label54.config(text="WBC Count : HIGH",font=("Times 16 bold",12))
          except:
             #label54.config(text="WBC Count : Enter a Numeric Value",font=("Times 16 bold",12))
              messagebox.showerror('Error','Invalid Entry')
       else:
          try:
             if(1<=float(var16.get())<5000):
                label54.config(text="WBC Count : LOW",font=("Times 16 bold",12))
             elif(5000<=float(var16.get())<=10000):
                label54.config(text="WBC Count : NORMAL",font=("Times 16 bold",12))
             else:
                label54.config(text="WBC Count : HIGH",font=("Times 16 bold",12))
          except:
             #label54.config(text="WBC Count : Enter a Numeric Value",font=("Times 16 bold",12))
              messagebox.showerror('Error','Invalid Entry')
             
    def UricAcid():
        if(int(var.get()==2)):
           try:
              if(1<=float(var19.get())<2.4):
                 label58.config(text="URIC ACID LEVEL:LOW",font=("Times 16 bold",12))
              elif(2.4<=float(var19.get())<=6.0):
                 label58.config(text="URIC ACID LEVEL:NORMAL",font=("Times 16 bold",12))
              else:
                 label58.config(text="URIC ACID LEVEL:HIGH",font=("Times 16 bold",12))
           except:
              #label58.config(text="URIC ACID LEVEL:Enter a Numeric Value",font=("Times 16 bold",12))
               messagebox.showerror('Error','Invalid Entry')
              
        elif(int(var.get()==1)):
           try:
              if(1<=float(var19.get())<3.4):
                 label58.config(text="URIC ACID LEVEL:LOW",font=("Times 16 bold",12))
              elif(3.4<=float(var19.get())<=7.0):
                 label58.config(text="URIC ACID LEVEL:NORMAL",font=("Times 16 bold",12))
              else:
                 label58.config(text="URIC ACID LEVEL:HIGH",font=("Times 16 bold",12))
           except:
              #label58.config(text="URIC ACID LEVEL:Enter a Numeric Value",font=("Times 16 bold",12))
               messagebox.showerror('Error','Invalid Entry')
           
              
    
    def Hemoglobin():
        if(int(var.get()==1)):
           try:
              if(1<=float(var18.get())<13.5):
                 label56.config(text="HB level : LOW",font=("Times 16 bold",12))
              elif(13.5<=float(var18.get())<=17.5):
                 label56.config(text="HB level : NORMAL",font=("Times 16 bold",12))
              else:
                 label56.config(text="HB level : HIGH",font=("Times 16 bold",12))
           except:
              #label56.config(text="HB level : Enter a Numeric Value",font=("Times 16 bold",12))
               messagebox.showerror('Error','Invalid Entry')
               
        elif(int(var.get()==2)):
           try:
              if(1<=float(var18.get())<12.0):
                 label56.config(text="HB level : LOW",font=("Times 16 bold",12))
              elif(12.0<=float(var18.get())<=15.5):
                 label56.config(text="HB level : NORMAL",font=("Times 16 bold",12))
              else:
                 label56.config(text="HB level : HIGH",font=("Times 16 bold",12))
           except:
              #label56.config(text="HB level : Enter a Numeric Value",font=("Times 16 bold",12))
               messagebox.showerror('Error','Invalid Entry')
              
             
    def Cholestrol():
       try:
          if(1<=float(var20.get())<200):
             label57.config(text="Cholestrol Level: NORMAL",font=("Times 16 bold",12))
          elif(200<=float(var20.get())<239):
             label57.config(text="Cholestrol Level: BODERLINE HIGH",font=("Times 16 bold",12))
          else:
             label57.config(text="Cholestrol Level: HIGH",font=("Times 16 bold",12))
       except:
          #label57.config(text="Cholestrol Level: Enter a Numeric Number",font=("Times 16 bold",12))
           messagebox.showerror('Error','Invalid Entry')
          
           
    def Platlates():
       try:
          if(1<=float(var17.get())<1.5):
             label55.config(text="Platlates Count : LOW",font=("Times 16 bold",12))
          elif(1.5<=float(var17.get())<=4.5):
             label55.config(text="Platlates Count : NORMAL",font=("Times 16 bold",12))
          else:
             label55.config(text="Platlates Count : HIGH",font=("Times 16 bold",12))
       except:
          #label55.config(text="Platlates Count : Enter a Numeric Number",font=("Times 16 bold",12))
          messagebox.showerror('Error','Invalid Entry')
          
            
    def show():
       try:
          text_Input=(float(var4.get())/float(var3.get())**2)
          label30.config(text="Your BMI is : "+str(text_Input),font=("Times 16 bold",12))
          text_Input=float(text_Input)
          if(str(text_Input)<'16'):
             label31.config(text="You belongs to Severe Thinness Category",font=("Times 16 bold",12))
          elif('16'<=str(text_Input)<'17'):
             labe131.config(text="You belongs to Moderate Thinness Category",font=("Times 16 bold",12))
          elif('17'<=str(text_Input)<'18.5'):
             label31.config(text="You belongs to Mild Thinness Category",font=("Times 16 bold",12))
          elif('18.5'<=str(text_Input)<'25'):
             label31.config(text="You belongs Normal Category",font=("Times 16 bold",12))
          elif('25'<=str(text_Input)<'30'):
             label31.config(text="You belong to Overweight Category",font=("Times 16 bold",12))
          elif('30'<=str(text_Input)<'35'):
             label31.config(text="You belong to Obese Class I Category",font=("Times 16 bold",12))
          elif('35'<=str(text_Input)<'40'):
             label31.config(text="You belong to Obese Class II Category",font=("Times 16 bold",12))
          else:
             label31.config(text="You belong to Obese Class III Category",font=("Times 16 bold",12))
       except:
          #label31.config(text="Please provide proper information",font=("Times 16 bold",12))
           messagebox.showerror('Error','Invalid Entry')
          
            
    

    label309=Label(pk,text="",bg="#a1dbcd") 
    label309.grid(row=20,columnspan=3)     
                  
    label30=Label(pk,text="",bg="#a1dbcd") # Your BMI is ________
    label30.grid(row=21,columnspan=3)
    label51=Label(pk,text="",bg="#a1dbcd")  #Blood Pressure is __________
    label51.grid(row=22,columnspan=3)
    label52=Label(pk,text="",bg="#a1dbcd")  #Pulse Rate is ____________
    label52.grid(row=23,columnspan=3)
    label53=Label(pk,text="",bg="#a1dbcd")  # RBC Count is ________
    label53.grid(row=24,columnspan=3)
    label54=Label(pk,text="",bg="#a1dbcd")  # WBC Count is ________
    label54.grid(row=25,columnspan=3)
    label55=Label(pk,text="",bg="#a1dbcd")  # Platlates Count is ________
    label55.grid(row=26,columnspan=3)
    label56=Label(pk,text="",bg="#a1dbcd")  # Hemoglobin Level is ________
    label56.grid(row=27,columnspan=3)
    label57=Label(pk,text="",bg="#a1dbcd")  # Cholestrol Level is ________
    label57.grid(row=28,columnspan=3)
    label58=Label(pk,text="",bg="#a1dbcd")  # Uric Acid Level is ________
    label58.grid(row=29,columnspan=3)
    label31=Label(pk,text="",bg="#a1dbcd",font=("Times 16 bold",12)) #You Belongs to __________ category.
    label31.grid(row=50,columnspan=3)
    names()
    show()
    BP()
    Pulse()
    RBC()
    WBC()
    Platlates()
    Hemoglobin()
    UricAcid()
    Cholestrol()
    
    
    pk.mainloop()





#min value for Systolic Pressure is 50
#min value for Diastolic Pressure is 33

root=Tk()
root.title("BMI FITNESS CALCULATOR")
#########placing icon#######################
icon = PhotoImage(file='images3.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
###############################################
root.configure(background='white')
background_image=PhotoImage(file='bang.png')
background_image1=background_image.zoom(2)
background_label=Label(root,image=background_image1)
background_label.place(x=0,y=0,relheight=1,relwidth=1)
var=IntVar()
var1=IntVar()
var3=DoubleVar() 
var4=DoubleVar() 
var10=StringVar() 
var12=DoubleVar()
var13=DoubleVar()
var14=DoubleVar()
var15=DoubleVar()
var16=DoubleVar()
var17=DoubleVar()
var18=DoubleVar()
var19=DoubleVar()

var20=DoubleVar()

label4=Label(root,text="FITNESS CALCULATOR",fg="#383a39",font=("Arial Black",30),bg="#AEEEEE")
label4.grid(row=0,column=1, padx=30, pady=20)

label10=Label(root,text="NAME",bg="#AEEEEE",font=("Times 16 bold", 20))
label10.grid(row=4,column=0, padx=2, pady=2)
E10 = Entry(root, bd =5,textvariable=var10,width=15,font="Times 16 bold")
E10.grid(row=4,column=1 ,padx=2, pady=2)

   
#e = Entry(f,textvariable=1,height=20)

label=Label(root,text="AGE",bg="#AEEEEE",font=("Times 16 bold", 20))
label.grid(row=4,column=2,padx=2, pady=2)
E1 = Entry(root, bd =5,textvariable=var1,font="Times 16 bold",width=15)
E1.grid(row=4,column=4,padx=2, pady=2)

R1 = Radiobutton(root, text="MALE",variable=var,value=1,bg="#AEEEEE",font="Times 16 bold")
R1.grid(row=6,column=0,padx=2, pady=2)
R2 = Radiobutton(root, text="FEMALE",variable=var,value=2,bg="#AEEEEE",font="Times 16 bold")
R2.grid(row=6,column=1,padx=2, pady=2)

label2=Label(root,text="HEIGHT(in m)",bg="#AEEEEE",font=("Times 16 bold",15))
label2.grid(row=7,column=0,padx=2, pady=2)
E2 = Entry(root, bd =5,textvariable=var3,font="Times 16 bold",width=15)
E2.grid(row=7,column=1,padx=2, pady=2)

label3=Label(root,text="WEIGHT(in kg)",bg="#AEEEEE",font=("Times 16 bold",15))
label3.grid(row=8,column=0,padx=2, pady=2)
E3= Entry(root, bd =5,textvariable=var4,font="Times 16 bold",width=15)
E3.grid(row=8,column=1,padx=2, pady=2)

label12=Label(root,text="SYSTOLIC PRESSURE (mm Hg)",bg="#AEEEEE",font=("Times 16 bold",15))
label12.grid(row=9,column=0,padx=2, pady=2)
E12 = Entry(root, bd =5,textvariable=var12,font="Times 16 bold",width=15)
E12.grid(row=9,column=1,padx=2, pady=2)
label13=Label(root,text="DIASTOLIC PRESSURE (mm Hg)",bg="#AEEEEE",font=("Times 16 bold",15))
label13.grid(row=10,column=0,padx=2, pady=2)
E13= Entry(root, bd =5,textvariable=var13,font="Times 16 bold",width=15)
E13.grid(row=10,column=1,padx=2, pady=2)
label14=Label(root,text="PULSE RATE",bg="#AEEEEE",font=("Times 16 bold",15))
label14.grid(row=11,column=0,padx=2, pady=2)
E14 = Entry(root, bd =5,textvariable=var14,font="Times 16 bold",width=15)
E14.grid(row=11,column=1,padx=2, pady=2)
label15=Label(root,text="RBC COUNT(in millions)",bg="#AEEEEE",font=("Times 16 bold",15))
label15.grid(row=12,column=0,padx=2, pady=2)
E15 = Entry(root, bd =5,textvariable=var15,font="Times 16 bold",width=15)
E15.grid(row=12,column=1,padx=2, pady=2)
label16=Label(root,text="WBC COUNT(per microlitre of blood)",bg="#AEEEEE",font=("Times 16 bold",15))
label16.grid(row=13,column=0,padx=2, pady=2)
E16 = Entry(root, bd =5,textvariable=var16,font="Times 16 bold",width=15)
E16.grid(row=13,column=1,padx=2, pady=2)
label17=Label(root,text="PLATLATES(in Lacs(per microlitre of blood))",bg="#AEEEEE",font=("Times 16 bold",15))
label17.grid(row=14,column=0,padx=2, pady=2)
E17 = Entry(root, bd =5,textvariable=var17,font="Times 16 bold",width=15)
E17.grid(row=14,column=1,padx=2, pady=2)
label18=Label(root,text="HB",bg="#AEEEEE",font=("Times 16 bold",15))
label18.grid(row=15,column=0,padx=2, pady=2)
E18 = Entry(root, bd =5,textvariable=var18,font="Times 16 bold",width=15)
E18.grid(row=15,column=1,padx=2, pady=2)
label19=Label(root,text="URIC ACID",bg="#AEEEEE",font=("Times 16 bold",15))
label19.grid(row=16,column=0,padx=2, pady=2)
E19 = Entry(root, bd =5,textvariable=var19,font="Times 16 bold",width=15)
E19.grid(row=16,column=1,padx=2, pady=2)
label20=Label(root,text="CHOLESTROL",bg="#AEEEEE",font=("Times 16 bold",15))
label20.grid(row=17,column=0,padx=2, pady=2)
E20 = Entry(root, bd =5,textvariable=var20,font="Times 16 bold",width=15)
E20.grid(row=17,column=1,padx=2, pady=2)
try:
   button2=Button(root,padx=6,pady=3,bd=3,bg="Green",fg="white",font=("arial",20,"bold"),
               text="Generate Report",relief=RAISED,\
                         cursor="heart",command=lambda:[newGUI()])
   button2.grid(row=19,column=1,padx=5, pady=5)
except:
   print("lamda")

root.mainloop()

















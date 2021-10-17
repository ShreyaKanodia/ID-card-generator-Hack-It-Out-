from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


import re
import mysql.connector 
import pyttsx3
class Register:
    def __init__(self,root):


        self.root=root
        self.root.title("Register Page")
        self.root.geometry('1600x790+0+0')

        # text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)

         
        # VARIABLES

        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.country_var=StringVar()
        
        self.id_no_var=StringVar()
        self.password_var=StringVar()
        self.confirm_password_var=StringVar()
        self.check_var=IntVar()

        #Images
        self.bg=ImageTk.PhotoImage(file='background.jpg')
        bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        bg_lbl.place(x=0,y=0,width=1600,height=790)

        logo_img=Image.open('logo.jpg')
        logo_img=logo_img.resize((60,60),Image.ANTIALIAS)
        self.photoLogo=ImageTk.PhotoImage(logo_img)

        #Title Frame()
        title_Frame=Frame(self.root,bd=1,relief=RIDGE)
        title_Frame.place(x=500,y=28,width=550,height=82)

        title_lbl=Label(title_Frame,image=self.photoLogo,compound=LEFT,text="STUDENT REGISTRATION FORM",font=('times new roman',20,'bold','underline'),fg='darkblue')
        title_lbl.place(x=10,y=10)
        


        #Information Frame
        main_Frame=Frame(self.root,bd=1,relief=RIDGE)
        main_Frame.place(x=500,y=110,width=550,height=650)

        #USERNAME
        user_name=Label(main_Frame,text='Name:',font=('times new roman',16,'bold'))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        user_entry=ttk.Entry(main_Frame,textvariable=self.name_var,font=('times new roman',14,'bold'),width=28)
        user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        



        #EMAIL
        email_lbl=Label(main_Frame,text='Email ID:',font=('times new roman',16,'bold'))
        email_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        email_entry=ttk.Entry(main_Frame,textvariable=self.email_var,font=('times new roman',14,'bold'),width=28)
        email_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        

        # CONTACT
        contactNo=Label(main_Frame,text='Contact:',font=('times new roman',16,'bold'))
        contactNo.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        contact_entry=ttk.Entry(main_Frame,textvariable=self.contact_var,font=('times new roman',14,'bold'),width=28)
        contact_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        

        #GENDER

        gender_lbl=Label(main_Frame,text='Gender:',font=('times new roman',16,'bold'))
        gender_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        gender_Frame=Frame(main_Frame)
        gender_Frame.place(x=180,y=160,width=280,height=35)

        radio_male=Radiobutton(gender_Frame,variable=self.gender_var,value='Male',text='Male',font=("times new roman",15))
        radio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set('Male')
  

        radio_Female=Radiobutton(gender_Frame,variable=self.gender_var,value='Female',text='Female',font=("times new roman",15))
        radio_Female.grid(row=0,column=1,padx=10,pady=0,sticky=W)


        #Country
        select_country=Label(main_Frame,text='Country:',font=('times new roman',16,'bold'))
        select_country.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        list=['India','UK','Nepal','Afganistan','Pakistan']
        droplist=OptionMenu(main_Frame,self.country_var,*list)
        droplist.config(width=21,font=('times new roman',15),bg='white')
        self.country_var.set('Select your country')
        droplist.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        
        #ID NUMBER
        id_no=Label(main_Frame,text='Enrollment Number:',font=('times new roman',16,'bold'))
        id_no.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        id_no_entry=ttk.Entry(main_Frame,textvariable=self.id_no_var,font=('times new roman',14,'bold'),width=28)
        id_no_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        #PASSWORD

        password=Label(main_Frame,text='Password:',font=('times new roman',16,'bold'))
        password.grid(row=7,column=0,padx=10,pady=10,sticky=W)

        pass_entry=ttk.Entry(main_Frame,textvariable=self.password_var,font=('times new roman',14,'bold'),width=28)
        pass_entry.grid(row=7,column=1,padx=10,pady=10,sticky=W)

       

        #CONFIRM PASSWORD

        c_password=Label(main_Frame,text='Confirm Password:',font=('times new roman',16,'bold'))
        c_password.grid(row=8,column=0,padx=10,pady=10,sticky=W)

        c_pass_entry=ttk.Entry(main_Frame,textvariable=self.confirm_password_var,font=('times new roman',14,'bold'),width=28)
        c_pass_entry.grid(row=8,column=1,padx=10,pady=10,sticky=W)


        #CHECK BUTTON FRAME

        chechb_Frame=Frame(main_Frame)
        chechb_Frame.place(x=70,y=460,width=400,height=100)

        check_btn=Checkbutton(chechb_Frame,variable=self.check_var, text="Agree Our Terms And Conditions: ",font=('times new roman',16,'bold'),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)

        self.check_lbl=Label(chechb_Frame,text='',font=('aerial',14,'bold'),fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)


        # BUTTON FRAME

        button_Frame=Frame(main_Frame)
        button_Frame.place(x=20,y=550,width=500,height=100)

        save_data=Button(button_Frame,text='Save ',command=self.validation, font=('times new roman',14,'bold'),fg='white',bg='blue',width=14,cursor='hand2')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        verify_data=Button(button_Frame,text='Verify Data ',command=self.verify_data, font=('times new roman',14,'bold'),fg='white',bg='blue',width=14,cursor='hand2')
        verify_data.grid(row=0,column=1,padx=1,sticky=W)

        clear_data=Button(button_Frame,text='Clear Data ',command=self.clear_data,font=('times new roman',14,'bold'),fg='white',bg='blue',width=14,cursor='hand2')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)

    # CHeck Name
    def checkname(self,name):
        if name.isalpha():
            return True
        if name=='':
            return True
        else:
            self.engine.say('Space or special character or numbers are not allowed in name')
            self.engine.runAndWait()
            messagebox.showerror('Invalid','Not Allowed')

    # CheckContact
    def checkcontact(self,contact):
        if contact.isdigit() and  len(self.contact_var.get())==10:
            return True
        if len(str(contact))==0:
            return True
        else:
            self.engine.say('Only 10 digits are allowed in contact')
            self.engine.runAndWait()
            messagebox.showerror('Invalid','Invalid Entry')
            return False
    

    #CHECK PASSWORD

    def checkpassword(self,password):
        if len(password)<=21:

            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                return True

            else:
                self.engine.say('Enter a valid password')
                self.engine.runAndWait()
                messagebox.showinfo('invalid','Enter valid password (Example: Kiran@123)')

        else:
            self.engine.say('Length try to exceed')
            self.engine.runAndWait()
            messagebox.showerror('invalid',"Length try to exceed")
            return False


    #CHECK EMAILID

    def checkemail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                self.engine.say('Enter a valid user email')
                self.engine.runAndWait()
                messagebox.showwarning('Alert','Invalid email. Enter a valid user email (exammple: kiran@gmail.com)')
                return False

        else:
            self.engine.say('Email Length is too small')
            self.engine.runAndWait()
            messagebox.showinfo('Invalid','Email Length is too small')

    



    #Validations
    def validation(self):
        if self.name_var.get()=='':
            
            self.engine.say('Please enter your name')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your name',parent=self.root)
            
        elif self.email_var.get()=='':
            self.engine.say('Please enter your email-id')
            self.engine.runAndWait()

            messagebox.showerror('Error','Please enter your Email-Id',parent=self.root)

        elif self.contact_var.get()=='':
            self.engine.say('Please enter your  contact')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your  Contact',parent=self.root)

        elif self.gender_var.get()=='':
            
            self.engine.say('Please enter your gender')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your Gender',parent=self.root)

        elif self.country_var.get()=='' or self.country_var.get()=='Select your country':
            self.engine.say('Please select your country name')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please select your Country name',parent=self.root)

        

        elif len(self.id_no_var.get())!=12:
            self.engine.say('Please enter your 12 digit Enrollment number')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your 12 digit Enrollment number like 0X01XX1X10XX',parent=self.root)

        elif self.password_var.get()=='':
            self.engine.say('Please enter your Password')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your Password',parent=self.root)

        elif self.confirm_password_var.get()=='':
            self.engine.say('Please enter your Confirm Password')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your Confirm Password',parent=self.root)

        elif self.password_var.get()!=self.confirm_password_var.get():
            self.engine.say('Password and Confirm Password should match')
            self.engine.runAndWait()
            messagebox.showerror('Error','Password and Confirm Password should match',parent=self.root)

        elif self.email_var.get()!=None and self.password_var.get()!=None and self.name_var.get()!=None and self.contact_var.get()!=None :

            x=self.checkemail(self.email_var.get())
            print(f'x:{x}')
            y=self.checkpassword(self.password_var.get())
            print(f'y:{y}')

            
            u=self.checkname(self.name_var.get())
            print(f'u:{u}')
            w=self.checkcontact(self.contact_var.get())
            print(f'w:{w}')
            
     
            # callback and validation register
            # validate_name=self.root.register(self.checkname)
            # self.user_entry.config(validate='key',validatecommand=(validate_name,'%P'))

            # callback and validation register
            # validate_contact=self.root.register(self.checkcontact)
            # self.contact_entry.config(validate='key',validatecommand=(validate_contact,'%P'))

        if (x==True) and (y==True) and (w==True) and (u==True):
            
            if self.check_var.get()==0:
                self.engine.say('Please Agree Our terms And Conditions')
                self.engine.runAndWait()
                self.check_lbl.config(text='Please Agree Our terms And Conditions',      fg='red')

            else:
                self.check_lbl.config(text='Checked',fg='green')

                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='',database='mydata')
                    my_cursur=conn.cursor()
                    my_cursur.execute('insert into registration values(%s,%s,%s,%s,%s,%s,%s)',(
                                            
                                                                                                    self.name_var.get(),
                                                                                                    self.email_var.get(),
                                                                                                    self.contact_var.get(),
                                                                                                    self.gender_var.get(),
                                                                                                    self.country_var.get(),
                                                                                                
                                                                                                    self.id_no_var.get(),
                                                                                                    self.password_var.get()
                                                                                                    
                                                                                                    
                                                                                                        ))
                    conn.commit()

                    conn.close()
                    messagebox.showinfo('Successfull\n',f'Your registration successfully completed.\nName: {self.name_var.get()} \nPassword: {self.password_var.get()}')

                except Exception as es:
                    messagebox.showerror('Error',f'Due to: {str(es)}',parent=self.root)

    def verify_data(self):
        
        data=f'Name:{self.name_var.get()}\nEmail:{self.email_var.get()}\nContact:{self.contact_var.get()}\nCountry:{self.country_var.get()}\nGender:{self.gender_var.get()}\nID Type:{self.id_var.get()}\nId Number:{self.id_no_var.get()}\n'
        messagebox.showinfo('Details',data)

    def clear_data(self):
        
        self.name_var.set('')
        self.email_var.set('')
        self.contact_var.set('')
        self.gender_var.set('Male')
        self.country_var.set('Select your country')
        self.id_var.set('Select your ID')
        self.id_no_var.set('')
        self.password_var.set('')
        self.confirm_password_var.set('')
        self.check_var.set(0)



        

if __name__=='__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()

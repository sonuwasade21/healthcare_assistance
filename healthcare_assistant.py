# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:35:33 2021

@author: hp
"""
 
import csv
import sys
from matplotlib import pyplot as plt
import datetime
now=datetime.datetime.now()
import mysql.connector as m
con=m.connect(host="localhost",user="root",password="Sonu@2198",database="health_assistance")
db=con.cursor()
db.execute("use health_assistance")
db.execute("create table if not exists signup(username varchar(20),password varchar(20));")
db.execute("create table if not exists physical_info(weight float ,age float,height float ,gender char (5));")
db.execute("create table if not exists walking_data(Date date,walking_speed float,walking_duration float,calories_burned float);")
def say_wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!  ")

    elif hour>=12 and hour<18:
        print("Good Afternoon! ")   

    else:
        print("Good Evening!  ")  
    print("I am Ammy Sir. your personal health assistant")
    
def intro():
    print("Hi, I am your health assistant")
    print("I will help you to track your physical activity and help you stay fit")
    
    ch=input("TO KNOW ABOUT MY FEATURES PRESS ANY KEY: ")
    
    print("1.I can calculate your body mass index and tell you how much fit you are ")

    print("2. With the help of your walking data like distance you walked and walking duration i can calculate how much calories did you burn ")
    print("3. I will store your calories burning data and plot a graph for you so that you can analyse your calories burning data")
    print("\n1. IF YOU ARE A NEW USER PRESS 1 \n2. IF YOU ARE EXIXTING USER PRESS 2")
    while True :
        ch=int(input("ENTER YOUR CHOICE : "))
        if ch==1:
            print(phyc_data())
            break
        if ch==2:
            print("Do you want to see the menu, type y for yes and n for no ")
            me_choice=input("enter your choice : ")
            if me_choice=='y':
                print("ok sir")
                print(menu())
            if me_choice=='n':
                print("ok sir")
            break
            
        else:
            continue

def security():
    print(say_wish())
    print("This software is for physical activity tracking purpose , so we also keep you data privately accessible ,to ensure enought security , we will ask you for login details . initially you need to signup first")
    db.execute("create table if not exists signup(username varchar(20),password varchar(20))")

    while True:
        print("""
                                    +-------------------------------------------+
                                    |        Choose one option from below       |
                                    +-------------------------------------------+
                                    |                 1. Signup                 | 
                                    +-------------------------------------------+
                                    |                 2. Login                  |
                                    +-------------------------------------------+
                                                                                                        """)
            
        print("Warning for privacy reasons i format every saved data from the databases when you are a existing user and  select signup again ,so that any other person cannot able to acces your data. Be careful while entering your choice  ")
        print("press 1 for signup, press 2 for login")
        ch=int(input("Signup/Login(1,2):"))


        if ch==1:
            db.execute("delete from signup;")
            db.execute("delete from physical_info;")
            db.execute("delete from walking_data ;")
            
            print("enter your username ")
            username=input("USERNAME:")
            print("enter your password")
            pw=input("PASSWORD:")
            db.execute("insert into signup values('"+username+"','"+pw+"')")
            con.commit()
            print("your login data has succesfully recorded ")
            


        elif ch==2:
            print("enter your username ")

            username=input("USERNAME:")

            db.execute("select username from signup where username='"+username+"'")
            pot=db.fetchone()

            if pot is not None:
                print("VALID USERNAME!!!!!!")
                print("enter your password")

                pw=input("PASSWORD:")

                db.execute("select password from signup where password='"+pw+"'")
                a=db.fetchone()

                if a is not None:
                    print("""
                            +++++++++++++++++++++++
                            +++LOGIN SUCCESSFULL+++
                            +++++++++++++++++++++++
                                                        """)
                    print("Login succesfull , good to see you back sir/maam  ")
                    print(intro())
                    break
                else:
                    print("""
                            ++++++++++++++++++++++
                            ++INCORRECT PASSWORD++
                            ++++++++++++++++++++++
                                                        """)
                    print("incorrect password , access denied ")
                    
                    break


            else:
                print("""
                         ++++++++++++++++++++
                         ++INVALID USERNAME++
                         ++++++++++++++++++++
                                                """)
                print("incorrect username , access denied")
                
                break
        else:
            print("INVALID INPUT!")
            print(security())

def menu():
    print("Please read the menu carefully and enter your choice")

    
    print('''
                                    +----------------------------------------------------------+
                                    |        Choose one option from below                      |
                                    +----------------------------------------------------------+
                                    | 1. Check your bmi                                        | 
                                    +----------------------------------------------------------+
                                    | 2. Check how much calories did you burn during walking   |
                                    +----------------------------------------------------------+
                                    | 3. Take a look at your physical data                     | 
                                    +----------------------------------------------------------+
                                    | 4. Update your physical data                             | 
                                    +----------------------------------------------------------+
                                    | 5. Top 6 high calories burning cardio exercise or games  | 
                                    +----------------------------------------------------------+
                                    | 6. Take a look at your walking record                    | 
                                    +----------------------------------------------------------+
                                    | 7. Analyse your calories burning record                  |
                                    +----------------------------------------------------------+
                                    | 8. Exit                                                  |
                                    +----------------------------------------------------------+
                                                                                                                                ''')
    
    choi=int(input("enter your choice (1/2/3/4/5/6/7/8) : "))
    if choi==1:
        print(BMI_checker())
    if choi==2:
        print(pedo_tracker())
    if choi==3:
        print(see())
    if choi==4:
        print(up_data())
    if choi==5:
        print(work())
    if choi==6:
        print(see_walk())
    if choi==8:
        print(connect_termination())
    if choi==7:
        print(visualise())
    if choi==8:
        print(connect_termination())
def speak_menu():
    print("Enter your choice: ")

    
    print('''
                                    +----------------------------------------------------------+
                                    |        Choose one option from below                      |
                                    +----------------------------------------------------------+
                                    | 1. Check your bmi                                        | 
                                    +----------------------------------------------------------+
                                    | 2. Check how much calories did you burn during walking   |
                                    +----------------------------------------------------------+
                                    | 3. Take a look at your physical data                     | 
                                    +----------------------------------------------------------+
                                    | 4. Update your physical data                             | 
                                    +----------------------------------------------------------+
                                    | 5. Top 6 high calories burning cardio exercise or games  | 
                                    +----------------------------------------------------------+
                                    | 6. Take a look at your walking record                    | 
                                    +----------------------------------------------------------+
                                    | 7. Analyse your calories burning record                  |
                                    +----------------------------------------------------------+
                                    | 8.analyse your calories burning record                   |
                                    +----------------------------------------------------------+
                                                                                                                                ''')
                                                                                                                                
    choi=int(input("enter your choice (1/2/3/4/5/6/7/8) : "))
    if choi==1:
        print(BMI_checker())
    if choi==2:
        print(pedo_tracker())
    if choi==3:
        print(see())
    if choi==4:
        print(up_data())
    if choi==5:
        print(work())
    if choi==6:
        print(see_walk())
    if choi==8:
        print(connect_termination())
    if choi==7:
        print(visualise())
    if choi==8:
        print(connect_termination())

        
def phyc_data():
    db.execute("delete from physical_info")
    print("please enter your physical data carefully it will be used for further calulations ")
    
    wgt=float(input("please enter your weight in kg(s) : "))
    
    age=int(input(" enter your age : "))
    
    hgt=float(input("enter your height in cm : "))
    
    gen=input("please enter your gender (m/f) :")
    insert_data=(
    "INSERT INTO physical_info(weight,age,height,gender)"
    "VALUES (%s,%s,%s,%s)"
    )
    data=(wgt,age,hgt,gen)
    try:
        db.execute(insert_data,data)
        con.commit()
        print("""YOUR DATA HAS BEEN INSERTED :)
              """)
        print("YOUR DATA HAS SUCCESSFULLY RECORDED")
        
    except:
        db.roolback()
    print(see())
    print("Do you want to see the menu, type y for yes and n for no ")
    menu_choice=input("enter your choice: ")
    if menu_choice=='y':
        print("ok sir")
        print(menu())
    if menu_choice=='n':
        print("ok sir")
        
def connect_termination():
    print("Bye bye sir have a nice day ")
    sys.exit()

def BMI_checker():
    print("CALCULATING YOUR BODY MASS INDEX........")
    db.execute("use health_assistance")
    s=("select weight from physical_info;")
    db.execute(s)

    data=db.fetchall()
    wei=data[0][0]
    print(wei)
    l=("select height from physical_info;")
    db.execute(l)
    data=db.fetchall()
    hei=data[0][0]
    cov=hei*1/100
    print(cov)
    bmi=wei/(cov**2)
    
    print("Your BMI is: {0} and you are: ".format(bmi), end='')

    #conditions
    if ( bmi < 16):
       print(" you are severely underweigth")

    elif ( bmi >= 16 and bmi < 18.5):
       print("you are underweight")

    elif ( bmi >= 18.5 and bmi < 25):
       print("bingo! you are healthy")

    elif ( bmi >= 25 and bmi < 30):
       print("you are overweight ")

    elif ( bmi >=30):
        print("you are severely overweight")
    
    print("Do you want to see menu type y for yes and n for no ")
    me_choice=input("enter your choice: ")
    if me_choice=='n':
        print("ok sir")
        print(menu())
    if me_choice=='y':
        print("ok sir")
          
def pedo_tracker():

    print("""
                                                                ****************************************************************
                                                                                FIRST LET US CALCULATE YOUR BMR
                                                                ****************************************************************""")
    
    print("""
                                      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ABOUT BMR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                        Basal metabolic rate is the number of calories your body needs to accomplish its most basic (basal) life-sustaining functions.
                                      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")

    print("fetching your data from databases ")
    try:
        db.execute("use health_assistance")
        s=("select weight from physical_info;")
        db.execute(s)
        w_data=db.fetchall()
        w=w_data[0][0]
        l=("select height from physical_info;")
        db.execute(l)
        h_data=db.fetchall()
        h=h_data[0][0] 
        k=("select age from physical_info;")
        db.execute(k)
        a_data=db.fetchall()
        a=a_data[0][0]
        z=("select gender from physical_info;")
        db.execute(z)
        g_data=db.fetchall()
        g=g_data[0][0]
        
        if g=="m":
            bmr=66.47+(13.75*w)+(5.003*h)-(6.755*a)
                
            """**********************************************"""

            print("Your bmr is  : ",bmr)
        if g=="f":
            bmr=655.1+(9.563*w)+(1.85*h)-(4.676*a)
            
            """**********************************************"""

            print("Your bmr is  : ",bmr)
        speed=float(input("Enter your walking speed (km/h) : "))
    
        a=3.2
        b=4.0
        c=4.8
        d=5.6
        e=6.4
        f=7.2
        g=8.0
        if speed<=a:
            mets=2.0
        if speed==a:
            mets=2.8
        if speed==b:
            mets=3.0
        if speed==c:
            mets=3.5
        if speed==d:
            mets=4.3
        if speed==e:
            mets=5.0
        if speed==f:
            mets=7.0
        if speed==g:
            mets=8.3

        dur=int(input(" Enter your walking duration (in hour): "))
        print("""
              >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
              NOW CALCULATING HOW MUCH CALORIES DID YOU BURN!.......
              <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                                                      """)
        cal=bmr*mets/24*dur
        print("""
              >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
              CONGRAGULATION YOU BURN A TOTAL OF : """,cal,"calories","""
              <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                                     """)

        
        print("KEEP IT UP ;) ")   
        data_in=int(input("DO YOU WANT TO INSERT YOUR WALKING DATA (YES-TYPE 1 , NO TYPE-2 ) : "))
        if data_in==1:
            print('''             DATA WILL BE INSERTED ARE AS FOLLOWS
                                                                                ''')
            print('''
                                  DATA INSERTION DATE :''',now
                                                                                )
            print('''
                                  WALKING SPEED : ''',speed
                                                                    )
            print('''
                                  WALKING DURATION :''',dur
                                                                        )
            print('''
                                  CALORIES BURNED :''',cal
                                                                        )
            
            print("Proccesing your data insertion request")
            sql="INSERT INTO walking_data(Date , walking_speed , walking_duration , calories_burned) values(%s,%s,%s,%s)"
            val=(now,speed,dur,cal)
            db.execute(sql,val)
            con.commit()
            print('''
                                  YOUR DATA HADS SUCCESSFULLY RECORDED !
                                                                                            ''')
            
    except:
        print("""
            ------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!----------------
            PLEASE STORE YOUR PHYSICAL DATA FIRST, WE CALUCULATE THINGS THROUGHT YOUR STORED DATA
            ------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!----------------
                                                                                                                                                         """)   
        print(phyc_data())

    print("Do you want to see the menu , type y for yes and n for no ")
    me_choice=input("enter your choice")
    if me_choice=='n':
        print("ok sir")
        print(menu())
    if me_choice=='y':
        print("ok sir")
  
def up_data():    
    db.execute("delete from physical_info;")    
    print("Previous data deleted")
    wgt=int(input("please enter your weight in kg(s) : "))
    age=int(input(" enter your age : "))
    hgt=int(input("enter your height in cm : "))
    gen=input("please enter your gender (M/F/others) :")
    insert_data=(
    "INSERT INTO physical_info(weight,age,height,gender)"
    "VALUES (%s,%s,%s,%s)"
    )
    data=(wgt,age,hgt,gen)
    try:


        db.execute(insert_data,data)
        con.commit()
        print("""   
              YOUR DATA HAS BEEN INSERTED :)
                                                            """)
    except:
        con.roolback()
    
    print("Do you want to see the menu , type y for yes and n for no ")
    me_choice=input("enter your choice: ")
    if me_choice=='y':
        print("ok sir")
        print(menu())
    if me_choice=='n':
        print("ok sir")
    
def visualise():
    print("""
         VISUALISING YOUR DATA..........
                                                                                """)
    com=("select Date,calories_burned from walking_data;")
    db.execute(com)
    data=db.fetchall()
    row1=[]
    row2=[]

    for row in data:
        row1.append(row[0])
        row2.append(row[1])
    plt.xlabel('Date')  
# naming the y axis  
    plt.ylabel('Calories burned')  
    
# giving a title to my graph  
    plt.title('Calories burning record')  
    plt.plot(row1,row2,'-')
    plt.show()
    print("Do you want to see the menu , type y for yes and n for no ")
    me_choice=input("enter your choice: ")
    if me_choice=='y':
        print("ok sir")
        print(menu())
    if me_choice=='n':
        print("ok sir")
        
def see():
    show_t_data="select*from physical_info"
    db.execute(show_t_data)
    records=db.fetchall()
    
    print("\nprinting the record")
    for row in records:
        print("WEIGHT = ",row[0],)
        print("---------------------------")
        print("AGE = ",row[1],)
        print("---------------------------")              
        print("HEIGHT = ",row[2],)
        print("---------------------------")
        print("GENDER = ",row[3],)
        print("---------------------------")

    
    print("Do you want to see the menu , type y for yes and n for no ")
    me_choice=input("enter your choice: ")
    if me_choice=='y':
        print("ok sir")
        print(menu())
    if me_choice=='n':
        print("ok sir")
        
def see_walk():
    show_w_data="select*from walking_data"
    db.execute(show_w_data)
    rec=db.fetchall()
    print("total no of data in database : ",db.rowcount)
    print("\nprinting the record")
    for row in rec:
        print("DATE = ",row[0],)
        
        print("""---------------------------""")
        
        print("WALKING SPEED = ",row[1],)
        
        print("---------------------------")        
        
        print("WALKING DURATION = ",row[2],)
        
        print("---------------------------")
        
        print("CALORIES BURNED = ",row[3],)
        
        print("---------------------------")

    
    print("Do you want to see the menu , type y for yes and n for no ")
    me_choice=input("enter your choice: ")
    if me_choice=='y':
        print("ok sir")
        print(menu())
    if me_choice=='n':
        print("ok sir")
    
def work():     
    f=open("workout.csv","w")
    w=csv.writer(f)    
    l=['Workout name','Calories burned per hour']
    s=['RUNNING', '755 CALORIES/HOUR']
    run=['RUNNING UP STAIRS', '819 CALORIES/HOUR']
    swim=['VIGOUROUS SWIMMING', '892 CALORIES/HOUR']
    soc=['SOCCER', '937 CALORIES/HOUR']
    jump=['JUMP ROPE', '1074 CALORIES/HOUR']
    w.writerow(l)
    w.writerow(s)
    w.writerow(run)
    w.writerow(swim)
    w.writerow(soc)
    w.writerow(jump)
    f.close()
    f=open("workout.csv","r")
    airw=csv.reader(f)
    for i in airw:
        print(i)
    f.close()
    
    print("Do you want to see the menu , type y for yes and n for no ")
    me_choice=input("enter your choice: ")
    if me_choice=='y':
        print("ok sir")
        print(menu())
    if me_choice=='n':
        print("ok sir")
        
print(security())


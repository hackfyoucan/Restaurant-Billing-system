from tkinter import *
import datetime
from tkinter import Tk,StringVar, ttk
import tkinter.messagebox as tmsg
# from billGenerator import bill



root=Tk()
root.title("Billing System")

#screen resolution
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('{}x{}'.format(screen_width, screen_height))


#Date
now = datetime.datetime.now()
time=now.strftime("%Y-%m-%d %X")
Label(root,text=f"Date & Time:{time}",font="arial 13").grid(row=2,column=6)


Label(root,text="Team 02 restaurant",font="comicsanms 25 italic",fg="Red",padx=200,pady=10,
).grid(row=0,column=0,columnspan=3,sticky="w")
Label(root,text="South Indian,North Indian Food",font="tahoma 12 ",fg="Black",padx=200,pady=10).grid(row=1,column=0,columnspan=3)
Label(root,text="Menu",font="arial 10 bold").grid(row=2,column=0,columnspan=3)
# root.configure(background='grey')


#---------------------------------------------------
#defining all the required functions
#adding payment option
pmethod=Label(root,font="arial 11 bold",text="Payment Method",bd=10,width=16,
anchor="w")
pmethod.grid(row=4,column=6)
#adding dropdown menu
paymentoptions=[
    "Phone Pay",
    "Google Pay",
    "Paytm"
]

paymentmethod=ttk.Combobox(root,value=paymentoptions,width=15)
print(paymentmethod.get())
paymentmethod.current(1)#displaying default value
print("jdas",paymentmethod)
paymentmethod.grid(row=5,column=6)

#display ClientName and mobile number


def closewindow():
    ex=tmsg.askyesno("Notification","Do you want to exit?")
    if ex>0:
        root.destroy()
        return
   
def reset():
    var_11.set("0")
    var_12.set("0")
    var_13.set("0")
    var_14.set("0")
    var_15.set("0")
    var_21.set("0")
    var_22.set("0")
    var_23.set("0")
    var_24.set("0")
    var_25.set("0")
    var_26.set("0")
    var_27.set("0")
    var_31.set("0")
    var_32.set("0")
    var_33.set("0")
    var_34.set("0")
    var_35.set("0")
    var_36.set("0")
    var_37.set("0")
    var_38.set("0")
    var_39.set("0")
    var_310.set("0")
    var_311.set("0")
    var_312.set("0")
    var_51.set("0")
    var_52.set("0")
    var_53.set("0")
    var_54.set("0")
    var_55.set("0")
    var_56.set("0")
    var_61.set("0")
    var_62.set("0")
    var_63.set("0")
    var_64.set("0")
    var_65.set("0")
    var_66.set("0")
    var_67.set("0")
    var_68.set("0")
    var_69.set("0")
    var_610.set("0")
    var_611.set("0")
    mobile.set("")
    ClientName.set("")
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var37.set(0)
    var38.set(0)
    var39.set(0)
    var310.set(0)
    var311.set(0)
    var51.set(0)
    var52.set(0)
    var53.set(0)
    var54.set(0)
    var55.set(0)
    var56.set(0)
    var61.set(0)
    var62.set(0)
    var63.set(0)
    var64.set(0)
    var65.set(0)
    var66.set(0)
    var67.set(0)
    var68.set(0)
    var69.set(0)
    var610.set(0)
    var611.set(0)
    total.set(0) 


q = []
#calculating the total bill
def totalbill():
    food1=float(var_11.get())
    food2=float(var_12.get())
    food3=float(var_13.get())
    food4=float(var_14.get())
    food5=float(var_15.get())
    food6=float(var_21.get())
    food7=float(var_22.get())
    food8=float(var_23.get())
    food9=float(var_24.get())
    food10=float(var_25.get())
    food11=float(var_26.get())
    food13=float(var_31.get())
    food14=float(var_32.get())
    food15=float(var_33.get())
    food16=float(var_34.get())
    food17=float(var_35.get())
    food19=float(var_37.get())
    food20=float(var_38.get())
    food21=float(var_39.get())
    food22=float(var_310.get())
    food23=float(var_311.get())
    food24=float(var_51.get())
    food25=float(var_52.get())
    food26=float(var_53.get())
    food27=float(var_54.get())
    food28=float(var_55.get())
    food29=float(var_56.get())
    food30=float(var_61.get())
    food31=float(var_62.get())
    food32=float(var_63.get())
    food33=float(var_64.get())
    food34=float(var_65.get())
    food35=float(var_66.get())
    food36=float(var_67.get())
    food37=float(var_68.get())
    quantity = [food1,food2,food3,food4,food5,food6,food7,food8,food9,food10,food11,food13,food14,food15,food16,food17,food19,food20,food21,food22,food23,food24,food25,food26,food27,food28,food29,food30,food31,food32,food33,food34,food35,food36,food37]
    for i in range(35):
        if quantity[i] >0.0:
            q.append(quantity[i])
    #total amount calculation
    total.set((food1*10)+(food2*10)+(food3*15)+(food4*20)+(food5*20)+(food6*50)+(food7*30)+(food8*25)+(food9*35)+
    (food10*25)+(food11*25)+(food13*90)+(food14*110)+(food15*120)+(food16*120)+(food17*160)+(food19*140)+(food20*110)+(food21*130)+(food22*120)+(food23*190)+
    (food24*10)+(food25*15)+(food26*25)+(food27*30)+(food28*30)+(food29*35)+(food30*80)+(food31*50)+(food32*100)+(food33*120)+(food34*120)+(food35*120)+(food36*150)+(food37*160))
    
#---------------------------------------------------------------------------

#all variables involved
var11=IntVar()#subah ki shuruaat
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var21=IntVar()#breakfast
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var31=IntVar()#Starter veg and non veg
var32=IntVar()#machu
var33=IntVar()#mush
var34=IntVar()#paneer
var35=IntVar()#veg65
var36=IntVar()#chi chilly
var37=IntVar()#chic65
var38=IntVar()#egg65
var39=IntVar()#chicken sukha
var310=IntVar()#fish
var311=IntVar()
var51=IntVar()#Roti,Chapati
var52=IntVar()#tandoori roti
var53=IntVar()#naan
var54=IntVar()#butter naan
var55=IntVar()#kulcha
var56=IntVar()#butter kulcha
var61=IntVar()#Rice,Jeera
var62=IntVar()#ghee
var63=IntVar()#curd
var64=IntVar()#kadi
var65=IntVar()#dal khichdi
var66=IntVar()#rajma rice
var67=IntVar()#veg pulav
var68=IntVar()#chicken Biryani
var69=IntVar()#Mutton Biryani
var610=IntVar()#some fish rice
var611=IntVar()#Mutton birynani

#set
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var21.set(0)
var22.set(0)
var23.set(0)
var24.set(0)
var25.set(0)
var26.set(0)
var27.set(0)
var31.set(0)
var32.set(0)
var33.set(0)
var34.set(0)
var35.set(0)
var36.set(0)
var37.set(0)
var38.set(0)
var39.set(0)
var310.set(0)
var311.set(0)
var51.set(0)
var52.set(0)
var53.set(0)
var54.set(0)
var55.set(0)
var56.set(0)
var61.set(0)
var62.set(0)
var63.set(0)
var64.set(0)
var65.set(0)
var66.set(0)
var67.set(0)
var68.set(0)
var69.set(0)
var610.set(0)
var611.set(0)


#creating string variable
var_11=StringVar()
var_12=StringVar()
var_13=StringVar()
var_14=StringVar()
var_15=StringVar()
var_21=StringVar()
var_22=StringVar()
var_23=StringVar()
var_24=StringVar()
var_25=StringVar()
var_26=StringVar()
var_27=StringVar()
var_31=StringVar()
var_32=StringVar()
var_33=StringVar()
var_34=StringVar()
var_35=StringVar()
var_36=StringVar()
var_37=StringVar()
var_38=StringVar()
var_39=StringVar()
var_310=StringVar()
var_311=StringVar()
var_312=StringVar()

var_51=StringVar()#Roti,Chapati
var_52=StringVar()#tandoori roti
var_53=StringVar()#naan
var_54=StringVar()#butter naan
var_55=StringVar()#kulcha
var_56=StringVar()#butter kulcha
var_61=StringVar()#Rice,Jeera
var_62=StringVar()#ghee
var_63=StringVar()#curd
var_64=StringVar()#kadi
var_65=StringVar()#dal khichdi
var_66=StringVar()#rajma rice
var_67=StringVar()#veg pulav
var_68=StringVar()#chicken Biryani
var_69=StringVar()#Mutton Biryani
var_610=StringVar()#some fish rice
var_611=StringVar()#Mutton birynani

#additional things
ClientName=StringVar()
total=StringVar()
mobile=StringVar()
change=StringVar()

#----------------------------------------------------------------------------------------
#set the string var to "0"
var_11.set("0")
var_12.set("0")
var_13.set("0")
var_14.set("0")
var_15.set("0")
var_21.set("0")
var_22.set("0")
var_23.set("0")
var_24.set("0")
var_25.set("0")
var_26.set("0")
var_27.set("0")
var_31.set("0")
var_32.set("0")
var_33.set("0")
var_34.set("0")
var_35.set("0")
var_36.set("0")
var_37.set("0")
var_38.set("0")
var_39.set("0")
var_310.set("0")
var_311.set("0")
var_312.set("0")
var_51.set("0")
var_52.set("0")
var_53.set("0")
var_54.set("0")
var_55.set("0")
var_56.set("0")
var_61.set("0")
var_62.set("0")
var_63.set("0")
var_64.set("0")
var_65.set("0")
var_66.set("0")
var_67.set("0")
var_68.set("0")
var_69.set("0")
var_610.set("0")
var_611.set("0")
mobile.set("")
total.set("0")
change.set("0")



#------------------------------------------------------------------------------------------

#checking state of checkbutton
#subah ki shuruaat

res = []
price = []
def food_tea():
    if (var11.get()==1):
        foodntea.config(state=NORMAL)
        res.append("☕️Tea")
        price.append(10)
        var_11.set("")
    else:
        foodntea.configure(state=DISABLED)
        var_11.set(0)

def food_coffee():
    if (var12.get()==1):
        foodncoffee.configure(state=NORMAL)
        res.append("☕️ Coffee")
        price.append(10)
        var_12.set("")
    else:
        foodncoffee.configure(state=DISABLED)
        var_12.set(0)

def food_ccoffee():
    if (var13.get()==1):
        foodnccoffee.configure(state=NORMAL)
        res.append("cold coffee")
        price.append(10)
        var_13.set("")
    else:
        foodnccoffee.configure(state=DISABLED)
        var_13.set(0)

def food_milk():
    if (var14.get()==1):
        foodnmilk.configure(state=NORMAL)
        res.append("milk")
        price.append(10)
        var_14.set("")
    else:
        foodnmilk.configure(state=DISABLED)
        var_14.set(0)

def food_bmilk():
    if (var15.get()==1):
        foodnbmilk.configure(state=NORMAL)
        res.append("bornvita milk")
        price.append(10)
        var_15.set("")
    else:
        foodnbmilk.configure(state=DISABLED)
        var_15.set(0)

#breakfast
def food_cb():
    if var21.get()==1:
        foodncb.configure(state=NORMAL)
        res.append("chole Bhature")
        price.append(10)
        var_21.set("")
    else:
        foodncb.configure(state=DISABLED)
        var_21.set(0)
def food_shira():

    if var22.get()==1:
        foodnshira.configure(state=NORMAL)
        res.append("shira")
        price.append(10)
        var_22.set("")
    else:
        foodnshira.configure(state=DISABLED)
        var_22.set(0)

def food_poha():
    if var23.get()==1:
        print("poha")
        foodnpoha.configure(state=NORMAL)
        res.append(var23.get())
        price.append(10)
        var_23.set("")
    else:
        foodnpoha.configure(state=DISABLED)
        var_23.set(0)

def food_iv():
    if var24.get()==1:
        foodniv.configure(state=NORMAL)
        res.append("idli-vada")
        price.append(10)
        var_24.set("")
    else:
        foodniv.configure(state=DISABLED)
        var_24.set(0)

def food_mdosa():
    if var25.get()==1:
        foodnmdosa.configure(state=NORMAL)
        res.append("Masala Dosa")
        price.append(10)
        var_25.set("")
    else:
        foodnmdosa.configure(state=DISABLED)
        var_25.set(0)      

def food_pdosa():
    if var26.get()==1:
        foodnpdosa.configure(state=NORMAL)
        res.append("Paper Dosa")
        price.append(10)
        var_26.set("")
    else:
        foodnpdosa.configure(state=DISABLED)
        var_26.set(0)


#starter
def food_vm():
    if var31.get()==1:
        foodnvm.configure(state=NORMAL)
        res.append("Veg Manchurian")
        price.append(10)
        var_31.set("")
    else:
        foodnvm.configure(state=DISABLED)
        var_31.set(0)

def food_mcd():
    if var32.get()==1:
        foodnmcd.configure(state=NORMAL)
        res.append("Mushroom chilly Dry")
        price.append(10)
        var_32.set("")
    else:
        foodnmcd.configure(state=DISABLED)
        var_32.set(0)


def food_pcd():
    if var33.get()==1:
        foodnpcd.configure(state=NORMAL)
        res.append("Paneer Chilly Dry")
        price.append(10)
        var_33.set("")
    else:
        foodnpcd.configure(state=DISABLED)
        var_33.set(0)


def food_v65():
    if var34.get()==1:
        foodnv65.configure(state=NORMAL)
        res.append("veg 65 Dry")
        price.append(10)
        var_34.set("")
    else:
        foodnv65.configure(state=DISABLED)
        var_34.set(0)

def food_cchilly():
    if var35.get()==1:
        foodncc.configure(state=NORMAL)
        res.append("chicken chilly")
        price.append(10)
        var_35.set("")
    else:
        foodncc.configure(state=DISABLED)
        var_35.set(0)

# def food_cmd():
#     if var36.get()==1:
#         foodncmd.configure(state=NORMAL)
#         var36.set("")
#     else:
#         foodncmd.configure(state=DISABLED)
#         var36.set(0)

# def food_ccrispy():
#     if var37.get()==1:
#         foodnccrispy.configure(state=NORMAL)
#         res.append("Fish Koliwada")
#         price.append(10)
#         var_37.set("")
#     else:
#         foodnccrispy.configure(state=DISABLED)
#         var_37.set(0)

# def food_clolly():
#     if var38.get()==1:
#         foodncl.configure(state=NORMAL)
#         res.append("Chicken Crispy")
#         price.append(10)
#         var_38.set("")
#     else:
#         foodncl.configure(state=DISABLED)
#         var_38.set(0)

# def food_csukha():
#     if var39.get()==1:
#         foodncs.configure(state=NORMAL)
#         res.append("Chicken Sukha")
#         price.append(10)
#         var_39.set("")
#     else:
#         foodncs.configure(state=DISABLED)
#         var_39.set(0)

# def food_msukha():
#     if var310.get()==1:
#         foodnmsukha.configure(state=NORMAL)
#         res.append("Mutton Sukha")
#         price.append(10)
#         var_310.set("")
#     else:
#         foodnmsukha.configure(state=DISABLED)
#         var_310.set(0)

# def food_fkoli():
#     if var311.get()==1:
#         foodnfk.configure(state=NORMAL)
#         res.append("Fish Koliwada")
#         price.append(10)
#         var_311.set("")
#     else:
#         foodnfk.configure(state=DISABLED)
#         var_311.set(0)


#breads
def food_chapati():
    if var51.get()==1:
        foodnchapati.configure(state=NORMAL)
        res.append("Chapati")
        price.append(10)
        var_51.set("")
    else:
        foodnchapati.configure(state=DISABLED)
        var_51.set(0)

def food_troti():
    if var52.get()==1:
        foodntroti.configure(state=NORMAL)
        res.append("tandoori roti")
        price.append(10)
        var_52.set("")
    else:
        foodntroti.configure(state=DISABLED)
        var_52.set(0)

def food_naan():
    if var53.get()==1:
        foodnnaan.configure(state=NORMAL)
        res.append("Naan")
        price.append(10)
        var_53.set("")
    else:
        foodnnaan.configure(state=DISABLED)
        var_53.set(0)

def food_bnaan():
    if var54.get()==1:
        foodnbnaan.configure(state=NORMAL)
        res.append("Butter Naan")
        price.append(10)
        var_54.set("")
    else:
        foodnbnaan.configure(state=DISABLED)
        var_54.set(0)

def food_kulcha():
    if var55.get()==1:
        foodnkulcha.configure(state=NORMAL)
        res.append("Kulcha")
        price.append(10)
        var_55.set("")
    else:
        foodnkulcha.configure(state=DISABLED)
        var_55.set(0)

def food_bkulcha():
    if var56.get()==1:
        foodnbkulcha.configure(state=NORMAL)
        res.append("Butter Kulcha")
        price.append(10)
        var_56.set("")
    else:
        foodnbkulcha.configure(state=DISABLED)
        var_56.set(0)


#rice
def food_jeera():
    if var61.get()==1:
        foodnjeera.configure(state=NORMAL)
        res.append("Jeera rice")
        price.append(10)
        var_61.set("")
    else:
        foodnjeera.configure(state=DISABLED)
        var_61.set(0)

def food_curd():
    if var62.get()==1:
        foodncurd.configure(state=NORMAL)
        res.append("Curd Rice")
        price.append(10)
        var_62.set("")
    else:
        foodncurd.configure(state=DISABLED)
        var_62.set(0)
        
def food_rajma():
    if var63.get()==1:
        foodnrajma.configure(state=NORMAL)
        res.append("rajma")
        price.append(10)
        var_63.set("")
    else:
        foodnrajma.configure(state=DISABLED)
        var_63.set(0)


def food_vegpulav():
    if var64.get()==1:
        foodnvpulav.configure(state=NORMAL)
        res.append("Veg Pulav")
        price.append(10)
        var_64.set("")
    else:
        foodnvpulav.configure(state=DISABLED)
        var_64.set(0)

def food_vegbir():
    if var65.get()==1:
        foodnvbir.configure(state=NORMAL)
        res.append("veg biryani")
        price.append(10)
        var_65.set("")
    else:
        foodnvbir.configure(state=DISABLED)
        var_65.set(0)

def food_cbir():
    if var66.get()==1:
        foodncbir.configure(state=NORMAL)
        res.append("chicken Biryani")
        price.append(10)
        var_66.set("")
    else:
        foodncbir.configure(state=DISABLED)
        var_66.set(0)

# def food_mbir():
#     if var67.get()==1:
#         foodnmbir.configure(state=NORMAL)
#         res.append("Mutton Biryani")
#         price.append(10)
        
#         var_67.set("")
#     else:
#         foodnmbir.configure(state=DISABLED)
#         var_67.set(0)

# def food_fish():
#     if var68.get()==1:
#         foodnfish.configure(state=NORMAL)
#         res.append("Prawns Rice")
#         price.append(10)
#         var_68.set("")
#     else:
#         foodnfish.configure(state=DISABLED)
#         var_68.set(0)







##########################################################################################
Label(root,text="Subah ki shuruaat",font="arial 12 bold").grid(row=3,column=0)
Label(root,text="Breakfast",font="arial 12 bold").grid(row=3,column=2,sticky="e")
Label(root,text="Starter ",font="arial 12 bold").grid(row=10,column=0)
Label(root,text="Breads",font="arial 12 bold").grid(row=10,column=2)
Label(root,text="Rice",font="arial 12 bold").grid(row=3,column=4)
#Label(root,text="Beverages",font="comicsanms 11").grid(row=,column=)
#Label(root,text="",font="comicsanms 11").grid(row=,column=)

#adding tea

foodtea=Checkbutton(root,text="☕️ Tea\t\t₹10",variable=var11,font=" helvetica 10",command=food_tea)
foodtea.grid(row=4,column=0,sticky="w")
foodntea=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_11)
foodntea.grid(row=4,column=1,sticky="w")

foodcoffee=Checkbutton(root,text="☕️ Coffee\t₹10",variable=var12,font=" helvetica 10",command=food_coffee)
foodcoffee.grid(row=5,column=0,sticky="W")
foodncoffee=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_12)
foodncoffee.grid(row=5,column=1,sticky="w")

foodccoffee=Checkbutton(root,text="☕️ Cold Coffee\t₹15",variable=var13,font=" helvetica 10",command=food_ccoffee)
foodccoffee.grid(row=6,column=0,sticky="W")
foodnccoffee=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_13)
foodnccoffee.grid(row=6,column=1,sticky="w")

foodmilk=Checkbutton(root,text="☕️ Milk\t\t₹15",variable=var14,font=" helvetica 10",command=food_milk)
foodmilk.grid(row=7,column=0,sticky="W")
foodnmilk=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_14)
foodnmilk.grid(row=7,column=1,sticky="w")

foodbmilk=Checkbutton(root,text="☕️ Bornvita Milk\t₹20",variable=var15,font=" helvetica 10",command=food_bmilk)
foodbmilk.grid(row=8,column=0,sticky="W")
foodnbmilk=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_15)
foodnbmilk.grid(row=8,column=1,sticky="w")

#adding breakfast


foodcb=Checkbutton(root,text="🍱 Chole Bhature\t\t₹50",variable=var21,font=" helvetica 10",command=food_cb)
foodcb.grid(row=4,column=2,sticky="W")
foodncb=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_21)
foodncb.grid(row=4,column=3,sticky="w")

foodshira=Checkbutton(root,text="🍱 Shira\t\t\t₹30",variable=var22,font=" helvetica 10",command=food_shira)
foodshira.grid(row=5,column=2,sticky="W")
foodnshira=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_22)
foodnshira.grid(row=5,column=3,sticky="w")

foodpoha=Checkbutton(root,text="🍱 Poha\t\t\t₹25",variable=var23,font=" helvetica 10",command=food_poha)
foodpoha.grid(row=6,column=2,sticky="W")
foodnpoha=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_23)
foodnpoha.grid(row=6,column=3,sticky="w")

foodiv=Checkbutton(root,text="🍱 Idli-Vada\t\t₹35",variable=var24,font=" helvetica 10",command=food_iv)
foodiv.grid(row=7,column=2,sticky="W")
foodniv=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_24)
foodniv.grid(row=7,column=3,sticky="w")

foodmdosa=Checkbutton(root,text="🍱 Masala Dosa\t\t₹35",variable=var25,font=" helvetica 10",command=food_mdosa)
foodmdosa.grid(row=8,column=2,sticky="W")
foodnmdosa=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_25)
foodnmdosa.grid(row=8,column=3,sticky="w")

foodpdosa=Checkbutton(root,text="🍱 Paper dosa\t\t₹30",variable=var26,font=" helvetica 10",command=food_pdosa)
foodpdosa.grid(row=9,column=2,sticky="W")
foodnpdosa=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_26)
foodnpdosa.grid(row=9,column=3,sticky="w")

#starter 
foodvm=Checkbutton(root,text="🥗 Veg Manchurian Dry\t₹90",variable=var31,font=" helvetica 10",command=food_vm).grid(row=11,column=0,sticky="W")
foodnvm=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_31)
foodnvm.grid(row=11,column=1,sticky="w")

foodmcd=Checkbutton(root,text="🥗 Mushroom Chilly Dry\t₹110",variable=var32,font=" helvetica 10",command=food_mcd).grid(row=12,column=0,sticky="W")
foodnmcd=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_32)
foodnmcd.grid(row=12,column=1,sticky="w")

foodpcd=Checkbutton(root,text="🥗 Paneer Chilly Dry\t\t₹120",variable=var33,font=" helvetica 10",command=food_pcd).grid(row=13,column=0,sticky="W")
foodnpcd=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_33)
foodnpcd.grid(row=13,column=1,sticky="w")

foodv65=Checkbutton(root,text="🥗 Veg 65 Dry\t\t₹120",variable=var34,font=" helvetica 10",command=food_v65).grid(row=14,column=0,sticky="W")
foodnv65=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_34)
foodnv65.grid(row=14,column=1,sticky="w")

foodcchilly=Checkbutton(root,text="🥗 Chicken Chilly\t\t₹160",variable=var35,font=" helvetica 10",command=food_cchilly).grid(row=15,column=0,sticky="W")
foodncc=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_35)
foodncc.grid(row=15,column=1,sticky="w")

# foodcmd=Checkbutton(root,text="Chicken Manchurian Dry\t₹130",variable=var36,font=" helvetica 10",command=food_cmd).grid(row=16,column=0,sticky="W")
# foodnmcd=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_36)
# foodnmcd.grid(row=16,column=1,sticky="w")

# foodccrispy=Checkbutton(root,text="Chicken Crispy\t\t₹140",variable=var37,font=" helvetica 10",command=food_ccrispy).grid(row=17,column=0,sticky="W")
# foodnccrispy=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_37)
# foodnccrispy.grid(row=17,column=1,sticky="w")

# foodcl=Checkbutton(root,text="Chicken Lollypop\t\t₹110",variable=var38,font=" helvetica 10",command=food_clolly).grid(row=18,column=0,sticky="w")
# foodncl=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_38)
# foodncl.grid(row=18,column=1,sticky="w")

# foodcs=Checkbutton(root,text="Chicken Sukha\t\t₹130",variable=var39,font=" helvetica 10",command=food_csukha).grid(row=19,column=0,sticky="W")
# foodncs=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_39)
# foodncs.grid(row=19,column=1,sticky="w")

# foodms=Checkbutton(root,text="Mutton Sukha\t\t₹120",variable=var310,font=" helvetica 10",command=food_msukha).grid(row=20,column=0,sticky="W")
# foodnmsukha=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_310)
# foodnmsukha.grid(row=20,column=1,sticky="w")

# foodfk=Checkbutton(root,text="Fish Koliwada\t\t₹190",variable=var311,font=" helvetica 10",command=food_fkoli).grid(row=16,column=0,sticky="W")
# foodnfk=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_311)
# foodnfk.grid(row=16,column=1,sticky="w")


#Breads
foodchapati=Checkbutton(root,text="🫓 Chapati\t\t\t₹10",variable=var51, font="helvetica 10",command=food_chapati).grid(row=11,column=2,sticky="w")
foodnchapati=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_51)
foodnchapati.grid(row=11,column=3)

foodtroti=Checkbutton(root,text="🫓 tandoori Roti\t\t₹15",variable=var52 , font="helvetica 10",command=food_troti).grid(row=12,column=2,sticky="w")
foodntroti=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_52)
foodntroti.grid(row=12,column=3)

foodnaan=Checkbutton(root,text="🫓 Naan\t\t\t₹25",variable=var53, font="helvetica 10",command=food_naan).grid(row=13,column=2,sticky="w")
foodnnaan=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_53)
foodnnaan.grid(row=13,column=3)

foodbnaan=Checkbutton(root,text="🫓 Butter Naan\t\t₹30",variable=var54, font="helvetica 10",command=food_bnaan).grid(row=14,column=2,sticky="w")
foodnbnaan=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_54)
foodnbnaan.grid(row=14,column=3)

foodkulcha=Checkbutton(root,text="🫓 Kulcha\t\t\t₹30",variable=var55, font="helvetica 10",command=food_kulcha).grid(row=15,column=2,sticky="w")
foodnkulcha=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_55)
foodnkulcha.grid(row=15,column=3)

foodbkulcha=Checkbutton(root,text="🫓 Butter Kulcha\t\t₹35",variable=var56, font="helvetica 10",command=food_bkulcha).grid(row=16,column=2,sticky="w")
foodnbkulcha=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_56)
foodnbkulcha.grid(row=16,column=3)

#Rice


foodjeera=Checkbutton(root,text="🍚 Jeera Rice\t\t₹80",variable=var61, font="helvetica 10",command=food_jeera).grid(row=4,column=4,sticky="w")
foodnjeera=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_61)
foodnjeera.grid(row=4,column=5)

foodcurd=Checkbutton(root,text="🍚 Curd Rice\t\t₹50",variable=var62, font="helvetica 10",command=food_curd).grid(row=5,column=4,sticky="w")
foodncurd=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_62)
foodncurd.grid(row=5,column=5)

foodrajma=Checkbutton(root,text="🍚 Rajma Rice\t\t₹100",variable=var63 , font="helvetica 10",command=food_rajma).grid(row=6,column=4,sticky="w")
foodnrajma=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_63)
foodnrajma.grid(row=6,column=5)

foodvegpulav=Checkbutton(root,text="🍚 Veg Pulav\t\t₹120",variable=var64 , font="helvetica 10",command=food_vegpulav).grid(row=7,column=4,sticky="w")
foodnvpulav=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_64)
foodnvpulav.grid(row=7,column=5)

foodvegbir=Checkbutton(root,text="🍚 Veg Biryani\t\t₹120",variable=var65 , font="helvetica 10",command=food_vegbir).grid(row=8,column=4,sticky="w")
foodnvbir=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_65)
foodnvbir.grid(row=8,column=5)

foodcbir=Checkbutton(root,text="🍚 Chicken Biryani\t\t₹120",variable=var66, font="helvetica 10",command=food_cbir).grid(row=9,column=4,sticky="w")
foodncbir=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_66)
foodncbir.grid(row=9,column=5)

# foodmbir=Checkbutton(root,text="\t🍚 Mutton Biryani\t\t₹150",variable=var67, font="helvetica 10",command=food_mbir).grid(row=4,column=6,sticky="w")
# foodnmbir=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_67)
# foodnmbir.grid(row=4,column=7)

# foodfish=Checkbutton(root,text="\tPrawns Rice\t\t₹160",variable=var68, font="helvetica 10",command=food_fish).grid(row=5,column=6,sticky="w")
# foodnfish=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_68)
# foodnfish.grid(row=5,column=7)

# #Beverages
# Checkbutton(root,text="Lassi",variable=var , font="helvetica 10").grid(row=,column=,sticky="w")
# Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_).grid(row=,column=)
# Checkbutton(root,text="Mango Milk",variable=var , font="helvetica 10").grid(row=,column=,sticky="w")
# Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_).grid(row=,column=)
# Checkbutton(root,text="Soft Drink",variable=var , font="helvetica 10").grid(row=,column=,sticky="w")
# Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_).grid(row=,column=)
# Checkbutton(root,text="Butter Milk",variable=var , font="helvetica 10").grid(row=,column=,sticky="w")
# Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_).grid(row=,column=)
# Checkbutton(root,text="Mineral Water",variable=var , font="helvetica 10").grid(row=,column=,sticky="w")
# Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_).grid(row=,column=)
# Checkbutton(root,text="Masala Chhach",variable=var , font="helvetica 10").grid(row=,column=,sticky="w")
# Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_).grid(row=,column=)
# Checkbutton(root,text="",variable=var , font="helvetica 10").grid(row=,column=,sticky="w")
# Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_).grid(row=,column=)
# Checkbutton(root,text="",variable=var , font="helvetica 10").grid(row=,column=,sticky="w")
# Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_).grid(row=,column=)



Button(root,text="    Total    ",font="Arial 10 bold",borderwidth=3,relief=RAISED,command=totalbill).grid(row=13,column=4)

Entry(root,textvariable=total,width=10,).grid(row=13,column=5,sticky="w")

# Label(root,text="  Delivery Charges= ₹20 ",font="Arial 10 bold").grid(row=14,column=4)

Button(root,text="    Reset    ",font="Arial 10 bold",borderwidth=3,relief=RAISED,command=reset,bg="blue",fg="white").grid(row=16,column=4)

Button(root,text="    Exit    ",font="Arial 10 bold",borderwidth=3,relief=RAISED,command=closewindow,bg="red",fg="white").grid(row=19,column=4)


#adding ClientName
Label(root,text="ClientName",font="arial 11 bold").grid(row=10,column=6,sticky="w")
Entry(root,textvariable=ClientName,width=50,justify="left").grid(row=11,column=6,sticky="w")
#adding mobile number
Label(root,text="Mobile Number",font="arial 11 bold").grid(row=13,column=6,sticky="w")
Entry(root,textvariable=mobile,width=30,justify="left").grid(row=14,column=6,sticky="w")

# Label(root,text='    Change    ',font="arial 10 bold",borderwidth=3,relief=RAISED).grid(row=15,column=4)
# Entry(root,textvariable=change,font="arial 10 bold").grid(row=15,column=5,sticky="w")

import random

def closewindow2():
    ex=tmsg.askyesno("Notification","Do you want to order?")
    if ex>0:
        import os
        from InvoiceGenerator.api import Invoice,Item,Client,Provider,Creator
        from InvoiceGenerator.pdf import SimpleInvoice

        bank_acc = random.randint(2335,2999)
        bank_acc = str(bank_acc)+'-3324-3453-'+str(bank_acc)

        bank_code = random.randint(4506,5506)
        bank_code = str(bank_code)
        os.environ['INVOICE_LANG'] = 'en'
        client = Client('Name: {}'.format(ClientName.get(),mobile.get()))
        provider = Provider("TEAM 02",bank_account = bank_acc,bank_code=bank_code)
        creator = Creator('TEAM_140_151_166_177 02')
        invoice = Invoice(client,provider,creator)
        for i in range(len(res)):
            print(res[i])
            invoice.add_item(Item(q[i],price[i],description=res[i]))
        # invoice.add_item(Item(13,460,description='Fruit'))
        # invoice.add_item(Item(10,290,description='Milk'))
        # invoice.add_item(Item(3,165,description='Fruit'))

        invoice.currency = 'RS.'
        num = random.randint(10,50)
        invoice.number = str(num)+str(num)+str(num)

        docu = SimpleInvoice(invoice)
        pdf_n0 = random.randint(1,10)
        pdf_n0_str = str(pdf_n0)
        gen_pdf = pdf_n0_str+'.pdf'
        print(gen_pdf)
        docu.gen(gen_pdf,generate_qr_code=True) 


        return


    


Button(root,text="Place Order",font="arial 10 bold",borderwidth=3,relief=RAISED,command=closewindow2,bg="green",fg="white" ).grid(row=18,column=5)

root.mainloop()


from tkinter import *

import time



app = Tk()
app.geometry("400x700")

canvas = Canvas(app,bg='blue')

canvas.pack(anchor='nw',fill='both',expand=1)




# file player
x_list =[]
y_list=[]
prev_x = -1
prev_y = -1

ix,iy= 0,0
def get_x_and_y():
    global prev_x,prev_y,ix,iy
    prev_x ,prev_y = x_list[0],y_list[0]
    ix=ix+1
    iy=iy+1

def draw_line():
    global prev_x,prev_y,ix,iy
    canvas.create_line(int(prev_x),int(prev_y),int(x_list[ix]),int(y_list[iy]))
    prev_x ,prev_y = x_list[ix],y_list[iy]
    ix=ix+1
    iy=iy+1

def animate():
    if(ix==len(x_list)):
        return
    draw_line()
    app.after(50,animate)
    # if(ix!=len(x_list)):
    #     animate()

def play():
    global x_list,y_list
    # f= open("test.ap","r")
    # ls = str(f.read()).split("\n")
    # ls[0]=ls[0].replace('[',"")
    # ls[0]=ls[0].replace(']',"")
    # ls[1]=ls[1].replace('[',"")
    # ls[1]=ls[1].replace(']',"")

    # x_list=ls[0].split(",")
    # y_list=ls[1].split(",")
    # print(ls[2])
    # print(len(ls))
    # V_Text.insert(END,ls[2])
    # f.close()
    
   
    
    get_x_and_y()
    
    animate()


    print(x_list)
    print("/"*100)
    print(x_list[0])
    print(type(x_list[0]))
    print(y_list)


            


play_button = Button(
    app,
    text='Play',
    command=play
)
play_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

V_Text = Text(app,width= 400,height=200,)
V_Text.pack(pady=20)


# following code will read data from the file 
f= open("test.ap","r")
ls = str(f.read()).split("\n")
ls[0]=ls[0].replace('[',"")
ls[0]=ls[0].replace(']',"")
ls[1]=ls[1].replace('[',"")
ls[1]=ls[1].replace(']',"")

x_list=ls[0].split(",")
y_list=ls[1].split(",")
print(ls[2])
print(len(ls))
V_Text.insert(END,ls[2])
f.close()




app.mainloop()

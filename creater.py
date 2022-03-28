from tkinter import * 



app = Tk()
app.geometry("400x400")

canvas = Canvas(app,bg='blue')

canvas.pack(anchor='nw',fill='both',expand=1)

# importent global variables
prev_x =-1
prev_y = -1
x_list=[]
y_list=[]
ix =0
iy=0


def get_x_and_y(event):
    global prev_x,prev_y,ix,iy
    prev_x ,prev_y = event.x,event.y
    x_list.append(prev_x)
    y_list.append(prev_y)

def draw_line(event):
    global prev_x,prev_y,ix,iy
    canvas.create_line(prev_x,prev_y,event.x,event.y)
    prev_x ,prev_y = event.x,event.y
    if abs(x_list[ix]-event.x)>2:
        x_list.append(prev_x)
        ix=ix+1
        y_list.append(prev_y)
        iy=iy+1
   
    elif abs(y_list[iy]-event.y)>0.005:
        
        x_list.append(prev_x)
        ix=ix+1
        y_list.append(prev_y)
        iy=iy+1
        

        # y_list.append(prev_y)
        # print(y_list)


# save button feature
def save():
    f =open("test.ap","a")
    f.write(str(x_list)+"\n"+str(y_list))
    f.close()
    

save_button = Button(
    app,
    text='Save',
    command=save
)
save_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)




canvas.bind("<Button-1>",get_x_and_y)
canvas.bind("<B1-Motion>",draw_line)


app.mainloop()


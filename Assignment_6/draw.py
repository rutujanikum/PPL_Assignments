from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox


class Paint():
    def __init__(self, root):
        self.root = root
        self.root.title("paint")
        self.root.geometry("800x520")
        self.root.configure(background="white")
        self.root.resizable(0,0)

        self.pen_color = "black"
        self.eraser_color = "white"
        #adding widges to paint

        self.color_frame = LabelFrame(self.root,text='Color',font = ('Times New Roman',15),bd=5,relief=RIDGE,bg="white")
        self.color_frame.place(x=0,y=0,width=70,height=195)
        colors = ['red','black','pink','blue','grey','cyan','brown','yellow','purple','hotpink','green','olive','plum','indigo']
        i=j=0
        for color in colors:
            Button(self.color_frame,bg=color,bd=1,relief=RIDGE,width=3,command=lambda col =color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==7:
                i=0
                j+=1
        self.eraser_button = Button(self.root,text="ERASER",bd=4,bg="white",command=self.eraser,width=8,relief=RIDGE)
        self.eraser_button.place(x=0,y=192)

        self.clear_button = Button(self.root, text="CLEAR", bd=4, bg="white", command=lambda : self.canvas.delete("all"), width=8, relief=RIDGE)
        self.clear_button.place(x=0, y=222)

        self.save_button = Button(self.root, text="SAVE", bd=4, bg="white", command=None, width=8, relief=RIDGE)
        self.save_button.place(x=0, y=252)

        self.canvas_color_button = Button(self.root, text="FILL", bd=4, bg="white", command=self.canvas_color, width=8, relief=RIDGE)
        self.canvas_color_button.place(x=0, y=282)

        #creating a Scale for pen and Eraser Size

        self.pen_size_scale_frame = LabelFrame(self.root,text="size",bd=5,bg="white",font=('Times New Roman',15,'bold'),relief=RIDGE)
        self.pen_size_scale_frame.place(x=0,y=313,height=200,width=70)

        self.pen_size = Scale(self.pen_size_scale_frame,orient=VERTICAL,from_=50,to=0,length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0,column=1,padx=15)

        #creating canvas

        self.canvas = Canvas(self.root,bg="white",bd=5,relief=GROOVE,height=500,width=700)
        self.canvas.place(x=80,y=0)

        #bind canvas with mouse drag
        self.canvas.bind("<B1-Motion>",self.paint)

    #functions

    def paint(self,event):
        x1,y1 = (event.x-2),(event.y-2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1,y1,x2,y2,fill=self.pen_color,outline=self.pen_color,width=self.pen_size.get())

    def select_color(self, col):
        self.pen_color = col

    def eraser(self):
        self.pen_color = self.eraser_color

    def canvas_color(self):
        color = colorchooser.askcolor()
        self.canvas.configure(background=color[1])
        self.eraser_color = color[1]

if __name__ == "__main__":
    root = Tk()
    p = Paint(root)
    root.mainloop()

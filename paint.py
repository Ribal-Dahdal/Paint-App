from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image,ImageColor
import numpy as np
import matplotlib as mp
import cv2
class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title('Paint')
        self.root.geometry('1200x800')
        self.root.maxsize(1920,1080)
        self.root.minsize(500,300)
        self.original_image=0
        self.edited_image=0
        self.filtered_image=0
        self.img = PhotoImage('pen.png')  
 
        self.paint_tools = Frame(self.root,width=250,height=600,relief=RIDGE,borderwidth=2)
        self.paint_tools.place(x=0,y=0)

        self.upload_logo = ImageTk.PhotoImage(Image.open('pen.png'))
        self.p = Label(self.paint_tools, text="Upload",borderwidth=0,font=('verdana',10,'bold'))
        self.p.place(x=50,y=15)
        self.pen_button = Button(self.paint_tools,padx=6,image=self.upload_logo,borderwidth=2,command=self.upload_action)
        self.pen_button.place(x=5,y=10)

        self.brush_logo = ImageTk.PhotoImage(Image.open('brush.png'))
        self.b = Label(self.paint_tools,borderwidth=0,text='brush',font=('verdana',10,'bold'))
        self.b.place(x=50,y=45)
        self.brush_button = Button(self.paint_tools,image = self.brush_logo,borderwidth=2,command=self.draw_action) 
        self.brush_button.place(x=5,y=40)

        self.color_logo = ImageTk.PhotoImage(Image.open('color.png'))
        self.cl = Label(self.paint_tools, text='color',font=('verdana',10,'bold'))
        self.cl.place(x=50,y=75)
        self.color_button = Button(self.paint_tools,image = self.color_logo,borderwidth=2,command=self.choose_color)
        self.color_button.place(x=5,y=70)

        self.eraser_logo = ImageTk.PhotoImage(Image.open('eraser.png'))
        self.e = Label(self.paint_tools, text='eraser',font=('verdana',10,'bold'))
        self.e.place(x=50,y=105)
        self.eraser_button = Button(self.paint_tools,image = self.eraser_logo,borderwidth=2,command=self.erasef)
        self.eraser_button.place(x=5,y=100)
        
        self.rrotate_logo = ImageTk.PhotoImage(Image.open('right.png').resize((30,30)))
        self.e = Label(self.paint_tools, text='right rotate',font=('verdana',10,'bold'))
        self.e.place(x=50,y=135)
        self.eraser_button = Button(self.paint_tools,image = self.rrotate_logo,borderwidth=2,command=self.rotate_right_action)
        self.eraser_button.place(x=5,y=130)
        
        self.rotateleft_logo = ImageTk.PhotoImage(Image.open('left.png').resize((30,30)))
        self.rl = Label(self.paint_tools, text='left rotate',font=('verdana',10,'bold'))
        self.rl.place(x=50,y=165)
        self.rl_button = Button(self.paint_tools,image = self.rotateleft_logo,borderwidth=2,command=self.rotate_left_action)
        self.rl_button.place(x=5,y=160)
        
        self.translate_logo = ImageTk.PhotoImage(Image.open('translate.png').resize((30,30)))
        self.translateimg = Label(self.paint_tools, text='Translate',font=('verdana',10,'bold'))
        self.translateimg.place(x=50,y=195)
        self.translateimg_button = Button(self.paint_tools,image = self.translate_logo,borderwidth=2,command=self.translate)
        self.translateimg_button.place(x=5,y=190)


        self.bigger_logo = ImageTk.PhotoImage(Image.open('bigger.png').resize((30,30)))
        self.biggerimg = Label(self.paint_tools, text='Bigger',font=('verdana',10,'bold'))
        self.biggerimg.place(x=50,y=225)
        self.biggerimg_button = Button(self.paint_tools,image = self.bigger_logo,borderwidth=2,command=self.scale_bigger)
        self.biggerimg_button.place(x=5,y=220)
        
        self.smaller_logo = ImageTk.PhotoImage(Image.open('smaller.png').resize((30,30)))
        self.smallerimg = Label(self.paint_tools, text='Smaller',font=('verdana',10,'bold'))
        self.smallerimg.place(x=50,y=255)
        self.smallerimg_button = Button(self.paint_tools,image = self.smaller_logo,borderwidth=2,command=self.scale_smaller)
        self.smallerimg_button.place(x=5,y=250)

        self.skew_logo = ImageTk.PhotoImage(Image.open('eraser.png').resize((30,30)))
        self.skewimg = Label(self.paint_tools, text='Skew',font=('verdana',10,'bold'))
        self.skewimg.place(x=50,y=285)
        self.skewimg_button = Button(self.paint_tools,image = self.skew_logo,borderwidth=2,command=self.skew)
        self.skewimg_button.place(x=5,y=280)
        
        self.save_logo = ImageTk.PhotoImage(Image.open('eraser.png').resize((30,30)))
        self.saveimg = Label(self.paint_tools, text='wrapx',font=('verdana',10,'bold'))
        self.saveimg.place(x=50,y=315)
        self.saveimg_button = Button(self.paint_tools,image = self.rotateleft_logo,borderwidth=2,command=self.wrapx)
        self.saveimg_button.place(x=5,y=310)
        
        self.save_logo = ImageTk.PhotoImage(Image.open('eraser.png').resize((30,30)))
        self.saveimg = Label(self.paint_tools, text='wrapy',font=('verdana',10,'bold'))
        self.saveimg.place(x=50,y=345)
        self.saveimg_button = Button(self.paint_tools,image = self.rotateleft_logo,borderwidth=2,command=self.wrapy)
        self.saveimg_button.place(x=5,y=340)
        
        
        self.save_logo = ImageTk.PhotoImage(Image.open('eraser.png').resize((30,30)))
        self.saveimg = Label(self.paint_tools, text='save',font=('verdana',10,'bold'))
        self.saveimg.place(x=50,y=375)
        self.saveimg_button = Button(self.paint_tools,image = self.rotateleft_logo,borderwidth=2,command=self.save_action)
        self.saveimg_button.place(x=5,y=370)
        
        
        self.pen_size = Label(self.paint_tools,text="Brush Size",font=('verdana',10,'bold'))
        self.pen_size.place(x=15,y=520)
        self.choose_size_button = Scale(self.paint_tools, from_=1, to=20, orient=VERTICAL)
        self.choose_size_button.place(x=20,y=420)
        

        self.c = Canvas(self.root ,height=1000,width=1000)
        self.c.place(x=250,y=0)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.c.create_image(100,100,anchor=NW,image=self.img)
        self.c.image = self.img 
        self.line_width = self.choose_size_button.get()
        self.color_code = self.DEFAULT_COLOR
        self.erase = False
        self.active_button = self.brush_button
        
        # self.c.bind('<B1-Motion>', self.paint)
        # self.c.bind('<ButtonRelease-1>', self.reset)

    # def use_pen(self):
    #     self.activate_button(self.pen_button)

    # def use_brush(self):
    #     self.activate_button(self.brush_button)

    # def choose_color(self):
    #     self.eraser_on = False
    #     self.color = askcolor(color=self.color)[1]

    # de f use_eraser(self):
    #     self.activate_button(self.eraser_button, eraser_mode=True)

    # def activate_button(self, some_button, eraser_mode=False):
    #     self.active_button.config(relief=RAISED)
    #     some_button.config(relief=SUNKEN)
    #     self.active_button = some_button
    #     self.eraser_on = eraser_mode

    # def paint(self, event):
    #     self.line_width = self.choose_size_button.get()
    #     paint_color = 'white' if self.eraser_on else self.color
    #     if self.old_x and self.old_y:
    #         self.c.create_line(self.old_x, self.old_y, event.x, event.y,
    #                            width=self.line_width, fill=paint_color,
    #                            capstyle=ROUND, smooth=TRUE, splinesteps=36)
    #     self.old_x = event.x
    #     self.old_y = event.y
    def erasef(self):
        self.erase=True
    
    def draw_action(self):
        self.c.bind("<ButtonPress>", self.start_draw)
        self.c.bind("<B1-Motion>", self.draw)

    def choose_color(self):
        self.color_code = askcolor(color=self.color_code)[1]

    def start_draw(self, event):
        self.x = event.x
        self.y = event.y
        self.draw_ids = []
         
    
    def draw(self, event):
        # print(self.draw_ids)
        if self.erase:
                    self.line_width = self.choose_size_button.get()
                    self.draw_ids.append(self.c.create_line(self.x, self.y, event.x, event.y, width=self.line_width,
                                                                fill='#ffffff', capstyle=ROUND, smooth=True))
                    cv2.line(self.filtered_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
                            (int(event.x * self.ratio), int(event.y * self.ratio)),
                            (255,255,255) , thickness=self.line_width,
                            lineType=8)
                    self.x = event.x
                    self.y = event.y
        else:
                    self.line_width = self.choose_size_button.get()
                    self.draw_ids.append(self.c.create_line(self.x, self.y, event.x, event.y, width=self.line_width,
                                                                fill=self.color_code, capstyle=ROUND, smooth=True))
                    RGB = ImageColor.getcolor(self.color_code,'RGB')
                    R= RGB[0]
                    G= RGB[1]
                    B= RGB[2]
                    cv2.line(self.filtered_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
                            (int(event.x * self.ratio), int(event.y * self.ratio)),
                            (B,G,R) , thickness=self.line_width,
                            lineType=8)
                    self.x = event.x
                    self.y = event.y
    
    # def refresh_side_frame(self):
    #     try:
    #         self.side_frame.grid_forget()
    #     except:
    #         pass
    #     self.c.unbind("<ButtonPress>")
    #     self.c.unbind("<B1-Motion>")
    #     self.c.unbind("<ButtonRelease>")
    #     self.display_image(self.filtered_image)
    #     self.side_frame = self.brush_button.Frame(self.frame_menu)
    #     self.side_frame.grid(row=0, column=4, rowspan=10)
    #     self.side_frame.config(relief=GROOVE, padding=(50, 15))
        
        
    def upload_action(self):
        self.c.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)
        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        self.display_image(self.edited_image)
        
        
    def rotate_left_action(self):
        self.filtered_image = cv2.rotate(
            self.filtered_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.display_image(self.filtered_image)


    def rotate_right_action(self):
        self.filtered_image = cv2.rotate(
            self.filtered_image, cv2.ROTATE_90_CLOCKWISE)
        self.display_image(self.filtered_image)
    
    
    def scale_smaller(self):
        # height, width = self.filtered_image.shape[:2]
        self.filtered_image = cv2.resize(self.filtered_image, None, fx = 0.8, fy = 0.8)
        self.display_image(self.filtered_image)
       
       
    def wrapx(self):
        # height, width = self.filtered_image.shape[:2]
        self.filtered_image = cv2.resize(self.filtered_image, None, fx = 1.2, fy = 1)
        self.display_image(self.filtered_image)
        
    def wrapy(self):
        # height, width = self.filtered_image.shape[:2]
        self.filtered_image = cv2.resize(self.filtered_image, None, fx = 1, fy = 1.2)
        self.display_image(self.filtered_image)
       
       
       
       
    def scale_bigger(self):
        # height, width = self.filtered_image.shape[:2]
        self.filtered_image = cv2.resize(self.filtered_image, None, fx = 1.2, fy = 1.2)
        self.display_image(self.filtered_image)
       
       
    def translate(self):
        
        height, width = self.filtered_image.shape[:2]
        quarter_height, quarter_width = height / 4, width / 4
        T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
        self.filtered_image = cv2.warpAffine(self.filtered_image, T, (width, height))
        self.display_image(self.filtered_image)
       
       
    def skew(self):
        rows, cols,c= self.filtered_image.shape
        M = np.float32([[1, 0.5, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])          
        self.filtered_image = cv2.warpPerspective(self.filtered_image,M,(int(cols*1.5),int(rows*1.5)))
        self.display_image(self.filtered_image)
        
    
    def display_image(self, image=None):
        self.c.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width , channel = image.shape
        ratio = height / width

        new_width = width
        new_height = height

        # if height > 400 or width > 300:
        #     if ratio < 1:
        #         new_width = 300
        #         new_height = int(new_width * ratio)
        #     else:
        #         new_height = 400
        #         new_width = int(new_height * (width / height))

        self.ratio = height / new_height
        self.new_image = cv2.resize(image, (new_width, new_height))

        self.new_image = ImageTk.PhotoImage(
            Image.fromarray(self.new_image))

        self.c.config(width=new_width, height=new_height)
        self.c.create_image(
            new_width / 2, new_height / 2,  image=self.new_image)
        
    def save_action(self):
        original_file_type = self.filename.split('.')[-1]
        filename = filedialog.asksaveasfilename()
        filename = filename + "." + original_file_type

        save_as_image = self.filtered_image
        cv2.imwrite(filename, save_as_image)
        self.filename = filename
        
    # def reset(self, event):
    #     self.old_x, self.old_y = None, None

Paint()
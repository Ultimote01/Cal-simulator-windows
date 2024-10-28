from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
import os,time, keyboard


hm_dir=os.path.expanduser('~')
print(hm_dir)
class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master = master
        self.canvas = Canvas(self, width=15)
        row_num = [i for i in range(1, 11)]
        column_num = [i for i in range(4)]
        self.configure(background='#151515')
        self.pack(fill='both', expand=True)
        self.grid_rowconfigure(0, weight=1, uniform='true')
        self.grid_columnconfigure((0), weight=1)
        self.main = Frame(self, background='#151515', width=18, highlightbackground='#151515', bd=0)
        self.main.grid(row=0, column=0, sticky='nsew')
        self.main.grid_rowconfigure(tuple(row_num), weight=1, uniform='true')
        self.main.grid_columnconfigure(tuple(column_num), weight=1, uniform='false')
        self.main1 = Frame(self,bg='#151515',highlightbackground='#151515')
        self.bind("<Configure>", self.half_frame)
        self.canvas1 = Canvas(self.main1, bg='#151515',highlightbackground='#151515',height=20,width=20)
        self.canvas1.pack(fill='both', expand=True)
        self.label1 = Label(self.canvas1, text=' ',bg='#151515',height=0)
        self.label1.grid(row=0, column=2)
        self.numx =0
        self.t_tags=''
        self.number=[0,0]
        image= [Image.open(hm_dir+"\\Pictures\\project_images\\"+file) for file in os.listdir(hm_dir+"\\Pictures\\project_images\\")]

        resized_image=[file.resize((16,16),Image.BICUBIC) for file in image]
        self.photo = [ImageTk.PhotoImage(file) for file in resized_image]
        self.photo1=[ImageTk.PhotoImage((i.resize((11,11),Image.BICUBIC),x)[0]) for i,x in zip(image,range(len(image)))
                     if x == 5]
        self.dup_image = [ImageTk.PhotoImage((i.resize((10, 10), Image.BICUBIC), x)[0]) for i, x in
                       zip(image, range(len(image)))if x == 8]

        self.tag_list=['mc','mr','m+','m-','mx','m','%','ce','c','bk','1/*','*2','rootx',
                       '/','7','8','9','*','4','5','6','-','1','2','3','+','+/-','0','.','=']

        self.tag_list1 = ['xlider','label','ovr_button','hixtory','rectangle','rec1','display','history','memory']
        self.c_width = 0
        self.c_height = 0
        self.switch = False
        self.create_widgets()
        self.second_f_canvas()
        keyboard.hook(self.on_key_event)
        self.status, self.clear_it, self.auto_equal, self.checker, self.correct = '', False, [], '', True
        self.eqclear, self.record, self.record1, self.memory, self.display_v = True, '', '', '', ''
        self.conn, self.permit, self.last_in, self.last_entry, self.counter = False, True, [], '', 0
        self.var = ''
        self.expand_count=0
        self.master.bind("<Key>",self.change_window_size)
        self.keys=''
        self.kount=600

    def change_window_size(self,event):
         
        if event.keysym == 'Control_L':
           self.keys+=event.keysym
        elif event.keysym == 's':
             self.keys+=event.keysym
        if self.keys == 'Control_Ls':
           self.keys=''
           def expansion():
               if self.kount == 600:
                  self.master.geometry(f"{800}x{480}+550+100")
                  self.kount = 320
               elif self.kount == 320:
                   self.master.geometry(f"{320}x{480}+850+100")
                   self.kount=600 
               self.master.after(100,expansion)
           expansion()
     
    def half_frame(self, event):

        if event.width > 600 and event.width < 1360:

            self.label1.configure(width=40)
            self.main1.grid(row=0, column=1, sticky='nsew')

        elif event.width > 1360:
            self.label1.configure(width=50)
            self.main1.grid(row=0, column=1, sticky='nsew')


        elif event.width < 600:
            if self.main1.winfo_viewable():
                self.main1.grid_remove()


        if event.width < int(window_width) or event.height < int(window_height):
            #self.master.minsize(int(window_width), int(window_height))
            #self.master.maxsize()
            k=0

    def create_widgets(self):

        self.f_canvas=Canvas(self.main,bg='#151515',highlightbackground='#151515',height=15,bd=0)
        self.f_canvas.grid(row=0,rowspan=4,column=0,columnspan=4,sticky='nsew',padx=0,pady=0)
        self.f_canvas.bind("<Leave>", lambda event: self.on_canvas_leave('canvas'))
        self.f_canvas.bind("<Configure>", self.create_buttons1)


        self.nxt_canvas = Canvas(self.main,bg='#151515',highlightbackground='#151515',height=15,bd=0)
        self.nxt_canvas.grid(row=4,rowspan=8,column=0,columnspan=4,sticky='nsew',padx=2,pady=0)
        self.nxt_canvas.bind("<Configure>", self.create_buttons)
        self.nxt_canvas.bind("<Leave>", lambda event: self.on_canvas_leave('canvas'))
        self.master.bind("<KeyPress>", self.on_canvas_unclick)





    def on_canvas_click(self,event):

        if not isinstance(event, str):
            clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
            for item_id in clicked_items:
                tags = event.widget.gettags(item_id)  # Get all tags associated with the item
                xem = tags[0] if 's' not in tags[0] else ''  #
                if xem == 'tag=':
                    self.nxt_canvas.itemconfigure(xem, activefill='#4bc1c5')
                elif xem == 'tagxlider':
                    self.f_canvas.delete(xem + 's')
                    self.create_rounded_button(self.f_canvas, 2, 7, 40, 50, 5, '#151515', '#4a4a49', self.tag_list1[0]
                                               , "lightgrey", self.dup_image[0], 'canvas0')
                else:
                    self.nxt_canvas.itemconfigure(xem, activefill='#202020')
                    self.f_canvas.itemconfigure(xem, activefill='#202020')

                if tags[0] != xem:
                    tag = tags[0].replace('s', '')
                    if tag == 'tag=':
                        self.nxt_canvas.itemconfigure(tag, fill='#4bc1c5')

                    elif tag == 'tagxlider':
                        self.f_canvas.delete(tag + 's')
                        self.create_rounded_button(self.f_canvas, 2, 7, 40, 50, 5, '#151515', '#4a4a49',
                                                   self.tag_list1[0]
                                                   , "lightgrey", self.dup_image[0], 'canvas0')
                    else:
                        self.nxt_canvas.itemconfigure(tag, fill='#202020')
                        self.f_canvas.itemconfigure(tag, fill='#202020')

    def on_canvas_unclick(self,event):
        global text


        x = str(event)
        if not isinstance(event,str) and 'KeyPress' not in x:

            clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
            for item_id in clicked_items:
                tags = event.widget.gettags(item_id)  # Get all tags associated with the item
                xem = tags[0] if 's' not in tags[0] else ''

                if xem == 'tag=':
                    self.nxt_canvas.itemconfigure(xem, activefill='#57dbe0')
                elif xem == 'tagxlider':
                    self.f_canvas.delete(xem + 's')
                    self.create_rounded_button(self.f_canvas, 2, 7, 40, 50, 5, '#151515', '#4a4a49', self.tag_list1[0]
                                               , "lightgrey", self.photo[8], 'canvas0')
                else:
                    self.nxt_canvas.itemconfigure(xem, activefill='#4a4a49')
                    self.f_canvas.itemconfigure(xem, activefill='#4a4a49')

                # This code retrieve items tags for processing
                if 'ButtonRelease' in x:
                    z = ''
                    y = list('tags')
                    for i in tags[0]:
                        if i not in y:
                            z+=i
                    if z in [ '7', '8', '9', '4', '5', '6', '1', '2', '3', '0','.']:

                        self.display(z,True)
                    elif z == 'bk':
                        self.backspace()
                    elif z in ['/','1/*','*','mc','mr','m+','m-','mx','m','%','ce','c','=','+','-','1/*','*2','roox','.']:
                        self.display(z,False)



                if tags[0] != xem:

                    #create activefill for buttons when text is clicked
                    tag = tags[0].replace('s','')

                    if tag == 'tag=':
                        self.nxt_canvas.itemconfigure(tag, fill='#57dbe0')
                    elif tag == 'tagxlider' and 'ButtonRelease' in str(event):
                        self.f_canvas.delete(tag+'s')
                        self.create_rounded_button(self.f_canvas, 2, 7, 40, 50, 5, '#151515', '#4a4a49',
                                                   self.tag_list1[0], "lightgrey", self.photo[8], 'canvas0')
                    else:
                        self.nxt_canvas.itemconfigure(tag, fill='#4a4a49')
                        self.f_canvas.itemconfigure(tag, fill='#4a4a49')

                    if self.t_tags and self.t_tags != tag:
                        self.nxt_canvas.itemconfigure(self.t_tags,fill='#2c2c2b')

                if not "Enter" in str(event):
                    value = tags[0].replace('tags','') if 'tags' in tags[0] else tags[0].replace('tag','')

        elif 'KeyPress'  in x:
            if event.char in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.']:

                notification.notify(
                    title="System Information",
                    message=f'Battery Full\nRemove charger to safe energy',
                    timeout=35
                )
                self.var = event.char
                self.display(event.char, True)

            elif  event.keysym == 'BackSpace':
                self.var = 'bk'
                self.backspace()

            elif event.char in ['/','+','-','=','*']:
                self.var = event.char
                self.display(event.char, False)

            elif event.keysym == 'Return':
                self.var='='
                self.display('=', False)

            elif event.keysym == 'Escape':

                self.display('c',False)





    def on_canvas_leave(self,event):

        if not isinstance(event,str):
            clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
            for item_id in clicked_items:
                tags = event.widget.gettags(item_id)  # Get all tags associated with the item
                xem = tags[0] if 's' not in tags[0] else ''
                xem_x = tags[0] if 's'  in tags[0] else ''
                if xem == 'tag=':
                    self.nxt_canvas.itemconfigure(xem, fill='#58f7fd')
                elif xem == 'tagmc':
                    self.nxt_canvas.itemconfigure(xem, fill='#151515')
                elif xem == 'tagmr':
                    self.nxt_canvas.itemconfigure(xem, fill='#151515')
                elif xem == 'tagm+':
                    self.nxt_canvas.itemconfigure(xem, fill='#151515')
                elif xem == 'tagm-':
                    self.nxt_canvas.itemconfigure(xem, fill='#151515')
                elif xem == 'tagmx':
                    self.nxt_canvas.itemconfigure(xem, fill='#151515')
                elif xem == 'tagm':
                    self.nxt_canvas.itemconfigure(xem, fill='#151515')
                else:
                    self.nxt_canvas.itemconfigure(xem, fill='#2c2c2b')

                if xem_x and xem_x not in ['tagsmc','tagsmr','tagsm+','tagsm-','tagsmx','tagsm','tags=','tagsxlider',
                                           'tagshixtory','tagsovr_button']:
                    self.t_tags=xem_x.replace('s','')


        elif event == 'canvas':
            for i in self.tag_list:
                if i == 'mc':
                    self.nxt_canvas.itemconfigure(f"tag{i}", fill='#151515')
                elif i == 'mr':
                    self.nxt_canvas.itemconfigure(f"tag{i}", fill='#151515')
                elif i == 'm+':
                    self.nxt_canvas.itemconfigure(f"tag{i}", fill='#151515')
                elif i == 'm-':
                    self.nxt_canvas.itemconfigure(f"tag{i}", fill='#151515')
                elif i == 'mx':
                    self.nxt_canvas.itemconfigure(f"tag{i}", fill='#151515')
                elif i == 'm':
                    self.nxt_canvas.itemconfigure(f"tag{i}", fill='#151515')
                elif i == '=':
                    self.nxt_canvas.itemconfigure(f"tag{i}", fill='#58f7fd')
                else:
                    self.nxt_canvas.itemconfigure(f"tag{i}",fill='#2c2c2b')

            for i in self.tag_list1:
                self.nxt_canvas.itemconfigure(f"tag{i}", fill='#151515')



    def on_canvas_click_x(self,event):
        clicked_items = event.widget.find_withtag(tk.CURRENT)
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)
            # This code changes the bg  of list widgets when  the mouse enters widgets not listed
            if tags[0] not in ['tagmc','tagmr','tagm+','tagm-','tagmx','tagm','tag=',
                               ]:
                self.nxt_canvas.itemconfigure('tagmc', fill='#151515')
                self.nxt_canvas.itemconfigure('tagmr', fill='#151515')
                self.nxt_canvas.itemconfigure('tagm+', fill='#151515')
                self.nxt_canvas.itemconfigure('tagm-', fill='#151515')
                self.nxt_canvas.itemconfigure('tagmx', fill='#151515')
                self.nxt_canvas.itemconfigure('tagm', fill='#151515')
                self.nxt_canvas.itemconfigure('tag=', fill='#58f7fd')
                self.f_canvas.itemconfigure('tagxlider', fill='#151515')
                self.f_canvas.itemconfigure('tagovr_button', fill='#151515')
                self.f_canvas.itemconfigure('taghixtory', fill='#151515')


                # This code changes the bg of the previous button the mouse entered in self.nxt_canvas
                if self.t_tags and self.t_tags != tags[0]:
                    self.nxt_canvas.itemconfigure(self.t_tags, fill='#2c2c2b')
    def temp_display(self,text,args):
        global  xi2,yi2, f_adjust

        minus = len(text) * 9
        if args and len(args) < 30:
            self.f_canvas.delete('tags' + self.tag_list1[5])
            self.create_rounded_button(self.f_canvas, (xi2) - (len(args) * 5), 65, xi2, yi2 // 3, 5,
                                       'black', 'black', self.tag_list1[5], "lightgrey", args + '#', 'canvas0')

        if text and len(text) < 18:
            self.f_canvas.delete("tagsdisplay")
            self.create_rounded_button(self.f_canvas, (xi2-3) - minus, yi2 / 2, xi2 - 10, yi2 - 3, 5, 'white','yellow',
                                   self.tag_list1[6], "lightgrey", text, 'canvas0')

        elif text and len(text) >=18 and len(text) < 23:

            # this allows alteration of the text font size
            self.switch=True
            minus =len(text) *7
            self.f_canvas.delete("tagsdisplay")
            self.create_rounded_button(self.f_canvas, (xi2-3) - minus, yi2 / 2, xi2 - 10, yi2 - 3, 5, 'white',
                                       'yellow',self.tag_list1[6], "lightgrey", text, 'canvas0')
            if len(text) >= 18:
                f_adjust=1


    def  backspace(self):
        global text, xi2,yi2

        if  len(text) == 1:
            text = '0'
            self.display_v='0'


        else:
            text= text[0:len(text)-1]
            self.display_v = self.display_v[:len(self.display_v)-1]

        minus = len(text) * 9
        self.f_canvas.delete("tagsdisplay")
        self.create_rounded_button(self.f_canvas, (xi2 - 3) - minus, yi2 / 2, xi2 - 10, yi2 - 3, 5, 'white', 'yellow',
                               self.tag_list1[6], "lightgrey", text, 'canvas0')

    def on_key_event(self,event,active=None):
        if event.event_type == keyboard.KEY_DOWN:
            if self.master.focus_get() and event.name in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.'] :
                self.nxt_canvas.itemconfigure('tag'+event.name, fill='#202020')
            elif self.master.focus_get() and event.name in ['/','+','-','=','*']:
                self.nxt_canvas.itemconfigure('tag' + event.name, fill='#202020')
        elif event.event_type == keyboard.KEY_UP:
            if event.name in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.']:
                self.nxt_canvas.itemconfigure(f"tag{event.name}",fill='#2c2c2b')
            elif self.master.focus_get() and event.name in ['/', '+', '-', '=', '*']:
                self.nxt_canvas.itemconfigure('tag' + event.name, fill='#2c2c2b')


    # we will create widgets for the second window frame canvas
    def second_f_canvas(self):
        self.create_rounded_button(self.canvas1,10 , 25, 37,30, 5,
                                   'black', 'grey', self.tag_list1[6], "lightgrey", 'History', 'canvas1')
        self.create_rounded_button(self.canvas1, 60, 25, 90, 30, 5,
                                   'black', 'grey', self.tag_list1[7], "lightgrey", 'Memory', 'canvas1')

    # we create the rounded button and other self.f_canvas widgets with this function
    def create_buttons1(self,event):
        global text, xi2,yi2,text_x,start_ind

        xi1, yi1=2,7
        xi2 = event.width
        yi2 = event.height
        bg_1 = '#151515'
        af = '#4a4a49'
        radius = 5
        minus = (len(text))*9
        top_text = self.f_canvas.itemcget(self.number[1], 'text')
        bottom_text=self.f_canvas.itemcget(self.number[0], 'text')

        for i in self.tag_list1:
            self.f_canvas.delete(f"tag{i}")
            self.f_canvas.delete(f"tags{i}")

        self.create_rounded_button(self.f_canvas, xi1, yi1,40 ,50 , radius, bg_1, af, self.tag_list1[0],
                                   "lightgrey",self.photo[8], 'canvas0')
        self.create_rounded_button(self.f_canvas, xi1+70,yi1 , xi1+95, 50, 5,bg_1, bg_1, self.tag_list1[1],
                                   "lightgrey", 'Standard', 'canvas0')
        self.create_rounded_button(self.f_canvas, xi1 + 125, yi1, xi1 + 155, 50, 5, bg_1, af, self.tag_list1[2],
                                   "lightgrey", self.photo[6], 'canvas0')

        if not  self.main1.winfo_viewable():
            self.create_rounded_button(self.f_canvas, xi2-40, yi1, xi2-5, 50, 5, bg_1, af, self.tag_list1[3],
                                   "lightgrey", self.photo[4], 'canvas0')
        if not start_ind:
            self.create_rounded_button(self.f_canvas, (xi2) - (len(text_x) * 5), 65, xi2, yi2 // 3, 5,
                                   'black', 'black', self.tag_list1[5], "lightgrey", text_x + '#', 'canvas0')
        else:
            self.create_rounded_button(self.f_canvas, (xi2) - (len(top_text) * 5), 65, xi2, yi2 // 3, 5,
                                       'black', 'black', self.tag_list1[5], "lightgrey", top_text + '#', 'canvas0')

        self.create_rounded_button(self.f_canvas, xi1,yi2/2, xi2-3, yi2-3, 5,bg_1, af, self.tag_list1[4],
                                   "lightgrey", 'rectangle', 'canvas0')
        if not start_ind:
            self.create_rounded_button(self.f_canvas,(xi2-3)-minus, yi2 / 2, xi2, yi2 - 3, 5, 'white', af, self.tag_list1[6],
                                   "lightgrey",text, 'canvas0')
        else:
            self.create_rounded_button(self.f_canvas, (xi2 - 3) - (len(bottom_text))*9, yi2 / 2, xi2, yi2 - 3, 5, 'white', af,
                                       self.tag_list1[6],"lightgrey",bottom_text, 'canvas0')
        start_ind=True


    # we create the rounded button and other self.nxt_canvas widgets with this function
    def create_buttons(self,event):
        global num, x1, y1, x2, y2
        num = 0
        radius = 12
        radiux = 8
        bg = '#2c2c2b'
        bg_1='#151515'
        af = '#4a4a49'
        x2 = (event.width) // 4
        y2 = (event.height // 6) + 16
        xi2 = (event.width // 6)
        yi2 = (event.height // 13) +2
        y1 = yi2 + 2
        xi, yi = 0, 2
        self.c_width = self.nxt_canvas.winfo_width()
        self.c_height = self.nxt_canvas.winfo_height()




        for i in self.tag_list:
            self.nxt_canvas.delete(f"tag{i}")

            self.nxt_canvas.delete(f"tags{i}")
             

        self.create_rounded_button(self.nxt_canvas, xi, yi, xi2, yi2, radiux, bg_1, af,self.tag_list[0], "white", "MC", 'canvas')
        self.create_rounded_button(self.nxt_canvas, xi2 + 2, yi, xi2 * 2, yi2, radiux, bg_1, af,self.tag_list[1], "white", "MR", 'canvas')
        self.create_rounded_button(self.nxt_canvas, xi2 * 2 + 2, yi, xi2 * 3, yi2, radiux, bg_1, af,self.tag_list[2], "white", "M+", 'canvas')
        self.create_rounded_button(self.nxt_canvas, xi2 * 3 + 2, yi, xi2 * 4, yi2, radiux, bg_1, af,self.tag_list[3], "white", "M-", 'canvas')
        self.create_rounded_button(self.nxt_canvas, xi2 * 4 + 2, yi, xi2 * 5, yi2, radiux, bg_1, af,self.tag_list[4], "white", "MS", 'canvas')
        if not  self.main1.winfo_viewable():
            self.create_rounded_button(self.nxt_canvas, xi2 * 5 + 2, yi, xi2 * 6+2, yi2, radiux, bg_1, af,
                                   self.tag_list[5], "white",self.photo1, 'canvas')

        self.create_rounded_button(self.nxt_canvas, x1, y1, x2, y2, radius, bg, af,self.tag_list[6],
                               "lightgrey", "%",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 + 3, y1, x2 * 2, y2, radius, bg, af,self.tag_list[7],
                                   "lightgrey", "CE",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 2 + 3, y1, x2 * 3, y2, radius, bg, af,self.tag_list[8],
                                   "lightgrey", "C",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 3 + 3, y1, x2 * 4, y2, radius, bg, af,self.tag_list[9],
                                   "white", self.photo[2],'canvas')

        self.create_rounded_button(self.nxt_canvas, x1, y2 + 2, x2, y2 * 2 - 23, radius, bg, af,self.tag_list[10],
                              "white", self.photo[0],'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 + 3, y2 + 3, x2 * 2, y2 * 2 - 23, radius, bg, af,self.tag_list[11],
                               "white",self.photo[1],'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 2 + 3, y2 + 3, x2 * 3, y2 * 2 - 23, radius, bg, af,self.tag_list[12],
                               "white",self.photo[7],'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 3 + 3, y2 + 3, x2 * 4, y2 * 2 - 23, radius, bg, af,self.tag_list[13],
                               "lightgrey",self.photo[3],'canvas')

        self.create_rounded_button(self.nxt_canvas, x1, y2 * 2 - 21, x2, y2 * 3 - 44, radius, bg, af,self.tag_list[14],
                               "lightgrey", "7",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 + 3, y2 * 2 - 21, x2 * 2, y2 * 3 - 44, radius, bg, af,self.tag_list[15],
                              "lightgrey","8",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 2 + 3, y2 * 2 - 21, x2 * 3, y2 * 3 - 44, radius, bg, af,self.tag_list[16],
                              "lightgrey","9",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 3 + 3, y2 * 2 - 21, x2 * 4, y2 * 3 - 44, radius, bg, af, self.tag_list[17],
                               "lightgrey", "x",'canvas')

        self.create_rounded_button(self.nxt_canvas, x1, y2 * 3 - 42, x2, y2 * 4 - 62, radius, bg, af,self.tag_list[18],
                               "lightgrey", "4",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 + 3, y2 * 3 - 42, x2 * 2, y2 * 4 - 62, radius, bg, af,self.tag_list[19],
                               "lightgrey", "5",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 2 + 3, y2 * 3 - 42, x2 * 3, y2 * 4 - 62, radius, bg, af,self.tag_list[20],
                               "lightgrey", "6",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 3 + 3, y2 * 3 - 42, x2 * 4, y2 * 4 - 62, radius, bg, af, self.tag_list[21],
                               "lightgrey", "-",'canvas')

        self.create_rounded_button(self.nxt_canvas, x1, y2 * 4 - 60, x2, y2 * 5 - 80, radius, bg, af,self.tag_list[22],
                               "lightgrey", "1",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 + 3, y2 * 4 - 60, x2 * 2, y2 * 5 - 80, radius, bg, af,self.tag_list[23],
                               "lightgrey", "2",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 2 + 3, y2 * 4 - 60, x2 * 3, y2 * 5 - 80, radius, bg, af,self.tag_list[24],
                               "lightgrey", "3",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 3 + 3, y2 * 4 - 60, x2 * 4, y2 * 5 - 80, radius, bg, af,self.tag_list[25],
                               "lightgrey", "+",'canvas')

        self.create_rounded_button(self.nxt_canvas, x1, y2 * 5 - 78, x2, y2 * 6 - 99, radius, bg, af,self.tag_list[26],
                              "lightgrey", "+/-",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 + 3, y2 * 5 - 78, x2 * 2, y2 * 6 - 99, radius, bg, af,self.tag_list[27],
                               "lightgrey", "0",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 2 + 3, y2 * 5 - 78, x2 * 3, y2 * 6 - 99, radius, bg, af,self.tag_list[28],
                               "lightgrey", ".",'canvas')
        self.create_rounded_button(self.nxt_canvas, x2 * 3 + 3, y2 * 5 - 78, x2 * 4, y2 * 6 - 99, radius,
                              '#58f7fd', '#57dbe0', self.tag_list[29], "white", "=",'canvas')


    def create_rounded_button(self,canvas, x1, y1, x2, y2, radius, background_color, active_fill, tag, text_color, text,
                              type):
        global num, radiux,f_adjust


        canvas.create_rounded_rectangle =canvas.create_polygon
        points = [x1 + radius, y1,x1 + radius, y1,x1 + radius, y1,x2 - radius, y1,x2 - radius, y1,x2, y1,x2, y1 + radius,
                  x2, y1 + radius,x2, y1 + radius,x2, y2 - radius,x2, y2 - radius,x2, y2,x2 - radius, y2,x2 - radius, y2,
                  x2 - radius, y2,x1 + radius, y2,x1 + radius, y2,x1, y2,x1, y2 - radius,x1, y2 - radius,x1, y2 - radius,x1,
                  y1 + radius,x1, y1 + radius,x1, y1]

        if type == 'canvas':
            button = canvas.create_rounded_rectangle(points, fill=background_color, outline="", smooth=True,
                                                 tags=f"tag{tag}", activefill=active_fill, )
            if isinstance(text,str):
                if tag in ['mc','mr','m+','m-','mx','m']:
                    text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color, tags=f"tags{tag}",
                                  font=('Bookman-Old-Style 9 normal'))
                else:
                    text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color,
                                              tags=f"tags{tag}",font=('Bookman-Old-Style 11 normal'))

                canvas.tag_bind(text, "<Button-1>", self.on_canvas_click)
                canvas.tag_bind(text, "<ButtonRelease-1>", self.on_canvas_unclick)
                canvas.tag_bind(text, "<Enter>", self.on_canvas_unclick)
                canvas.tag_bind(text, "<Leave>", self.on_canvas_leave)
            else:
                image=canvas.create_image((x1 + x2) / 2, (y1 + y2) / 2,image=text,anchor=CENTER,tags=f"tags{tag}")
                canvas.tag_bind(image, "<Button-1>", self.on_canvas_click)
                canvas.tag_bind(image, "<ButtonRelease-1>", self.on_canvas_unclick)
                canvas.tag_bind(image, "<Enter>", self.on_canvas_unclick)
                canvas.tag_bind(image, "<Leave>", self.on_canvas_leave)

            canvas.tag_bind(button, "<Button-1>", self.on_canvas_click)
            canvas.tag_bind(button, "<ButtonRelease-1>", self.on_canvas_unclick)
            canvas.tag_bind(button, "<Leave>", self.on_canvas_leave)
            canvas.tag_bind(button, "<Enter>", self.on_canvas_click_x)

        elif type == 'canvas0':
            if text == 'Standard':
                pass
            elif text == 'rec1':
                pass
            elif isinstance(text,str) and text  not in self.tag_list1:
                pass
            elif text == 'rectangle':
                button = canvas.create_rectangle(x1, y1, x2, y2, fill=background_color, outline="white",
                                                         tags=f"tag{tag}",)

            else:
                button = canvas.create_rounded_rectangle(points, fill=background_color, outline="", smooth=True,
                                                     tags=f"tag{tag}", activefill=active_fill, )
                print(button)
                canvas.tag_bind(button, "<Button-1>", self.on_canvas_click)
                canvas.tag_bind(button, "<ButtonRelease-1>", self.on_canvas_unclick)
                canvas.tag_bind(button, "<Leave>", self.on_canvas_leave)
                canvas.tag_bind(button, "<Enter>", self.on_canvas_click_x)

            if isinstance(text, str):
                if text == "Standard":
                    text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color, tags=f"tags{tag}",
                                          font=('Bookman-Old-Style 15 normal'))
                elif text == "rectangle":
                     pass

                #this code allows us to create text at the higher layer above rectangle
                elif text.endswith('#'):
                    text=text.replace('#','')
                    text = canvas.create_text(x1, (y1 + y2) / 2, text=text, fill=text_color,
                                              tags=f"tags{tag}",font=('Bookman-Old-Style 12 normal'))
                    self.number[1] = text
                elif text not in self.tag_list1:
                    if self.switch:
                        f_adjust+=1
                        text = canvas.create_text(x1, (y1 + y2) / 2, text=text, fill=text_color,
                                                  tags=f"tags{tag}", font=(f"Bookman-Old-Style {21-f_adjust} bold"))
                        self.number[0] = text
                        self.switch = False
                    elif not self.switch:
                        text = canvas.create_text(x1, (y1 + y2)/2, text=text, fill=text_color,
                                              tags=f"tags{tag}", font=('Bookman-Old-Style 25 bold'))
                        self.number[0] = text
                        f_adjust=1
                else:
                    text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color,
                                              tags=f"tags{tag}",font=('Bookman-Old-Style 9 normal'))
                    canvas.tag_bind(text, "<Button-1>", self.on_canvas_click)
                    canvas.tag_bind(text, "<ButtonRelease-1>", self.on_canvas_unclick)
                    canvas.tag_bind(text, "<Enter>", self.on_canvas_unclick)
                    canvas.tag_bind(text, "<Leave>", self.on_canvas_leave)
            else:
                image = canvas.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=text, anchor=CENTER, tags=f"tags{tag}")
                canvas.tag_bind(image, "<Button-1>", self.on_canvas_click)
                canvas.tag_bind(image, "<ButtonRelease-1>", self.on_canvas_unclick)
                canvas.tag_bind(image, "<Enter>", self.on_canvas_unclick)
                canvas.tag_bind(image, "<Leave>", self.on_canvas_leave)

        elif type == 'canvas1':
            if isinstance(text, str):
                    text = canvas.create_text((x1 + x2),(y1 + y2), text=text, fill=text_color,
                                                  tags=f"tags{tag}",font=('Bookman-Old-Style 15 normal'))

            else:
                pass
    def display(self, value, flag):
        global expression,text, vii,ctn


        if flag:

            if not self.eqclear:
                self.clear()
                self.eqclear = True

            if text == '0':
                self.clear()
                if '.' not in text:
                    if len(text) == 1 and text == '0':
                        text = ''
                    if value == '.':
                        text+='0'+ value
                        self.temp_display(text,'')
                    else:
                        text +=value
                        self.temp_display(text,'')



                elif value != '.':
                    if min(text) != '0':
                        text+=value
                        self.temp_display(text,'')
                    elif min(text) == '0':
                        self.clear()
                        text += value
                        self.temp_display(text, '')
            elif text != '0':
                if '.' not in text:
                    if value == '.':
                        text+=value
                        self.temp_display(text, '')
                    else:
                        text += value
                        self.temp_display(text, '')

                elif value != '.':
                    if min(text) != '0':
                        text += value
                        self.temp_display(text, '')
                    elif min(text) == '0':
                        self.clear()
                        text += value
                        self.temp_display(text, '')
            self.memory = ''
            self.record += value
            self.permit = True
            if (self.f_canvas.itemcget(self.number[1], 'text')).endswith('='):
                vi = self.f_canvas.itemcget(self.number[1], 'text').replace('=','')
                v= [i for i in vi if not i.isnumeric()]
                vii = v[0]+vi.split(v[0])[1]





                self.f_canvas.delete('tagsrec1')
            if len(self.checker) > 1:
                if self.display_v == '0':
                    self.display_v=''
                self.display_v += value
                self.clear()
                text+= self.display_v
                self.temp_display(text, '')

        else:

            # halt the procedure for operators sign
            if self.permit:

                if len(self.checker) > 1:
                    expression = self.status
                    expression += self.record1
                    self.display_v = ''
                    self.conn = True




                if value != '=' and value != 'ce' and value != 'c' and value!= 'roox' and value != '*2' and value != '1/*':
                    self.record = value
                    self.memory = ''
                    self.checker += ''.join([i for i in value if not i.isnumeric()])
                    vii=''

                    # code to use non equal signs as equal sign
                    if len(self.checker) > 1:
                        self.record1 = value
                        expression +=text
                        self.process(expression, 'operator_sign')
                        expression = ''
                        self.memory = '='
                        self.last_in = []





                    elif len(self.checker) < 2 :
                        expression += text
                        expression += value
                        self.clear()



                    self.permit = False

            # this code saves the previous used operator sign
            elif not self.permit:
                if value != '=' and value != 'ce' and value != 'roox' and value!= '*2' and value != '1/*':
                    self.last_entry = value
                    self.counter += 1

            # code displays main screen/half screen values
            if value != '=' and value != 'ce' and value != 'c' and value != 'roox' and value!= '*2' and value != '1/*':
                zee = self.f_canvas.itemcget(self.number[0], 'text')
                self.temp_display('',zee+value)



            if value == 'c':
                self.reset('clear_all')


            elif value == 'ce':
                if (self.f_canvas.itemcget(self.number[1], 'text')).endswith('='):
                    vi = self.f_canvas.itemcget(self.number[1], 'text').replace('=', '')
                    v = [i for i in vi if not i.isnumeric()]
                    ctn = v[0] + vi.split(v[0])[1]
                    self.reset('clear_all')
                else:
                     self.reset('clear_half')




            if value == '=':
                self.memory += value

                if len(self.memory) > 1:
                    if self.record and self.record[len(self.record) - 1].isnumeric():
                        self.process(text + self.record, 'equal_sign')
                        print('top',self.record)

                    elif self.record and not self.record[len(self.record) - 1].isnumeric():
                        self.last_in.append(text)
                        self.process(text + self.record + self.last_in[0], 'equal_sign')
                        print('bottom')

                # initial equal sign command
                elif self.record and len(self.memory) <= 1:
                    zee =[i for i in self.f_canvas.itemcget(self.number[1], 'text') if not i.isnumeric()]
                    expression += text
                    if vii:
                        expression =''
                        self.memory=''
                        expression=text+vii
                        self.process(expression,'equal_sign')
                        expression=''
                    if not zee:
                       expression = ''
                       self.memory = ''

                    self.process(expression, 'equal_sign')
                    expression = ''
                    self.eqclear = False
                    self.checker = ''

    def reset(self,arg):
        global expression,text,vii,text_x

        if arg == 'clear_all':
            expression,self.status,self.record ,self.record1,self.memory,self.correct = '','','','','',True
            self.clear_it,self.auto_equal, self.count,self.checker = False,[],'',''
            self.display_v ,self.conn,self.permit,self.last_in,self.last_entry= '',False,True,[],''
            self.counter,text,vii,text_x = 0,'0','',''
            self.temp_display(text,'')
            self.f_canvas.delete('tags'+self.tag_list1[5])

        else:
            text,= '0'
            self.temp_display(text, '')

    def process(self, req, ident):
        global text,text_x
        res = req
        res = res.replace('x', '*')
        res = res.replace('x2', '**')

        # code to alter the operator signs
        if self.counter >= 1:
            xi = [i for i in res if not i.isnumeric()]
            if len(xi) == 2:
                res = res.replace(''.join(xi), self.last_entry)
                res = res.replace(xi[1], self.last_entry)


            elif len(xi) < 2:

                res = res.replace(''.join(xi), self.last_entry)
                res = res.replace('x', '*')
                self.record = self.last_entry + self.record[1:]

        self.display_v = ''
        self.counter = 0

        # check for values and display the result
        if res and res[len(res)-1].isnumeric() and res.count('*') < 3:
            display=res
            res = str(eval(str(res)))
            self.status = res

            if res.endswith('0'):
                self.clear()
                text=str(int(eval(res)))
                self.temp_display(text,'')
                if ident == 'equal_sign':
                    self.temp_display('', display + '=')
                    text_x= req + '='

                elif ident == 'operator_sign':
                    self.temp_display('', text + self.record1)
                    text_x=text + self.record1

            else:
                self.clear()
                text=res
                self.temp_display(text,'')
                if ident == 'equal_sign':
                    self.temp_display('',display+'=')
                    text_x = req + '='

                elif ident == 'operator_sign':
                    self.temp_display('',text+self.record1)
                    text_x = text + self.record1


    #fucntion clears the screen
    def clear(self):
        global  text
        text=''
        self.temp_display(text,'')

window_width = '320'
window_height = '480'

expression = ''
x1, y1 = 0, 2
x2, y2 = 0, 0
xi2,yi2=2,0
dec,text,text_x = 30,'0',''
f_adjust,vii,ctn=0,'',''
start_ind = False



if __name__ == "__main__":
    window = Tk()
    window.title("Calculator")
    window.geometry(f"{window_width}x{window_height}+850+100")
    app = Application(window)
    app.mainloop()
from Tkinter import Tk, Label, Button, Entry, LEFT, RIGHT
from ttk import *
import sys




class LinkStack:
    def __init__(self, master):
        self.master = master
        master.title("LinkStack")
        
        self.stack = self.read_stack()
        self.stack_size = len(self.stack)
        self.pointer = 0
        
        self.label = Label(master, text = 'Enter link: ')
        self.label.pack(side = LEFT)

        self.pop_button = Button(master, text = 'Pop', command=self.pop)
        self.pop_button.pack(side = RIGHT)

        self.push_button = Button(master, text = 'Push', command=self.push)
        self.push_button.pack(side = RIGHT)
        
        self.link_input = Entry(master, width = 72)
        self.link_input.pack(side = RIGHT)


    def read_stack(self):
        txt = open('stack.txt', 'a+').close()
        txt = open('stack.txt', 'rU')
        lines = txt.readlines()
        line_list = [line for line in lines if line.strip()]
        txt.close()
        return line_list


    def write_stack(self, stack):
        txt = open('stack.txt', 'w')
        for line in stack:
            txt.write('{}\r\n'.format(line))


    def pop(self):
        if len(self.stack):
            line = self.stack[self.pointer]
            self.link_input.delete(0, 'end')
            self.link_input.insert(0, line)
            self.pointer = (self.pointer - 1) % self.stack_size


    def push(self):
        line = self.link_input.get()
        if line: 
            self.link_input.delete(0, 'end')
            self.stack.insert(0, line)
            self.stack_size = len(self.stack)
            self.pointer = 0
            self.write_stack(self.stack)

root = Tk()
my_gui = LinkStack(root)
if 'win32' in sys.platform or 'win64' in sys.platform:
    root.iconbitmap('linkstack.ico')
root.mainloop()

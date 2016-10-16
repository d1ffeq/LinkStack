from Tkinter import Tk, Label, Button, Entry, LEFT, RIGHT, BOTTOM, X
from ttk import *
import sys




root = Tk()

class LinkStack:
    def __init__(self, master):
        self.master = master
        master.title("LinkStack")

        self.stack = self.read_stack()
        self.stack_size = len(self.stack)
        self.pointer = 0

        self.label = Label(master, text = 'Enter link: ')
        self.label.pack(side = LEFT)

        self.del_link = Button(master, text = 'Del', width = 4, command=self.delete)
        self.del_link.pack(side = RIGHT)

        self.paste_link = Button(master, text = 'Paste', width = 5, command=self.paste)
        self.paste_link.pack(side = RIGHT)

        self.copy_link = Button(master, text = 'Copy', width = 5, command=self.copy)
        self.copy_link.pack(side = RIGHT)

        self.pop_button = Button(master, text = 'Pop', width = 7, command=self.pop)
        self.pop_button.pack(side = RIGHT)

        self.push_button = Button(master, text = 'Push', width = 7, command=self.push)
        self.push_button.pack(side = RIGHT)

        self.link_input = Entry(master, width = 72)
        self.link_input.pack(side = RIGHT)


    def read_stack(self):
        f = open('stack.txt', 'a+').close()
        txt = open('stack.txt', 'rU').read()
        lines = txt.splitlines()
        line_list = [line for line in lines if line]
        return line_list


    def write_stack(self, stack):
        txt = open('stack.txt', 'wb')
        for line in stack:
            txt.write('{}\r\n'.format(line))


    def pop(self):
        if len(self.stack):
            line = self.stack[self.pointer].rstrip('\r\n')
            self.link_input.delete(0, 'end')
            self.link_input.insert(0, line)
            self.pointer = (self.pointer + 1) % self.stack_size


    def push(self):
        line = self.link_input.get()
        if line and not line in self.stack: 
            self.link_input.delete(0, 'end')
            self.stack.insert(0, line)
            self.stack_size = len(self.stack)
            self.pointer = 0
            self.write_stack(self.stack)


    def copy(self):
        line = self.link_input.get().rstrip('\r\n')
        if line:
            root.clipboard_clear()
            root.clipboard_append(line)


    def paste(self):
        line = root.clipboard_get()
        if line:
            self.link_input.delete(0, 'end')
            self.link_input.insert(0, line)


    def delete(self):
        line = self.link_input.get().rstrip('\r\n')
        if line and line in self.stack: 
            self.link_input.delete(0, 'end')
            self.stack.remove(line)
            self.stack_size = len(self.stack)
            self.pointer = 0
            self.write_stack(self.stack)

my_gui = LinkStack(root)
if 'win32' in sys.platform or 'win64' in sys.platform:
    root.iconbitmap('linkstack.ico')
root.mainloop()

"""
测试一个经典的GUI程序的写法，使用面向对象的方式
"""
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    """一个经典的GUI程序"""
    def __init__(self, master = None):
        super().__init__(master)  # super()代表父类的定义
        self.master = master
        self.pack()
        self.createWidget()
        
    def createWidget(self):
        """"创建组件"""
        self.label01 = Label(self,text="Label",width=10,height = 2, bg = 'black', fg = 'white')
        self.label01.pack()
        self.label02 = Label(self,text="God",width=10,height = 2, bg = 'blue', fg = 'white', font = ("黑体",30))
        self.label02.pack()
        
        # 显示图像
        global photo  # 把photo定义成全局变量，如果是局部变量，本方法执行完后，图像对象销毁，窗口不显示图像
        photo = PhotoImage(file="pic01.gif")
        self.label03 = Label(self, image = photo)
        self.label03.pack()
        
        self.label04 = Label(self, text="哦哦\n这东西好难\n慢慢学吧，加油", borderwidth=1, relief="solid", justify = "right")
        self.label04.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你99多玫瑰花")

if __name__ == "__main__":
    root = Tk()
    root.geometry("900x900+100+50")
    root.title("Label标签测试")
    app = Application(master=root)

    root.mainloop()

# 学完GUI编程40节视频，明天继续。 2024-05-28  18：23
# 学完41节，不想看了，好困。2024-05-29 15：26
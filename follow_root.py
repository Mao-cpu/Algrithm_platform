import DP
import time
import search
import Greedy
import tkinter
import backtrack
import tkinter as tk            # 导入GUI界面函数库
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from heredity import heredity
from PIL import Image, ImageTk  # 导入图像处理函数库
from sort import decrease, increase
from draw_picture import scatter, barh


# 1.算法
def in_main(a_name, choice):
    def go(*args):  # 处理事件，*args表示可变参数
        s = comboxlist.get()
        if choice == 1:
            c, n, w, v, stime, y1, maxvalue = DP.Dp(s)
        elif choice == 2:
            c, n, w, v, stime, y1, maxvalue = Greedy.Greedy(s)
        elif choice == 3:
            c, n, w, v, stime, y1, maxvalue = backtrack.Bt(s)
        elif choice == 4:
             c, n, w, v, stime, y1, maxvalue = heredity(s)

        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 执行算法的时间
        search.in_log(time1, a_name, s)
        # 显示文本框
        tab = Frame(master=tabBar)
        tabBar.add(tab, text=s)
        textContainer = Labelframe(tab)
        textContainer.pack(expand=YES, fill=BOTH)
        tabBar.pack(expand=YES, fill=BOTH)
        textArea = tkinter.Text(master=textContainer)
        textArea.pack(side=LEFT, expand=YES, fill=BOTH)

        textArea.insert(INSERT, '\n背包容量：' + str(c) + '\n物品个数：' + str(n))
        textArea.insert(INSERT, '\n最大价值：'+str(maxvalue))
        textArea.insert(INSERT, "\n耗时：" + stime + 's')
        textArea.insert(INSERT, '\n背包编号   重量       价值      解向量\n')
        for i in range(len(w)):
            textArea.insert(INSERT, str(i+1) + '          ' + str(w[i]) + '         ' + str(v[i]) + '           ' + str(y1[i]) + '\n')

    win = tkinter.Tk()  # 构造窗体
    win.geometry('500x400')
    win.title(a_name)
    comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
    comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
    comboxlist["values"] = search.sqlite_read()
    # comboxlist.current(0)  # 选择第一个
    comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist.pack()
    # 显示文本框
    tabBar = Notebook(master=win)
    tab = Frame(master=tabBar)
    textContainer = Labelframe(tab)
    textContainer.pack(expand=YES, fill=BOTH)
    tabBar.pack(expand=YES, fill=BOTH)
    textArea = tkinter.Text(master=textContainer)
    textArea.pack(side=LEFT, expand=YES, fill=BOTH)
    win.mainloop()  # 进入消息循环


# 2.绘图
def in_main2(a_name, choice):
    win = tk.Toplevel()
    win.geometry('850x623')
    win.title(a_name)

    def show():
        if choice == 5:
            scatter(s)
        elif choice == 6:
            barh(s)
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 执行算法的时间
        search.in_log(time1, a_name, s)
        global img_png  # 定义全局变量 图像的

        def Show_Img():
            global img_png
            if choice == 5:
                Img = Image.open('./src/picture/scatter_' + s + '.png')
            else:
                Img = Image.open('./src/picture/barch_' + s + '.png')
            img_png = ImageTk.PhotoImage(Img)
            label_Img = tk.Label(win, image=img_png)
            label_Img.pack(ipady=45)

        # 创建显示图像按钮
        btn_Show = tk.Button(win,
                             text='显示图像',  # 显示在按钮上的文字
                             width=15, height=2,
                             command=Show_Img)  # 点击按钮式执行的命令
        btn_Show.pack()  # 按钮位置

    menuBar = Menu(win)
    selectfMenu = Menu(menuBar, tearoff=0)
    list = search.sqlite_read()
    for i in range(len(list)):
        fileMune = Menu(selectfMenu)
    menuBar.add_cascade(label="选择数据", menu=selectfMenu)
    for i in range(len(list)):
        s = list[i]
        selectfMenu.add_command(label=s, command=show, background='pink')
    win.configure(menu=menuBar)
    # 显示窗口
    win.mainloop()


# 3.排序
def in_main3(a_name, choice):

    def go(*args):  # 处理事件，*args表示可变参数
        s = comboxlist.get()
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        search.in_log(time1, a_name, s)
        if choice == 7:
            c, n, w, v, x, y = increase(s)
        elif choice == 8:
            c, n, w, v, x, y = decrease(s)

        # 显示文本框
        tab = Frame(master=tabBar)
        tabBar.add(tab, text=s)
        textContainer = Labelframe(tab)
        textContainer.pack(expand=YES, fill=BOTH)
        tabBar.pack(expand=YES, fill=BOTH)
        textArea = tkinter.Text(master=textContainer)
        textArea.pack(side=LEFT, expand=YES, fill=BOTH)

        textArea.insert(INSERT, '\n背包容量：' + str(c) + '\n物品个数：' + str(n))
        textArea.insert(INSERT, '\n按单位重量价值排序后得：\n')
        textArea.insert(INSERT, '\n背包编号    重量       价值         单位价值\n')
        for i in range(len(w)):
            textArea.insert(INSERT, str(y[i]) + '           '+str(w[i]) + '         ' + str(v[i]) + '           ' + str(x[i]) + '\n')

    win = tkinter.Tk()  # 构造窗体
    win.geometry('500x400')
    win.title(a_name)
    comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
    comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
    comboxlist["values"] = search.sqlite_read()
    comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist.pack()
    # 显示文本框
    tabBar = Notebook(master=win)
    tab = Frame(master=tabBar)
    # tabBar.add(tab, text=s)
    textContainer = Labelframe(tab)
    textContainer.pack(expand=YES, fill=BOTH)
    tabBar.pack(expand=YES, fill=BOTH)
    textArea = tkinter.Text(master=textContainer)
    textArea.pack(side=LEFT, expand=YES, fill=BOTH)
    win.mainloop()  # 进入消息循环


# 4. 显示日志记录
def in_main4(a_name):
    # 构造窗体
    win = tkinter.Tk()
    win.geometry('920x250')
    win.title(a_name)
    list = search.log()
    tree = ttk.Treeview(win)  # #创建表格对象
    tree["columns"] = ("重量", "价值", "解向量")  # #定义列
    tree.column("重量", width=220)  # #设置列
    tree.column("价值", width=220)
    tree.column("解向量", width=220)
    for num in range(len(list)):
        i = len(list) - num - 1
        tree.insert("", num, text=str(num), values=(str(list[i][0]), str(list[i][1]), str(list[i][2])))  # 给第0行添加数据，索引值可重复
    tree.pack()
    win.mainloop()
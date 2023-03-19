import re
import tkinter
import tkinter.messagebox

#创建Tk的实例，也就是要显示的窗口
root = tkinter.Tk()

#可以获取屏幕宽度与高
# ws = root.winfo_screenwidth()
# wh = root.winfo_screenheight()
# print("宽：{}高：{}" .format(ws,wh))
# print("宽：%d高：%d" % (ws,wh))

#设置窗口的大小和位置,在左上角（400，100）的位置;宽*高+x+y
root.geometry("300x270+400+100")
#(width = False, height = False)不改变窗口的大小
root.resizable(False,False)
#设置窗口的标题
root.title("简易计算器")

#放置用来显示信息的文本框，并设置为只读
#输入框与一个变量绑定
#entry,输入控件；用于显示简单的文本内容;
#textvariable文本框的值，是一个StringVar()对象
contentVar = tkinter.StringVar(root,'')
contentEntry = tkinter.Entry(root,textvariable = contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=10,y=10,width=280,height=20)

#按钮通用代码，参数btn表示按的是哪个按钮
def buttonClick(btn):
    content = contentVar.get()
    #如果已有内容是以小数点开头的，前面加0
    #startswith()方法用于检查字符串是否是以指定子字符串开头
    #根据不同按钮做出相应的处理
    if content.startswith('.'):
        content = '0' + content
    if btn in "0123456789":
        content += btn
    elif btn == '.':
        #如果最后一个运算数中已经有小数点，就提示错误
        lastPart = re.split(r'\+|-|\*|/',content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('错误','小数点多了')
            return
        else:
            content += btn
    elif btn == 'C':
        #清除整个表达式
        content = ''
    elif btn == '=':
        try:
            #对输入表达式求值
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('错误','表达式错误')
            return
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror('错误','不允许存在连续运算符')
            return
        content += btn
    elif btn =='Sqrt':
        n = content.split('.')
        #map() 会根据提供的函数对指定序列做映射。
        #all() 函数用于判断给定的可迭代参数iterable中的所有元素是否都为TRUE
        if all(map(lambda x: x.isdigit(),n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return

    contentVar.set(content)


# 放置清除按钮和等号按钮
btnClear = tkinter.Button(root,
                          text='Clear',
                          command=lambda: buttonClick('C'))
btnClear.place(x=40, y=40, width=80, height=20)
btnCompute = tkinter.Button(root,
                            text='=',
                            command=lambda: buttonClick('='))
btnCompute.place(x=170, y=40, width=80, height=20)

# 放置10个数字、小数点和计算平方根的按钮
digits = list('0123456789.') + ['Sqrt']
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigit = tkinter.Button(root,
                                  text=d,
                                  command=lambda x=d: buttonClick(x))
        btnDigit.place(x=20 + col * 70,
                       y=80 + row * 50,
                       width=50,
                       height=20)

# 放置运算符按钮
operators = ('+', '-', '*', '/', '**', '//')
for index, operator in enumerate(operators):
    btnOperator = tkinter.Button(root,
                                 text=operator,
                                 command=lambda x=operator: buttonClick(x))
    btnOperator.place(x=230, y=80 + index * 30, width=50, height=20)

root.mainloop()

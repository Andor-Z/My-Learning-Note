#简单图形编程

from graphics import *
#创建窗体 默认 高200像素 宽200像素
win = GraphWin('Celsius Converter', 400, 300)
win.setCoords(0.0, 0.0, 3.0, 4.0)
#绘制接口
Text(Point(1, 3), 'Celsiu Temperature:').draw(win)
Text(Point(1, 1), 'Fahrenheit Temperature:').draw(win)
input = Entry(Point(2, 3), 5)
input.setText('0.0')
input.draw(win)

output = Text(Point(2, 1),'')
output.draw(win)

button= Text(Point(1.5, 2.0), 'Coverter It')
button.draw(win)
Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
#等待鼠标点击
win.getMouse()
celsius = eval(input.getText())
fahrenheit = 9.0/5.0 *celsius +32.0
# 显示输出，改变按钮
output.setText(fahrenheit)
button.setText('Quit')

win.getMouse()
win.close()
import matplotlib.pyplot as plt 
import numpy as np 


def ex1():
	plt.plot(range(1,7),'ro')
	plt.ylabel('Description of y value')
	plt.show()


def ex2():
	X = np.linspace(-np.pi,np.pi,256,endpoint= True)
	#使用numpy库的linspace函数生成一个numpy数组X，包含了从-pi到+pi等间隔的256个值
	C, S = np.cos(X*X), np.sin(X)
	plt.plot(X, C, 'ro', label = '$sin(X)$')
	plt.plot(X, S, label = '$cos(X^2)$')
	plt.xlabel('xlabel')
	plt.ylabel('ylabel')
	plt.legend() #描述表示每条曲线的标签
	plt.title('The Title')
	plt.show()

def ex3():
	X = np.linspace(-np.pi,np.pi,256,endpoint= True)
	#使用numpy库的linspace函数生成一个numpy数组X，包含了从-pi到+pi等间隔的256个值
	C, S = np.cos(X*X), np.sin(X)
	plt.plot(X, C,  label = '$sin(X)$')
	plt.plot(X, S, label = '$cos(X^2)$')
	plt.xlabel('x轴')
	plt.ylabel('y轴')
	plt.legend() #描述表示每条曲线的标签
	plt.title('The Title')
	plt.show()

#pyplot 子库创建多个子图  subplot(nrows, mcols, plotnum)

def ex4():
	plt.subplot(222)  #分成4个图 取2号
	plt.subplot(121)  #整个图分成2列 取第一列
	plt.subplot(224)
	plt.show()

def f(t):
	return np.exp(-t) * np.cos(2 *np.pi *t)

def ex5():
	t1 = np.arange(0.0, 5.0, 0.1)
	t2 = np.arange(0.0, 5.0, 0.02)

	plt.subplot(211)
	plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
	plt.subplot(212)
	plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
	plt.show()

def ex5_1():
	t1 = np.arange(0.0, 5.0, 0.1)
	t2 = np.arange(0.0, 5.0, 0.02)

	plt.subplot(211)
	plt.plot(t1, f(t1), 'bo', t2, np.cos(2 * np.pi * t2), 'k')
	plt.subplot(212)
	plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
	plt.show()


#直方图、柱状图  hist()

def ex6():
	mu, sigma = 100, 15
	x = mu +sigma *np.random.randn(10000)
	plt.hist(x, 50, normed = 1, facecolor = 'g')  
	#第二参数50表示直方图中直条即bin个数
	#normed 参数是一个布尔值，为真时，将直方图归一化，纵轴一概率的形式表示。
	plt.xlabel('Smarts')
	plt.ylabel('Histogram of IQ')
	plt.text(60, 0.025, r'$\mu = 100, \sigma = 15$')
	#text 指定位置添加文本
	plt.axis([40, 160, 0, 0.03])
	plt.show()

#image子库 对图像进行操作
import matplotlib.image as mpimg

def ex7():
	p = input('请输入图片路径：')
	img = mpimg.read(p)
	plt.imshow(img)
	plt.show()




#ex1()
ex6()
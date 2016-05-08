import numpy as np
import operator
import os


def creat_dataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A','A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # training example called dataSet
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # X是a*b的矩阵，np.tile（X, (m, n))  是将X复制为a*m行，b*n列的矩阵
    # 维数不一致怎么减
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis = 1)
    # array.sum(axis=1)按行累加，axis=0为按列累加
    distance = sqDistance ** 0.5
    sortedDistIndicies = distance.argsort()
    # argsort()是numpy中的方法，得到矩阵中每个元素的排序序号
    # A=array.argsort()  A[0]表示排序后 排在第一个的那个数在原来数组中的下标
    classCount = {} 
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]


def file_to_matrix(filename):
    '''
    输入文本文件，输出training example matrix 和 label 向量
    将文本转换为NumPy
    '''
    fr = open(filename)
    arrayOLines = fr.readlines()
    linesNumb = len(arrayOLines)
    traMat = np.zeros((linesNumb, 3))
    classLabelVector = []
    index = 0 
    for line in arrayOLines:
        line = line.strip()
        # 移除字符串头尾指定的字符（默认为空格）,这里主要去掉回车符
        listFromLine = line.split('\t')
        traMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return traMat, classLabelVector


'''
mat, label = file_to_matrix(r'D:\GitHub\Python-note\machinelearninginaction\Ch02\datingTestSet2.txt')
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
# matplotlib中的图像都位于Figure对象中
ax = fig.add_subplot(111)
# ax.scatter(mat[:,1], mat[:, 2])
ax.scatter(mat[:,1], mat[:, 2], 15.0*np.array(label), 15.0*np.array(label))
# 后面的两个arrary表示颜色的方式目前不太明白
plt.show()
'''

# Prepare data : normalizing numeric values归一化数值
# newValue = (Value - min)/(max - min)

def auto_norm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    # array.min(0)  返回一个数组，数组中每个数都是它所在列的所有数的最小值
    # array.min(1)  返回一个数组，数组中每个数都是它所在行的所有数的最小值
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))  # 这句有意义吗?
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet/np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def dating_class_test():
    hoRatio = 0.10
    datingDataMat, datingDataLabels = file_to_matrix(r'D:\GitHub\Python-note\machinelearninginaction\Ch02\datingTestSet2.txt')
    normMat, ranges, minVals = auto_norm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingDataLabels[numTestVecs:m], 3)
        print('the classifier came back with: %d, the real answer is : %d.' %(classifierResult, datingDataLabels[i]))
        if classifierResult != datingDataLabels[i]:
            errorCount += 1.0
    print('the total error rate is: %f.' % (errorCount/float(numTestVecs)))

# dating_class_test()
# the total error rate is: 0.050000.




# handwriting recognition system
def img_to_vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i + j] = int(lineStr[j])
    return returnVect


def handwriting_class_test():
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')
    # strlist=listdir('str')  读取目录str下的所有文件名，返回一个字符串列表
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        # fileStr = fileNameStr.split('.')[0]     #take off .txt
        # classNumStr = int(fileStr.split('_')[0])
        # 若只是0-9个位数，其实可以直接取fileNameStr的第一个字符
        classNumStr = int(fileNameStr[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img_to_vector(os.path.join('trainingDigits', fileNameStr))
    testFileList = os.listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        classNumStr = int(fileNameStr[0])
        vectorUnderTTest = img_to_vector(os.path.join('testDigits', fileNameStr))
        classfierResult = classify0(vectorUnderTTest, trainingMat, hwLabels, 3)
        print('the classifier came back with: %d, the real answer is: %d.' %(classfierResult, classNumStr))
        if classfierResult != classNumStr :
            errorCount += 1.0
    print('\nthe total number of error is: %d' %errorCount)
    print('\nthe total error rate is: %f' % (errorCount/float(mTest)))


# %run -i c2-1-k-NN.py
# %time handwriting_class_test()

# the total number of error is: 11

# the total error rate is: 0.011628
# Wall time: 53.1 s


# k-近邻算法的缺陷
# 1.必须保存全部数据集，如果训练数据集的很大，必须使用大量的存储空间。必须对数据集中的每个数据计算距离值，实际使用时可能非常耗时。
# 2.它无法给出任何数据的基础结构信息，因此我们也无法知晓平均实例样本和典型实例样本具有什么特征。
# k决策树就是k-近邻算法的优化版，可以节省大量的计算开销。
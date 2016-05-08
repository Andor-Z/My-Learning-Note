# ID3算法
import operator
from math import log

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

def calc_Shannon_Entropy(dataSet):
    '''
    计算给定数据集的熵
    '''
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        labelCounts[currentLabel] = labelCounts.get(currentLabel, 0) + 1
        # 为何不用前一章中的这句？
        # if currentLabel not in labelCounts.keys():
        #     labelCounts[currentLabel] = 0
        # labelCounts[currentLabel] += 1
    Entropy = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        Entropy -= prob * log(prob, 2)
    return Entropy

# myDat,labels=createDataSet()
# calc_Shannon_Entropy(myDat)

# 熵越高，则混合的数据也越多，

def splitDataSet(dataSet, axis, value):
    '''
    dataSet: 待划分的数据集：n列，前n-1列是特征向量， 第n列是标签
    axis: 划分数据集的特征: 也就是指定数据集里的特征向量，axis 可取 0到(n-2)，完整的算法应该要把这些都取遍
    value: 需要返回的特征的值：也就是每一列中出现的
    表示在dataSet中，找出第(axis+1)列中特征值是value的行，并返回去除第(axis+1)列的数据集
    '''
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[: axis]
            reducedFeatVec.extend(featVec[axis+1 :])
            # list.extend(L)将给定列表L中的所有元素附加到原列表a的末尾。相当于a[len(a):] = L
            retDataSet.append(reducedFeatVec)
            # list.append(x)添加一个元素到列表的末尾。相当于a[len(a):] = [x]。
    return retDataSet


# 遍历整个数据集，循环计算shannon Entropy 和splitDataSet()函数，找到最好的特征划分方式
# 调用的数据需要满足一定的要求：
# 1.数据必须是一种由列表元素组成的列表，而且所有的列表元素都要具有相同的数据长度
# 2.数据的最后一列或者每个实例的最后一个元素是当前实例的类别标签。
def chooseBestFeatureToSlipt(dataSet):
    numFeatures = len(dataSet[0]) -1
    baseEntropy = calc_Shannon_Entropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)          # 将dict装换成set，保证无重复元素
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            # 通过双循环for，将dataSet中的特征向量，和特征向量不重复值，循环个遍
            prob = len(subDataSet)/float(len(dataSet))
            # 第(i+1)列中值为value占总数据集的百分比
            newEntropy += prob * calc_Shannon_Entropy(subDataSet)
            # 计算每种规划方式的信息熵
        infoGain = baseEntropy - newEntropy
        # i 这种划分数据方法的信息增益
        # 信息增益是熵的减少或者是数据无序度的减少
        if infoGain > bestInfoGain :
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    # sortedClassCount是列表，而不是dict
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    # ！！！！！labels是数据集中所有特征的标签，并不是这个数据集的分类标签
    classList = [example[-1] for example in dataSet]
    # 其实是这个数据集的分类标签
    if classList.count(classList[0]) == len(classList):
        # 如果分类标签都是同一值的话，返回这个值
        return classList[0]
    if len(dataSet[0]) == 1:
        # 所有的特征向量已经使用完了，只剩下了标签向量了
        return majorityCnt(classList)
        # 挑选出现次数最多的类别作为返回值。
    bestFeat = chooseBestFeatureToSlipt(dataSet)
    # bestFeat 应该是数值吧，代表最佳特征值的那一列吧
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
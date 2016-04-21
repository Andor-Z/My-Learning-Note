# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}



import numpy as np
import pandas as pd
from pandas import Series, DataFrame
critics_df = DataFrame(critics)

# Returns a distance-based similarity score for p1 and p2
#返回一个欧几里得距离
def sim_distance( prefs, p1, p2 ):
    #
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    

    #如果两者没用共同之处，则返回0
    if len(si) == 0: return 0

    sum_of_squares = sum([pow(prefs[p1][item] - prefs[p2][item], 2)
                          for item in prefs[p1] if item in prefs[p2]])

    return 1/(1 + np.sqrt(sum_of_squares))

#sim_distance(critics, 'Lisa Rose', 'Gene Seymour')


# Returns the Pearson correlation coefficient for p1 and p2
#返回p1和p2的皮尔逊相关系数
def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)
    # 如两者没有共同之处，则返回0
    if n == 0:return 0
    #对所有偏好求和
    sump1 = sum([prefs[p1][it] for it in si])
    sump2 = sum([prefs[p2][it] for it in si])

    # 求平方和
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # 求乘积之和 Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # 计算皮尔逊评价值 Calculate r (Pesrson score)
    num = pSum - (sump1*sump2)/n
    den = np.sqrt((sum1Sq - pow(sump1, 2)/n)*(sum2Sq - pow(sump2, 2)/n))
    if den == 0 : return 0

    r = num/den
    return r

#sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')


def topMatches(prefs, person, n = 5, similarity = sim_pearson):
    '''
    Return the best mathces for person from the prefs dictionary.
    从反映偏好的字典中返回最为匹配者。
    Number of results and similarity function are optional params.
    返回结果的个数n和相似度函数similarity均为可选参数。
    '''
    scores = [(similarity(prefs, person, other),other) for other in prefs if other !=person]

    scores.sort()
    scores.reverse()
    return scores[0:n]


#topMatches(critics, 'Lisa Rose')


# 推荐物品 Recommending Items
def getRecommendations(prefs, person, similarity= sim_pearson):
    totals= {}
    simSums={}
    for other in prefs:
        # 不和自己做比较
        if other == person:
            continue
        sim = similarity(prefs, person, other) # person与其他人的相似度
        # 忽略评价值为0或者小于0的情况
        if sim <= 0:
            continue
        for item in prefs[other]:

            # 只对自己还未看过的影片进行评价
            if item not in prefs[person] or prefs[person][item] ==0:
                totals.setdefault(item,0)
                # 相似度 * 评价度
                totals[item] = totals[item] + sim * prefs[other][item]
                
                #相似度之和
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # 建立一个归一化的列表
    #print(totals) 
    rankings = [(total/simSums[item],item) for item, total in totals.items()]
    # 循环迭代字典的时候，键和对应的值通过使用items()方法可以同时得到。
    #rankings_df = DataFrame(rankings)

    rankings.sort()
    rankings.reverse()
    return rankings



#getRecommendations(critics, 'Toby')


def transformPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})

			# 将物品和人员对调
			result[item][person] = prefs[person][item]
	return result 


def calculateSimilarITems(prefs, n =10, similarity = sim_distance):
	'''
	建立字典，以给出与这些物品最为相近的所有其他物品
	'''
	result = {}
	itemPrefs = transformPrefs(prefs)
	c = 0
	for item in itemPrefs:
		# 
		c +=1 
		if c%100 ==0:
			print('%d / %d ')  % (c,len(itemPrefs))
		# 寻找相似的物品
		scores = topMatches(itemPrefs, item, n = n , similarity = similarity)
		result[item] = scores 
	result_df = DataFrame(result)
	return result_df


def getRecommendedItems(prefs, itemMatch,user):
	

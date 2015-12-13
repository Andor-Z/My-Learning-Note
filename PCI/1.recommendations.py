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

# Returns a distance-based similarity score for person1 and person2
#返回一个欧几里得距离
def sim_distance( prefs, person1, person2 ):
	#
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	

	#如果两者没用共同之处，则返回0
	if len(si) == 0: return 0

	sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
		                  for item in prefs[person1] if item in prefs[person2]])

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


def topMatches(prefs, person, n = 5, similarity)




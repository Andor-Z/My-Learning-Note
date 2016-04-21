from pydelicious import get_popular,get_userposts,get_urlposts

def initializeUserDict(tag, count=5):
    user_dict={}
    # 获取前count个最受欢迎的张
    for p1 in get_popular(tag = tag)[0:count]:
        for p2 in get_urlposts(p1['href']):
            user=p2['user']
            user_dict[user] = {}
    return user_dict



def fillItems(user_dict):
    all_items ={}
    # 查找所有用户都提交过的链接
    for user in user_dict:
        for i in range(3):
            try:
                posts = get_userposts(user)
                break 
            except:
                print('Failed user' + user +',retrying!')
        for post in posts:
            usl = post['href']
            user_dict[user][url] = 1.0
            all_items[url] = 1

    # 用0 填充缺失项
    for ratings in user_dict.values():
        for item in all_items:
            if item not in ratings:
                ratings[item] = 0.0


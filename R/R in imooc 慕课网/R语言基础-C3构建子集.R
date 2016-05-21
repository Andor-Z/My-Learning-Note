# 3-2 矩阵的子集
x <- matrix(1:6, nrow = 2, ncol = 3)
x
x[1, 2]
x[1,]
x[2, c(1,3)]
x[1, 2, drop = FALSE]

# 3-3 数据框的子集

x <- data.frame(v1=1:5, v2=6:10, v3=11:15)

#将第三列中的第2,4元素赋值为缺失值
x$v3[c(2, 4)] <- NA 

# 取出第二列
x[,2]
x[,"v2"]

# 找出v1列小于4，v2列大于等于8的行
x[(x$v1<4 & x$v2>=8),]

# subset()构造子集函数,参数：传入数据，条件
subset(x,x$v1>2)

# 3-4 Subsetting List
x <- list(id=1:4, height=170, gender='male')
# 取得列表中的元素
x[1]
x["id"]
# 取得列表中元素的内容
x[[1]]
x[["id"]]
x$id

x[c(1, 3)]

## subsetting nested elements of a list 从列表中获得嵌套元素
x <- list(a=list(1, 2, 3, 4), b=c("Monday","Tuesday"))

x[[1]]
x[[1]][[2]]
x[[1]][2]

x[[c(1, 2)]]

## partial matching 不完全匹配
l <- list(asdfghj = 1:10)
l$a

# 处理缺失值
x <- c(1, NA, 2, NA, 3)
is.na(x) #判断数据中是否存在缺失值
x[!is.na(x)] # ！ 表示取反

y <- c("c", "b", NA, "a", NA)
z <- complete.cases(x,y) 
# Return a logical vector indicating which cases are complete, i.e., have no missing values
x[z]
y[z]

library(datasets)
head(airquality)

g <- complete.cases(airquality)
airquality[g,][1:10,]

## Vectorized

x <- 1:5
y <- 6:10
x+y
x*y
x/y

x <- matrix(1:4, nrow = 2, ncol = 2)
y <- matrix(rep(2, 4), nrow = 2, ncol = 2)
x+y
x*y
x/y

x%*%y# 矩阵乘法

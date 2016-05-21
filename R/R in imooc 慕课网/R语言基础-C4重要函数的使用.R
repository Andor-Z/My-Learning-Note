# lapply

str(lapply)

x <- list(a=1:10, b=c(11, 21, 31, 41, 51))
lapply(x,mean)

x <- 1:4
lapply(x, runif) # runif()从一个均匀总体抽取若干的数
lapply(x, runif, min=0, max=100)


x <- list(a=matrix(1:6, 2, 3), b=matrix(4:7, 2, 2))
lapply(x, function(m) m[1,]) # 匿名函数


# sapply 某些时候讲lapply 化简

x <- list(a=1:10, b=c(11, 21, 31, 41, 51))
lapply(x,mean)
sapply(x,mean)

# apply

x <- matrix(1:16, 4, 4)
apply(x, 2, mean) # 对x的第二维度（列）求平均

# 可以用以下替代
rowSums(x)
rowMeans(x)
colSums(x)
colMeans(x)


x <- matrix(rnorm(100), 10, 10)
apply(x, 1, quantile, probs=c(0.25, 0.75))

x <- array(rnorm(2*3*4), c(2, 3, 4))
apply(x,c(1, 2), mean)
mean()

# mapply

list(rep(1, 4), rep(2,3), rep(3,2), rep(4,1))
mapply(rep, 1:4, 4:1)


s <- function(n, mean, std){
  rnorm(n, mean, std)
}
s(4, 0, 1)

rnorm(4, 0 , 1) # 和s函数一样？

mapply(s, 1:5, 5:1, 2)


# tapply

x <- c(rnorm(5), runif(5), rnorm(5, 1))
f <- gl(3, 5)  # 因子函数，3个水平，每个水平下5个元素

tapply(x, f, mean)

# split

split(x, f)
lapply(split(x, f), mean)



s <- split(airquality, airquality$Month)
table(airquality$Month)
lapply(s, function(x) colMeans(x[,c("Ozone", "Wind", "Temp")]))
sapply(s, function(x) colMeans(x[,c("Ozone", "Wind", "Temp")]))
sapply(s, function(x) colMeans(x[,c("Ozone", "Wind", "Temp")], na.rm = T))


# Sort and Order
x <- data.frame(v1=1:5, v2=c(10, 7, 9, 8, 6), v3=11:15, v4=c(1, 2, 2, 1, 1))
sort(x$v2) # 升序
sort(x$v2, decreasing = T)

order(x$v2)
x[order(x$v2),]


# Summarize data

head(airquality, 10)
tail(airquality)

summary(airquality)
str(airquality)
table(airquality$Ozone, useNA = "ifany")
table(airquality$Month, airquality$Day)


any(is.na())
sum(is.na())

all(airquality$Month<10)


Titanic
titanic <- as.data.frame(Titanic)
head(titanic)
dim(titanic) #维度
summary(titanic)

x<- xtabs(Freq~Class + Age, data=titanic)  # 频率交叉表

ftable(x)

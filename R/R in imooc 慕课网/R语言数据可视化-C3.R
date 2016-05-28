hist(airquality$Wind, xlab = "wind") # 柱状图
boxplot(airquality$Wind, xlab = "wind", ylab = "Speed(mph)") # 箱线图
boxplot(Wind~Month, airquality, xlab = "wind", ylab = "Speed(mph)") # 风速和月份


plot(airquality$Wind, airquality$Temp)

with(airquality, plot(Wind, Temp))
title(main="Wind and Temp in NYC")

with(airquality, plot(Wind, Temp, main="Wind and Temp in NYC")) # 标题


# 将其他信息画出，并不画出点
with(airquality, plot(Wind, Temp, main="Wind and Temp in NYC", type = "n")) 

# 用红色画出airquality中限制条件9月的子集的WindTemp数据
with(subset(airquality, Month==9), points(Wind, Temp, col="red"))

with(subset(airquality, Month %in% c(6, 7, 8)), points(Wind, Temp, col="black"))

# 拟合模型，加一条回归线
fit <- lm(Temp ~ Wind, airquality)  # 线性模型，第一参数中，左边因变量Y， 右边自变量X
abline(fit, lwd=3)  # lwd 线的宽度

# 图的说明
legend("topright", pch = 1, col = C("red","black"), legend = c("sep", "other"))
# 

# 全局参数par()
par("bg") #背景颜色
par("col") # 绘图色
par("mar") # (bottom, left, top, right) 绘图区域距离面板下左上右的距离
par("mfrow")  # 将当前绘图面板划分成n行m列 按照row行填充
par("mfcol")  #  按照列 填充


par(mfrow = c(1, 2))
with(airquality, {
  hist(Temp)
  hist(Wind)
})



y1 <- c(100, 200, 300, 400, 500)
y2 <- c(1, 2, 3, 4, 5)
x <- c(1, 2, 3, 4, 5)
df <- data.frame(x=rep(x,2), y=c(y1, y2), class=c(rep("y1", 5), rep("y2", 5)))

library(ggplot2)
ggplot(df, aes(x=x, y=y, color=class)) + geom_point()

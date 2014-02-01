library(graphics)
library('animation')
library('ggplot2')

data=data.frame(i=1:100,x=runif(100),y=runif(100))
saveGIF({for(i in 2:100){print(ggplot(data[1:i,],aes(x=x,y=y))+geom_point())}})

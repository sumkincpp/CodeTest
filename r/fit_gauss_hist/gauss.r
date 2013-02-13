data <- read.table("data.txt", sep=",",col.names=c("col"))

x <- data$col

xfit<-seq(min(x),max(x),length=40) 
yfit<-dnorm(xfit,mean=mean(x),sd=sd(x)) 

h <- hist(data$col, breaks=100)

yfit <- yfit*diff(h$mids[1:2])*length(x) 
lines(xfit, yfit, col="blue", lwd=2) 

#ks.test(data$col, "pnorm", mean(data$col), sd(data$col))
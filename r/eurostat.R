install.packages('XML')
library(XML)

mylines <- readLines(url("http://appsso.eurostat.ec.europa.eu/nui/show.do?query=BOOKMARK_DS-054198_QID_-55FD03C1_UID_-3F171EB0&layout=TIME,C,X,0;GEO,L,Y,0;AGE,L,Z,0;SEX,L,Z,1;INDICATORS,C,Z,2;&zSelection=DS-054198AGE,TOTAL;DS-054198INDICATORS,OBS_FLAG;DS-054198SEX,T;&rankName1=SEX_1_2_-1_2&rankName2=AGE_1_2_-1_2&rankName3=INDICATORS_1_2_-1_2&rankName4=TIME_1_0_0_0&rankName5=GEO_1_2_0_1&sortC=ASC_-1_FIRST&rStp=&cStp=&rDCh=&cDCh=&rDM=true&cDM=true&footnes=false&empty=false&wai=false&time_mode=ROLLING&time_most_recent=false&lang=EN&cfo=%23%23%23,%23%23%23.%23%23%23"))
closeAllConnections()
mylist <- readHTMLTable(mylines, asText=TRUE)
mytable <- mylist$xTable

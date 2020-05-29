# library
#library(dplyr)

datasetOnlyWithCountries <- subset(GSAF5_refined, `Site Type` == 'Country')
sites <- count(datasetOnlyWithCountries['Site'], Site)
orderedSites <- sites[order(-sites$n),]
topSites <- orderedSites[1:10,]
tableTopSites <- table(topSites$Site, topSites$n)
par(mar = c(5, 10, 2, 2))
barplot(height = topSites$n, names.arg = topSites$Site, main="Incident Count by Country", xlab="Country", horiz=TRUE, las = 2)
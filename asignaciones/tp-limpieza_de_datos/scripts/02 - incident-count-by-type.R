types <- table(GSAF5_refined['Type'])
par(mar = c(5, 5, 2, 2))
barplot(types, main="Incident Count by Type", xlab="Incident Type")
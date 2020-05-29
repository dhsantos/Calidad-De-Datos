types <- table(GSAF5_refined['Site Type'])
par(mar = c(5, 5, 3, 2))
barplot(types, main="Candidad de incidentes: Países vs Otros", xlab="Tipo de Site")
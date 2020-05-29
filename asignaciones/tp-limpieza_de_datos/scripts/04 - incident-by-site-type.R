types <- table(GSAF5_refined['Site Type'])
barplot(types, main="Incidents specifying Country vs Other", xlab="Site Type")
import pandas as  pd
import matplotlib.pyplot as plt
import numpy as np

def crearDataFrame(dataFrame, columna):
	res = dataFrame[[columna]].fillna('DESCONOCIDO').groupby([columna])[columna].count().reset_index(name='Cantidad')
	res = res.sort_values(by="Cantidad", ascending = False)
	res["Porcentaje"] = res["Cantidad"]/res["Cantidad"].sum() * 100
	res = res.sort_values(by="Cantidad", ascending = False).reset_index()
	del res['index']
	return res

def crearDataFrameNumerico(dataFrame, columna):
	res = dataFrame[[columna]].groupby([columna])[columna].count().reset_index(name='Cantidad')
	res = res.sort_values(by="Cantidad", ascending = False)
	res["Porcentaje"] = res["Cantidad"]/res["Cantidad"].sum() * 100
	res = res.sort_values(by="Cantidad", ascending = False).reset_index()
	del res['index']
	return res


def graficoBarras(dataFrame, columna, fullDF):

	fullDF = fullDF.sort_values(by=columna, ascending = False)
	moda = "La moda es :" + str(fullDF[columna].mode().values[0])
	indice = (fullDF[columna].count() + 1) // 2
	mediana = "La mediana es :" + str(fullDF[columna].values[indice])
	datos = moda + '\n' + mediana

	ax = dataFrame.head(15).plot.barh(x=columna, y= 'Cantidad', rot=0, figsize=(15,15), fontsize = 13, title= 'Proyeccion de valores de ' + columna)
	mean = dataFrame['Cantidad'].mean()
	ax.axvline(mean, color='r', linestyle='--', lw=2, label ='Promedio')
	plt.legend(loc='upper right', fontsize=20)
	plt.figtext(0.5, 0.01, datos, wrap=True, horizontalalignment='center', fontsize=20)
	plt.savefig('analisisUnivariado/'+ columna.lower()+'.png') 


def graficoPuntos(columna, fullDF):

	fullDF = fullDF.sort_values(by=columna, ascending = False)
	moda = "La moda es :" + str(fullDF[columna].mode().values[0])
	indice = (fullDF[columna].count() + 1) // 2
	mediana = "La mediana es :" + str(fullDF[columna].values[indice])
	datos = moda + '\n' + mediana

	fullDF = fullDF[columna].dropna()
	fullDF = fullDF.reset_index()
    
	fullDF["etiquetas"] = fullDF[columna]
	mean = fullDF[columna].mean()

	ax = fullDF.plot.scatter(x='index', y= columna, c='etiquetas' ,colormap='terrain', figsize=(15,15), title= 'Los 15 mas repetidos de ' + columna)
	ax.axhline(mean, color='r', linestyle='--', lw=2, label ='Promedio')
	plt.legend(loc='upper right', fontsize=20)
	plt.figtext(0.5, 0.01, datos, wrap=True, horizontalalignment='center', fontsize=20)
	plt.savefig('analisisUnivariado/'+ columna.lower()+'.png') 
	plt.cla()
	plt.clf()


def graficoBoxplot(columna, fullDF):

	primerCuartil = fullDF[columna].dropna().quantile(.25)  
	medio = fullDF[columna].dropna().quantile(.5)  
	tercerCuartil = fullDF[columna].dropna().quantile(.75)  
	minimo = fullDF[columna].dropna().min() 
	maximo = fullDF[columna].dropna().max()
	mean = round(fullDF[columna].dropna().mean(),2)

	
	ax = fullDF[columna].dropna().plot.box()

	ax.axhline(primerCuartil, color='r', linestyle='--', lw=2, label ='Cuartil 25: ' + str(primerCuartil))	
	ax.axhline(medio, color='r', linestyle='--', lw=2, label ='Cuartil 50: ' + str(medio))
	ax.axhline(tercerCuartil, color='r', linestyle='--', lw=2, label ='Cuartil 75: ' + str(tercerCuartil))
	ax.axhline(minimo, color='b', linestyle='--', lw=2, label ='Minimo: ' + str(minimo))
	ax.axhline(maximo, color='b', linestyle='--', lw=2, label ='Maximo: ' + str(maximo))
	#ax.axhline(mean, color='g', linestyle=':', lw=2, label ='Promedio: ' + str(mean))

	plt.title('Boxplot de ' + columna)
	plt.legend(loc='upper right', fontsize=20)
	plt.savefig('analisisUnivariado/'+ columna.lower()+'-boxplot.png')
	plt.cla()
	plt.clf()


if __name__ == "__main__":

	obras = pd.read_csv("obras.csv")
	
	obras['Numero'] = obras['Numero'].astype("Int64")
	obras['Comuna'] = obras['Comuna'].astype("Int64")
	obras['Longitud'] = obras['Longitud'].astype("float64")
	obras['Latitud'] = obras['Latitud'].astype("float64")
	obras['MetrosCuadrados'] = obras['MetrosCuadrados'].astype("float64")
	obras.info()
	print(obras)
#Barrio
	columna = "Barrio"
	barrio = crearDataFrame(obras, columna)
	barrio.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(barrio, columna, obras)
	barrio["Barrio"].describe()


#Expediente
	columna = "Expediente"
	expedientes = crearDataFrame(obras, columna)
	expedientes.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(expedientes, columna, obras)

#FechaRegistro
	columna = "FechaRegistro"
	fechaRegistro = crearDataFrame(obras, columna)
	fechaRegistro.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(fechaRegistro, columna, obras)

#Calle
	columna = "Calle"
	calle = crearDataFrame(obras, columna)
	calle.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(calle, columna, obras)

#Tipo
	columna = "Tipo"
	tipo = crearDataFrame(obras, columna)
	tipo.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(tipo, columna, obras)

#CodigoPostal
	columna = "CodigoPostal"
	codigoPostal = crearDataFrame(obras, columna)
	codigoPostal.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(codigoPostal, columna, obras)

#Comuna
	columna = "Comuna"
	comuna = crearDataFrame(obras, columna)
	comuna.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(comuna, columna, obras)

#AlturaObra
	columna = "AlturaObra"
	alturaObra = crearDataFrame(obras, columna)
	alturaObra.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(alturaObra, columna, obras)

#Parcela
	columna = "Parcela"
	parcela = crearDataFrame(obras, columna)
	parcela.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(parcela, columna, obras)

#Manzana
	columna = "Manzana"
	manzana = crearDataFrame(obras, columna)
	manzana.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoBarras(manzana, columna, obras)

#Numero
	columna = "Numero"
	numero = crearDataFrameNumerico(obras, columna)
	numero.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoPuntos(columna,obras)
	graficoBoxplot(columna,obras)

#Seccion
	columna = "Seccion"
	seccion = crearDataFrameNumerico(obras, columna)
	seccion.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoPuntos(columna,obras)
	graficoBoxplot(columna,obras)

#MetrosCuadrados
	columna = "MetrosCuadrados"
	metrosCuadrados = crearDataFrameNumerico(obras, columna)
	metrosCuadrados.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoPuntos(columna,obras)
	graficoBoxplot(columna,obras)

#Latitud
	columna = "Latitud"
	latitud = crearDataFrameNumerico(obras, columna)
	latitud.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoPuntos(columna,obras)
	graficoBoxplot(columna,obras)

#Longitud
	columna = "Longitud"
	longitud = crearDataFrameNumerico(obras, columna)
	longitud.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoPuntos(columna,obras)
	graficoBoxplot(columna,obras)

#Zona
	columna = "Zona"
	longitud = crearDataFrameNumerico(obras, columna)
	longitud.to_csv('analisisUnivariado/'+ columna.lower()+'.csv', index = False)
	graficoPuntos(columna,obras)
	graficoBoxplot(columna,obras)	
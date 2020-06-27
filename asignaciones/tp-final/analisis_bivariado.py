import pandas as  pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

	obras = pd.read_csv("obras.csv")
	
	obras['Numero'] = obras['Numero'].astype("Int64")
	obras['Comuna'] = obras['Comuna'].astype("Int64")
	obras['Longitud'] = obras['Longitud'].astype("float64")
	obras['Latitud'] = obras['Latitud'].astype("float64")
	obras['MetrosCuadrados'] = obras['MetrosCuadrados'].astype("float64")
	
	#Latitud y Longitud
	print ("La medias de Longitud es : " + str(obras["Longitud"].mean()))
	print ("La medias de Latitud es: " + str(obras["Latitud"].mean()))

	print ("La diferencia entre medias es: " + str(obras["Longitud"].mean() - obras["Latitud"].mean()))

	plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
	plt.scatter('Longitud', 'Latitud', 
                data=obras[["Longitud","Latitud"]], 
                s=20)
	plt.xticks(fontsize=12); plt.yticks(fontsize=12)
	plt.title("Disperción entre Longitud y Latitud", fontsize=22)
	plt.xlabel("Longitud")
	plt.ylabel("Latitud")
	plt.savefig('analisisBivariado/latitud-longitud.png') 
	plt.cla()
	plt.clf()

	# Barrio y MetrosCuadrados

	barrioMetros = obras[["Barrio","MetrosCuadrados"]]
	barrioMetros = barrioMetros.groupby(['Barrio'])["MetrosCuadrados"].sum()
	ax = barrioMetros.plot.barh(x="MetrosCuadrados", y= "Barrio", rot=0, figsize=(15,15), fontsize = 13, title= 'Cantidad de metros cuadrados por barrio')
	plt.legend(loc='upper right', fontsize=20)
	plt.savefig('analisisBivariado/barrio-metros.png') 
	plt.cla()
	plt.clf()

	# Comuna y MetrosCuadrados
	comunaMetros = obras[["Comuna","MetrosCuadrados"]]
	comunaMetros = comunaMetros.groupby(['Comuna'])["MetrosCuadrados"].sum()
	ax = comunaMetros.plot.barh(x="MetrosCuadrados", y= "Comuna", rot=0, figsize=(15,15), fontsize = 13, title= 'Cantidad de metros cuadrados por barrio')
	plt.legend(loc='upper right', fontsize=20)
	plt.savefig('analisisBivariado/comuna-metros.png') 
	plt.cla()
	plt.clf()
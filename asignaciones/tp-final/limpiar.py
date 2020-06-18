import pandas as  pd

if __name__ == "__main__":

	obras = pd.read_csv("obras-registradas-junsep2019.csv")
	obras['calle_altura'] = obras['calle_altura'].astype("Int64")

	nomenclatura = pd.DataFrame(obras['nomenclacion_par'].str.split('-',3).tolist(), columns = ['Zona','Seccion','Manzana','Parcela'])
	
	direccion =  pd.DataFrame(obras['direccion'].str.split(' ',2).tolist(), columns = ['Calle','Altura1','Altura2'])
	direccion['AlturaObra'] = direccion['Altura2']
	direccion.loc[pd.isna(direccion['Altura2']), 'AlturaObra'] = direccion['Altura1']
	direccion = direccion[['AlturaObra']]

	obras = pd.concat([obras, nomenclatura, direccion], axis=1, join='inner')

	obras = obras[["nro_exp","fecha_registro_p","calle_nombre","calle_altura", "AlturaObra", 'Zona','Seccion','Manzana','Parcela',"barrio","comuna","codigo_postal_argentino","tipo_obra","metros_cuadrados_obra", "long", "lat"]].drop_duplicates()
	obras.rename(columns={'nro_exp': 'Expediente', 'fecha_registro_p': 'FechaRegistro','calle_nombre': 'Calle','calle_altura': 'Numero','barrio': 'Barrio' ,'comuna': 'Comuna' ,'codigo_postal_argentino': 'CodigoPostal' ,'tipo_obra': 'Tipo' ,'metros_cuadrados_obra': 'MetrosCuadrados' ,'long': 'Longitud' ,'lat': 'Latitud' }, inplace=True)           

	obras.to_csv('obras.csv', index = False)
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
	obras.info()
	print(obras)
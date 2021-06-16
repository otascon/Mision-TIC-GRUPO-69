
datos = ['linea uno','linea dos','linea tres','linea 4','linea 5']

ruta_3 = r'c:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\CICLO_UNO\GRUPO_69\Semana 5\archivo6_3.txt'

fichero = open(ruta_3, 'w')

#fichero.writelines(datos)
fichero.writelines('%s\n' % s for s in datos)
fichero.close()


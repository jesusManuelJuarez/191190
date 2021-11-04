from imgurpython import ImgurClient
import urllib.request
import timeit
import os
from multiprocessing import Pool


#VARIABLES
selecto_usuario = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_usuario = "bfa0e227a1c5643"
usuario = ImgurClient(id_usuario, selecto_usuario)


def descarga_url_img(link): #METODO PARA LA DESCARGA DE URL
   print(link)
   name = link.split("/")[3] # OBTIENE EL CORTE DE LA URL
   format = nombre_img.split(".")[1]
   name = nombre_img.split(".")[0]
   print(name, format)
   url_local = "C:/Users/chuya/images{}.{}" #SE ASIGNA LA UBICACIÓN
   urllib.request.urlretrieve(link, url_local.format(name, format)) #GUARDA EN LOCAL LAS IMAGENES
 
 
def main(): #METODO PRINCIPAL
   id_album = "bUaCfoz"
   imagen = cliente.get_album_images(id_album)
   hilos = len(imagen)
   with Pool(processes=hilos) as pool:
      pool.map(descarga_url_img,imagen)

if __name__ == "__main__":
   print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))

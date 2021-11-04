from concurrent.futures import ThreadPoolExecutor
import timeit
from imgurpython import ImgurClient
import os
import urllib.request
#VARIABLES
selecto_usuario = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
cliente = ImgurClient(id_cliente, selecto_usuario)

def descarga_url_img(link): # METODO PARA LA DESCARGA DEL URL
   print(link)
   name = link.split("/")[3]  # SE OBTIENE EL CORTE DE LA URL
   format = nombre_img.split(".")[1]
   name = nombre_img.split(".")[0]
   print(name, format)
   url_local = "C:/Users/chuya/images{}.{}"
   urllib.request.urlretrieve(link, url_local.format(name, format)) #GUARDA DE FORMA LOCAL LOS DATOS

def main(): #METODO PRINCIPAL
   id_album = "bUaCfoz" #ASIGNACIÓN DE ID AL ALBUM
   imagen = cliente.get_album_images(id_album) #SE OBTIENE EL LINK
   hilos = len(imagen)
 
   with ThreadPoolExecutor (max_workers= hilos) as executor:
       executor.map (descarga_url_img, imagen)
 
 
if __name__ == "__main__":
   print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1))) #SE MUESTRA EL TIEMPO DE LA DESCARGA

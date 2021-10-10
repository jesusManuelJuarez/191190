import time
import random
import threading
#DESIGNACIÓN DE VARIABLES
N = 5
TIEMPO_TOTAL = 3

class filosofo(threading.Thread):
    #ASEGURA LA EXCLUSION MUTUA
    semaforo = threading.Lock()
    # ARREGLO PARA CONOCER EL ESTADO DE CADA FILOSOFO
    estado = []
    # ARREGLO DE SEMAFOROS PARA SINCRONIZAR ENTRE FILOSOFOS, MUESTRA QUIEN ESTA EN COLA DEL TENEDOR
    tenedores = []
    count=0

    def __init__(self):
        super().__init__()
        # ASIGNA EL ID
        self.id=filosofo.count
        # CONTADOR 1 +1
        filosofo.count+=1
        # EL FILOSOFO ENTRA A LA MESA EN ESTADO PENSANDO
        filosofo.estado.append('PENSANDO')
        # AGREGA EL SEMAFORO DE SU TENEDOR( TENEDOR A LA IZQUIERDA)
        filosofo.tenedores.append(threading.Semaphore(0))
        print("FILOSOFO {0} - PENSANDO".format(self.id))
    #FUNCIONES PARA ASIGNAR ESTADOS Y UBICACIÓN

    # NECESARIO PARA SABER CUANDO TERMINA EL THREAD
    def __del__(self):
        print("FILOSOFO {0} - Se para de la mesa".format(self.id))

    # CADA FILOSOFO SE TOMA DISTINTO TIEMPO PARA PENSAR, ALEATORIO
    def pensar(self):
        time.sleep(random.randint(0,5))

    # BUSCAMOS EL INDICE DE LA DERECHA
    def derecha(self,i):
        return (i-1)%N

    # BUSCAMOS EL INDICE DE LA IZQUIERDA
    def izquierda(self,i):
        return(i+1)%N

    #VERIFICA EL ESTADO DE LOS FILOSOFOS
    def verificar(self,i):
        if filosofo.estado[i] == 'HAMBRIENTO' and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':
            filosofo.estado[i]='COMIENDO'
            filosofo.tenedores[i].release()  #SI SUS VECINOS NO ESTAN COMIENDO AUMENTA EL SEMAFORO DEL TENEDOR Y CAMBIA SU ESTADO A COMIENDO

    def tomar(self):
        # SEÑALA QUE TOMARA LOS TENEDORES (EXCLUSION MUTUA)
        filosofo.semaforo.acquire()
        filosofo.estado[self.id] = 'HAMBRIENTO'
        # VERIFICA SUS VECINOS, SI NO PUEDE COMER NO SE BLOQUEARA EN EL SIGUIENTE ACQUIRE
        self.verificar(self.id)
        # SEÑALA QUE YA DEJO DE INTENTAR TOMAR LOS TENEDORES (CAMBIAR EL ARRAY ESTADO)
        filosofo.semaforo.release()
        # SOLO SI PODIA TOMARLOS SE BLOQUEARA CON ESTADO COMIENDO
        filosofo.tenedores[self.id].acquire()

    #LIBERA LOS TENEDONES
    def soltar(self):
        # SEÑALA QUE SOLTARA LOS TENEDORES
        filosofo.semaforo.acquire()
        filosofo.estado[self.id] = 'PENSANDO'
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        # YA TERMINO DE MANIPULAR TENEDORES
        filosofo.semaforo.release()
    # TIEMPO ARBITRARIO PARA COMER
    def comer(self):
        print("FILOSOFO {} COMIENDO".format(self.id))
        time.sleep(2)
        print("FILOSOFO {} TERMINO DE COMER".format(self.id))

    def run(self):
        for i in range(TIEMPO_TOTAL):
            # EL FILOSOFO PIENSA
            self.pensar()
            # AGARRA LOS TENEDORES CORRESPONDIENTES
            self.tomar()
            self.comer()
            # SUELTA LOS TENEDORES
            self.soltar()

def main():
    lista=[]
    for i in range(N):
        # AGREGA UN FILOSOFO A LA LISTA
        lista.append(filosofo())

    for f in lista:
        # ES EQUIVALENTE A RUN()
        f.start()

    for f in lista:
        # BLOQUEA HASTA QUE TERMINA EL THREAD
        f.join()

if __name__=="__main__":
    main()

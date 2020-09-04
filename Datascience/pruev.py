from ListaVF import List_of_frecuenci_trip
from ListaVF import saving_list
from ListaVF import current_list

def SaveCycle(curren_trip):
    frecuenci_trip = current_list()
    List_of_frecuenci_trip(curren_trip,frecuenci_trip)
    saving_list(frecuenci_trip)

if __name__ == "__main__":
    SaveCycle('Colombia')
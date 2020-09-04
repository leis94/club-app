
def FrecuencyPlace(current_trip,frecuenci_tryp):
    
    for trip in frecuenci_tryp:
        if current_trip == trip:
            place = trip
            value = frecuenci_tryp[trip]
            break
        else:
            place = None
    
    if current_trip == place:
        value = value + 1
        respaldo = frecuenci_tryp.copy()
        frecuenci_tryp.update({place:value})
    else:
        frecuenci_tryp.update({current_trip:1})
    return frecuenci_tryp

def FrecuencyList(places):
    maxim = 0
    medium = 0
    mini = 0
    for place in places:
        if places[place]>= maxim:
            mini = medium
            medium = maxim
            maxim = places[place]
        elif places[place] >= medium:
            mini = medium
            medium = places[place]
        elif places[place] >= mini:
            mini= places[place]
        else:
            pass
    values = places.values()
    keys = places.keys()
    inverted_dictionary = dict(zip(values,keys))
    first_place = inverted_dictionary[maxim]
    second_place = inverted_dictionary[medium]
    thirth_place = inverted_dictionary[mini]
    lugares_frecuentes = [first_place,second_place,thirth_place]
    return lugares_frecuentes


def List_of_frecuenci_trip(current_trip, frecuenci_tryp):
    places = FrecuencyPlace(current_trip,frecuenci_tryp)
    list_of_frequent_places = FrecuencyList(places)
    frecuenci_tryp.update(places)
    return list_of_frequent_places

def current_list():
    archivo = open('lugares_frecuente.txt','r')
    frecuenci_tryp_str = archivo.read()
    frecuenci_tryp={}
    for line in frecuenci_tryp_str.splitlines():
	    valores=line.split(":",1)
	    frecuenci_tryp[valores[0].strip()]=int(valores[1].strip())
    archivo.close
    return frecuenci_tryp

def saving_list(frecuenci_tryp,):
    archivo = open('lugares_frecuente.txt', 'w')
    frec_trip = str(frecuenci_tryp)
    frec_trip = frec_trip.replace('{','')
    frec_trip = frec_trip.replace('}','')
    frec_trip = frec_trip.replace(',','\n')
    frec_trip = frec_trip.replace("'",'')
    archivo.write(frec_trip)
    archivo.close

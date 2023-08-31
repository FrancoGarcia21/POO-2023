import requests #la importacion no existe / calculo que es parte del ejercicio
from zipfile import ZipFile

class ConexionHTTP: ## No respeta el Single Responsibility , Ya que tiene metodos que no deberian
    #ser de la clase , que deberian estar en otra
    
    def __init__(self, url):
        self.__url = url ## no estaba el objeto en privado / Open-Close?
        

    def peticionTCP(self):
        res = requests.get(self.__url)
        print(res)

    def imprimir_encabezados(self):
        res = requests.get(self.__url)
        print(res.headers)

    def respuesta(self):## NO NECESITABA pasar el URL por parametro / ya que este en el constructor
        return requests.get(self.__url)
    
    def peticion_con_parametros(self): ### porque pediria los parametros en esta clase?? 
        '''param es un dict con los paramtros a enviar en la peticion'''
        param = input("ingrese parametro: ")
        res = requests.get(self.__url, params={'parametro':param})## estaba mal tipeado la manera
        # de mostrar un elemento del diccionario --- No reconzco el Patro que no respeta
        # o si solo estaba mal tipiado
        
    def parsear_json(self):# no se porque estaria esta funcion en la Clase ConexionHTTP
        '''transforma la respuesta a un json '''## aca no deberia esta por sigle responsibility
        pass
    
    '''
    La single responsibility no se cumple porque tiene metodos que no deberian estar en esta clase?
    
    Open-Close porque los atributos del constructor no estaban cerrados ?
    
    Liskov no hay herencia asi que no deberia aparecer en ningun lado
    
    Interface Segregation tampoco lo veo
    '''
class Vehiculos():
    
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frenar=True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
             "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
        
class furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
        
class Moto(Vehiculos):      # Hereda las propiedades y métodos de la clase Vehículo
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"    # Ahora un objeto de tipo moto tiene 6 métodos.

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
            "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)
    
class vElectricos(Vehiculos):
    def __init__(self,marca,modelo):
        
        super().__init__(marca,modelo)
        self.autonomia=100
        
    def __cargarEnergia__(self):
        self.cargando=True
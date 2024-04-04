from sortareMasini.Domain.Masina import Masina


class fileRepository:
    def __init__(self, textFile):
        self.__masinaDictionary = {}
        self._readFromFile(textFile)

    def getAllEntities(self):
        return list(self.__masinaDictionary.values())

    def addEntity(self, entity):
        self.__masinaDictionary[entity.get_tokenMasina()] = entity

    def _readFromFile(self, textFile):
        f = open(textFile, "r")
        line = f.readline()
        while line != "":
            attr = line.split()

            marca = attr[0]
            model = attr[1]
            tokenMasina = attr[2]
            pretAchizitie = attr[3]
            pretVanzare = attr[4]


            car = Masina(marca, model, tokenMasina, pretAchizitie, pretVanzare)

            self.addEntity(car)

            line = f.readline()

        f.close()
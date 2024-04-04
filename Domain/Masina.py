class Masina:
    def __init__(self, marca, model, tokenMasina, pretAchizitie, pretVanzare):
        self.__marca = marca
        self.__model = model
        self.__tokenMasina = tokenMasina
        self.__pretAchizitie = pretAchizitie
        self.__pretVanzare = pretVanzare

    def get_marca(self):
        return self.__marca

    def get_model(self):
        return self.__model

    def get_tokenMasina(self):
        return self.__tokenMasina

    def get_pretAchizitie(self):
        return self.__pretAchizitie

    def get_pretVanzare(self):
        return self.__pretVanzare

    def get_profit(self):
        return int(self.__pretVanzare) - int(self.__pretAchizitie)

    def compare_marca(self,other):
        return self.__marca.strip()> other.get_marca().strip()



    def __str__(self):
        return f'{self.__marca} {self.__model} {self.__tokenMasina} {self.__pretAchizitie} {self.__pretVanzare} \n'
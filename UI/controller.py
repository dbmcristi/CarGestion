from sortareMasini.Service import  masinaService,bubbleSortService,sortService,searchService

class Controller:
    def __init__(self, masinaServ: masinaService,bubbleSortService: bubbleSortService,sortService : sortService,searchService : searchService):
        self.__masinaService = masinaServ
        self.__bubbleSortService = bubbleSortService
        self.__sortService = sortService
        self.__searchService = searchService

    def showCarsWithToken(self):
        tokenMasina = input("Alegeti un token al unei masini: ")
        self.__masinaService.getCarsByToken(tokenMasina)

    def sortCarsToken(self):
        self.__masinaService.sortareEficienta(0, 0, 1, 0, 0, 0)

    def sortCarsMarcaModel(self):
        self.__masinaService.sortareEficienta(1, 1, 0, 0, 0, 0)

    def sortCarsMarcaModelToken(self):
        self.__masinaService.sortareEficienta(1, 1, 1, 0, 0, 0)

    def sortCarsProfit(self):
        self.__masinaService.sortareEficienta(0, 0, 0, 0, 0, 1)

    def menuMerge(self):
        print("1. Afiseaza masinile cu tokenul ales: ")
        print("2. Sorteaza masinile dupa tokenMasina: ")
        print("3. Sorteaza masinile dupa marca si model: ")
        print("4. Sorteaza masinile dupa marca, model si token: ")
        print("5. Sorteaza masinile dupa profit: ")

    def controllerMain(self):
        while True :
            inp = input("Tipul sortarii: Bubble/Merge/Python")
            if(inp == "Merge") :
                self.menuMerge()
                alegere = input("Alegeti o varianta: ")

                if alegere == "1":
                    self.showCarsWithToken()
                if alegere == "2":
                    self.sortCarsToken()
                if alegere == "3":
                    self.sortCarsMarcaModel()
                if alegere == "4":
                    self.sortCarsMarcaModelToken()
                if alegere == "5":
                    self.sortCarsProfit()

            elif inp  == "Bubble" :
                self.menuMerge()
                alegere = input("Alegeti o varianta: ")
                if alegere == "1":
                    token = input("Introduceti token: ")

                    self.__searchService.searchSorted(token)
                    print("--------------------------------------------------")
                    self.__searchService.searchFiltered(token)

                if alegere == "2":
                    # token
                    self.__bubbleSortService.bubbleSort_token()

                if alegere == "3":
                    # marca model
                    self.__bubbleSortService.bubbleSort_marca_model()

                if alegere == "4":
                    # marca model token
                    self.__bubbleSortService.bubbleSort_marca_model_token()

                if alegere == "5":
                    # profit
                    self.__bubbleSortService.bubbleSort_profit()

            elif inp == "Python":
                self.menuMerge()
                alegere = input("Alegeti o varianta: ")
                if alegere == "2":
                    # token
                    self.__sortService.sort_token()

                if alegere == "3":
                    # marca model
                    self.__sortService.sort_marca_model()

                if alegere == "4":
                    # marca model token
                    self.__sortService.sort_marca_model_token()

                if alegere == "5":
                    # profit
                    self.__sortService.sort_profit()

from functools import wraps
import time
import timeit
from sortareMasini.fileRepository import fileRepository

class Service:
    def __init__(self, fileRepo: fileRepository):
        self.__fileRepository = fileRepo

    def getAllEntitiesService(self):
        return self.__fileRepository.getAllEntities()

    def getCarsByToken(self, tokenInput):
        listOfCars = self.getAllEntitiesService()

        beginTime = time.time()

        for token in listOfCars:
            if tokenInput == token.get_tokenMasina():
                print(token)

        endTime = time.time()

        print("Time=", "{:.6f}".format(endTime - beginTime))

    def sortToken(self, sub_array1, sub_array2, listCarTuples, i, j, k):

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i][2] < sub_array2[j][2]:
                listCarTuples[k] = sub_array1[i]
                i += 1
            else:
                listCarTuples[k] = sub_array2[j]
                j += 1
            k += 1
        return listCarTuples, sub_array1, sub_array2, i, j, k


    def sortMarcaModel(self, sub_array1, sub_array2, listCarTuples, i, j, k):

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i][0] == sub_array2[j][0]:
                if sub_array1[i][1] < sub_array2[j][1]:
                    listCarTuples[k] = sub_array1[i]
                    i += 1
                else:
                    listCarTuples[k] = sub_array2[j]
                    j += 1
            else:
                if sub_array1[i][0] < sub_array2[j][0]:
                    listCarTuples[k] = sub_array1[i]
                    i += 1
                else:
                    listCarTuples[k] = sub_array2[j]
                    j += 1
            k += 1
        return listCarTuples, sub_array1, sub_array2, i, j, k

    def sortMarcaModelToken(self, sub_array1, sub_array2, listCarTuples, i, j, k):

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i][0] == sub_array2[j][0]:
                if sub_array1[i][1] == sub_array2[j][1]:
                    if sub_array1[i][2] < sub_array2[j][2]:
                        listCarTuples[k] = sub_array1[i]
                        i += 1
                    else:
                        listCarTuples[k] = sub_array2[j]
                        j += 1
                else:
                    if sub_array1[i][1] < sub_array2[j][1]:
                        listCarTuples[k] = sub_array1[i]
                        i += 1
                    else:
                        listCarTuples[k] = sub_array2[j]
                        j += 1
            else:
                if sub_array1[i][0] < sub_array2[j][0]:
                    listCarTuples[k] = sub_array1[i]
                    i += 1
                else:
                    listCarTuples[k] = sub_array2[j]
                    j += 1
            k += 1
        return listCarTuples, sub_array1, sub_array2, i, j, k


    def sortProfit(self, sub_array1, sub_array2, listCarTuples, i, j, k):

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i][5] < sub_array2[j][5]:
                listCarTuples[k] = sub_array1[i]
                i += 1
            else:
                listCarTuples[k] = sub_array2[j]
                j += 1
            k += 1
        return listCarTuples, sub_array1, sub_array2, i, j, k

    def mergeSort(self, listCarTuples, marca, model, token, pretAchizitie, pretVanzare, profit):

        if len(listCarTuples) > 1:

            # Create sub_array2 ← A[start - mid] and sub_array2 ← A[mid+1 - end]
            mid = len(listCarTuples) // 2
            sub_array1 = listCarTuples[:mid]
            sub_array2 = listCarTuples[mid:]

            # Sort the two halves
            self.mergeSort(sub_array1, marca, model, token, pretAchizitie, pretVanzare, profit)
            self.mergeSort(sub_array2, marca, model, token, pretAchizitie, pretVanzare, profit)

            # Initial values for pointers that we use to keep track of where we are in each array
            i = j = k = 0

            # Until we reach the end of either start or end, pick larger among
            # elements start and end and place them in the correct position in the sorted array
            if token == 1 and model == marca == pretAchizitie == pretVanzare == profit == 0:
                listCarTuples, sub_array1, sub_array2, i, j, k = self.sortToken(sub_array1, sub_array2, listCarTuples, i, j, k)

            if marca == model == 1 and token == pretAchizitie == pretVanzare == profit == 0:
                listCarTuples, sub_array1, sub_array2, i, j, k = self.sortMarcaModel(sub_array1, sub_array2,
                                                                                listCarTuples, i, j, k)

            if marca == model == token == 1 and pretAchizitie == pretVanzare == profit == 0:
                listCarTuples, sub_array1, sub_array2, i, j, k = self.sortMarcaModelToken(sub_array1, sub_array2,
                                                                                listCarTuples, i, j, k)

            if marca == model == token == pretAchizitie == pretVanzare == 0 and profit == 1:
                listCarTuples, sub_array1, sub_array2, i, j, k = self.sortProfit(sub_array1, sub_array2,
                                                                                listCarTuples, i, j, k)
            # When all elements are traversed in either arr1 or arr2,
            # pick up the remaining elements and put in sorted array
            while i < len(sub_array1):
                listCarTuples[k] = sub_array1[i]
                i += 1
                k += 1

            while j < len(sub_array2):
                listCarTuples[k] = sub_array2[j]
                j += 1
                k += 1

        return listCarTuples

    def timer(self, mergeSort):
        @wraps(mergeSort)
        def wrapper(*args):
            start_time = time.time()
            retVal = self.mergeSort(*args)
            duration = time.time() - start_time
            print("the function ends in ", duration, "secs")
            return retVal
        return wrapper

    def getCars(self):
        listOfTuples = []
        listOfCars = self.getAllEntitiesService()
        for cars in listOfCars:
            marca = cars.get_marca()
            model = cars.get_model()
            token = cars.get_tokenMasina()
            pret_achizitie = cars.get_pretAchizitie()
            pret_vanzare = cars.get_pretVanzare()

            profit = int(pret_vanzare) - int(pret_achizitie)
            listOfTuples.append((marca, model, token, pret_achizitie, pret_vanzare, profit))

        return listOfTuples

    def sortareEficienta(self, *args):  # *args -> Doesn't give a freak about how many variables you are giving
        listOfCarsTuples = self.getCars()

        beginTime = timeit.default_timer()

        listOfCarsTuples = self.mergeSort(listOfCarsTuples, *args)

        endTime = timeit.default_timer()

        print("Time=","{:.6f}".format(endTime-beginTime))

        print(self.timer(self.mergeSort(listOfCarsTuples, *args)))

        print(listOfCarsTuples)

    ###### BubbleSort
    def bubbleSortMarcaModel(self):
        masini = self.__fileRepository.getAllEntitiesService()
        for masina in masini:
            ...

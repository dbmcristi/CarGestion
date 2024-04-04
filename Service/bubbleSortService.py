import sys
import time
from functools import cmp_to_key

from sortareMasini.Domain import Masina
from sortareMasini.Service.comparators import Comparators
from sortareMasini.fileRepository import fileRepository

class BubbleSortService():
    def __init__(self,fileRepository: fileRepository):
        self.__fileRepository = fileRepository

    def bubbleSort_marca_model_token(self):
        self.bubbleSort("marca model token")

    def bubbleSort_marca_model(self):
        self.bubbleSort("marca model")

    def bubbleSort_token(self):
        self.bubbleSort("token")

    def bubbleSort_profit(self):
        self.bubbleSort("profit")

    def bubbleSort_achizitie(self):
        self.bubbleSort("achizitie")

    def bubbleSort_vanzare(self):
        self.bubbleSort("vanzare")

    def bubbleSort(self,option):
        array = self.__fileRepository.getAllEntities()

        beginTime = time.time()
        for i in range(len(array)):
            swapped = False

            for j in range(0, len(array) - i - 1):

                # compare two adjacent elements
                #
                match option :
                    case "marca model token":
                        condition =Comparators.marca_model_token(array[j],array[j+1])
                    case "marca model":
                        condition =Comparators.marca_model(array[j],array[j+1])
                    case "token":
                        condition = Comparators.token(array[j], array[j + 1])
                    case "profit":
                        condition = Comparators.profit(array[j], array[j + 1])
                    case "achizitie":
                        condition = array[j].get_pretAchizitie() > array[j + 1].get_pretAchizitie()
                    case "vanzare":
                        condition = array[j].get_pretVanzare() > array[j + 1].get_pretVanzare()

                if condition == 1:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp

                    swapped = True

            if not swapped:
                break

        endTime = time.time()

        def myPrint(item):
            print("%s %s %s %s %s" % (str(item.get_marca()),
                                      "model=" + str(item.get_model()),
                                      "token=" + str(item.get_tokenMasina()),
                                      str(item.get_pretAchizitie()),
                                      str(item.get_pretVanzare())
                                      ))

        # [print(item) for item in array]
        [myPrint(item)for item in array]
        # [myPrint(item)for item in array[3:6]]
        print("Time=","{:.8f}".format(endTime-beginTime))

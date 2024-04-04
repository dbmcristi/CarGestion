import sys

import time
from functools import cmp_to_key
from sortareMasini.Service import comparators
from sortareMasini.Service.comparators import Comparators

from sortareMasini.fileRepository import fileRepository

class SortService():
    def __init__(self,fileRepository: fileRepository):
        self.__fileRepository = fileRepository

    def sort_marca_model(self):
            array = self.__fileRepository.getAllEntities()
            beginTime = time.time()

            data = sorted(array, key=cmp_to_key(Comparators.marca_model))

            endTime = time.time()

            def myPrint(item):
                print("%s %s %s %s %s" % (str(item.get_marca()),
                                          "model=" + str(item.get_model()),
                                          "token=" + str(item.get_tokenMasina()),
                                          str(item.get_pretAchizitie()),
                                          str(item.get_pretVanzare())
                                          ))

            # [print(item) for item in array]
            [myPrint(item) for item in data]
            # [myPrint(item)for item in array[3:6]]
            print("Time=", endTime - beginTime)

    def sort_marca_model_token(self):
            array = self.__fileRepository.getAllEntities()
            beginTime = time.time()

            data = sorted(array, key=cmp_to_key(Comparators.marca_model_token))

            endTime = time.time()

            def myPrint(item):
                print("%s %s %s %s %s" % (str(item.get_marca()),
                                          "model=" + str(item.get_model()),
                                          "token=" + str(item.get_tokenMasina()),
                                          str(item.get_pretAchizitie()),
                                          str(item.get_pretVanzare())
                                          ))

            # [print(item) for item in array]
            [myPrint(item) for item in data]
            # [myPrint(item)for item in array[3:6]]
            print("Time=", endTime - beginTime)

    def sort_token(self):
            array = self.__fileRepository.getAllEntities()
            beginTime = time.time()

            data = sorted(array, key=cmp_to_key(Comparators.token))

            endTime = time.time()

            def myPrint(item):
                print("%s %s %s %s %s" % (str(item.get_marca()),
                                          "model=" + str(item.get_model()),
                                          "token=" + str(item.get_tokenMasina()),
                                          str(item.get_pretAchizitie()),
                                          str(item.get_pretVanzare())
                                          ))

            # [print(item) for item in array]
            [myPrint(item) for item in data]
            # [myPrint(item)for item in array[3:6]]
            print("Time=", endTime - beginTime)

    def sort_profit(self):
        array = self.__fileRepository.getAllEntities()
        beginTime = time.time()

        data = sorted(array, key=cmp_to_key(Comparators.profit ))

        endTime = time.time()

        def myPrint(item):
            print("%s %s %s %s %s" % (str(item.get_marca()),
                                      "model=" + str(item.get_model()),
                                      "token=" + str(item.get_tokenMasina()),
                                      str(item.get_pretAchizitie()),
                                      str(item.get_pretVanzare())
                                      ))

        # [print(item) for item in array]
        [myPrint(item) for item in data]
        # [myPrint(item)for item in array[3:6]]
        print("Time=", endTime - beginTime)
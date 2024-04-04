import time
from functools import cmp_to_key

from sortareMasini.Service.comparators import Comparators
from sortareMasini.fileRepository import fileRepository

class SearchService:
    def __init__(self,fileRepository : fileRepository):
        self.__fileRepository = fileRepository

    def searchFiltered(self,token):
        cars = self.__fileRepository.getAllEntities()

        beginTime = time.time()

        result = list(filter(lambda x: x.get_tokenMasina() == token , cars))

        endTime = time.time()

        if len(result)>0:
            self.myPrint(result[0])
        else:
            print("Not found")

        print("Time=", endTime - beginTime)

    def searchSorted(self,token):
        cars = self.__fileRepository.getAllEntities()
        data = sorted(cars, key=cmp_to_key(Comparators.token))

        beginTime = time.time()

        result = list(filter(lambda x: x.get_tokenMasina() == token , data))

        endTime = time.time()
        if len(result)>0:
            self.myPrint(result[0])
        else:
            print("Not found")

        print("Time=","{:.6f}".format(endTime-beginTime))


    def myPrint(self,item):
        print("%s %s %s %s %s" % (str(item.get_marca()),
                                  "model=" + str(item.get_model()),
                                  "token=" + str(item.get_tokenMasina()),
                                  str(item.get_pretAchizitie()),
                                  str(item.get_pretVanzare())
                                  ))
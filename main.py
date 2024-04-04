from fileRepository.fileRepository import fileRepository
from Service.masinaService import Service
from UI.controller import Controller
from Service.bubbleSortService import BubbleSortService
from Service.sortService import SortService
from sortareMasini.Service.searchService import SearchService


def main():
    fileRepo = fileRepository("masini.txt")
    masinaServ = Service(fileRepo)
    bubbleSort = BubbleSortService(fileRepo)
    sortService = SortService(fileRepo)
    searchService = SearchService(fileRepo)
    controller = Controller(masinaServ,bubbleSort,sortService,searchService)

    controller.controllerMain()

main()
class Comparators:

    @staticmethod
    def marca_model(a, b):
        if a.get_marca().strip() < b.get_marca().strip():
            return -1
        if a.get_marca().strip() > b.get_marca().strip():
            return 1
        if a.get_model().strip() < b.get_model().strip():
            return -1
        if a.get_model().strip() > b.get_model().strip():
            return 1
        return 0

    @staticmethod
    def token(a, b):
        if a.get_tokenMasina().strip() < b.get_tokenMasina().strip():
            return -1
        if a.get_tokenMasina().strip() > b.get_tokenMasina().strip():
            return 1
        return 0

    @staticmethod
    def marca_model_token(a, b):
        rezultat = Comparators.marca_model(a, b)
        if rezultat == 0 :
            return Comparators.token(a,b)
            # token(a,b)
        return rezultat


    @staticmethod
    def profit(a, b):
        profitA =a.get_profit()
        profitB =b.get_profit()

        if profitA < profitB:
            return -1
        if profitA > profitB:
            return 1

        return 0
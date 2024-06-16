
class Manufacturer:

    def __init__(self,manufact,model,retailprice):
        self.__manufact=manufact
        self.__model=model
        self.__retail_price=retailprice

    def set_manufact(self,manufact):
        self.__manufact=manufact
    def set_model(self,model):
        self.__model=model
    def set_retail_price(self,retailprice):
        self.__retail_price=retailprice

    def get_manufact(self):
        return self.__manufact
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__retail_price
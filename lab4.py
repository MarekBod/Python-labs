class PreciousGem:

    def __init__(self, carats=0.0, price=0, name=None):
        self.__carats = carats
        self.__price = price
        self.__name = name
        self.public_number = 0
        self.public_string = "default"

    def __del__(self):
        print(f"Object {self.__name} is destroyed")


    def get_carats(self):
        return self.__carats

    def set_carats(self, carats):
        self.__carats = carats

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"PreciousGem(name={self.__name}, carats={self.__carats}, price={self.__price})"

    def __repr__(self):
        return f"PreciousGem(name='{self.__name}', carats={self.__carats}, price={self.__price})"

def main():
    gem1 = PreciousGem(1.5, 2000, "Ruby")
    gem2 = PreciousGem(2.0, 5000, "Diamond")
    gem3 = PreciousGem( 2.5 , 4000,"Emerald")
    gem4 = PreciousGem()
    print(gem1)
    print(gem2)
    print(gem3)
    print(gem4)
    print(repr(gem1))
    print(repr(gem2))
    print(repr(gem3))
    print(repr(gem4))

if __name__ == "__main__":
    main()




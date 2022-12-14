import copy

class Sheep:
    __name: str = ""
    __params: dict = {"weight": 20, "tall": .34}

    def __init__(self, donor: 'Sheep' = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())

    def set_name(self, name: str):
        self.__name = name
    
    def get_name(self) -> str:
        return self.__name
    
    def get_params(self) -> dict:
        return self.__params
    
    def set_weight(self, new_weight: int):
        self.__params['weight'] = new_weight
    
    def clone(self):
        # import pdb;pdb.set_trace()
        return Sheep(self)


if __name__ == "__main__":
    sheep_donor: Sheep = Sheep()
    sheep_donor.set_name("Dolly")

    sheep_clone: Sheep = sheep_donor.clone()

    print("Донор: ", sheep_donor.get_name(), sheep_donor.get_params())
    print("Клон: ", sheep_clone.get_name(), sheep_clone.get_params())

    sheep_clone.set_weight(35)
    sheep_clone.set_name("Новая Долли")

    print("Донор: ", sheep_donor.get_name(), sheep_donor.get_params())
    print("Клон: ", sheep_clone.get_name(), sheep_clone.get_params())
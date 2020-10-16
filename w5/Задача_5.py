class Mother:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return "Name:{}".format(self.__name)

class Daughter(Mother):
    def __init__(self, name, job):
        super().__init__(name)
        self.__job = job

    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job

    def __str__(self):
        return "Name:{}  Job:{}".format(self.get_name(), self.get_job())

print(Mother('Lisa'))
print(Daughter('Rose','Singer'))



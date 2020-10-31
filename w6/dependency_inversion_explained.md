* **Dependency inversion**: Пятый принцип соответствует букве D в SOLID, содержание этого принципа следующее:
1. Модули высокого уровня не должны зависеть от модулей низкого уровня. Оба должны зависеть от абстракций.
2. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
* **Пример**:
  * **Нарушение DIP**
```
class BackendDeveloper:
    """This is a low-level module"""
    @staticmethod
    def python():
        print("Writing Python code")
class FrontendDeveloper:
    """This is a low-level module"""
    @staticmethod
    def javascript():
        print("Writing JavaScript code")
class Project:
    """This is a high-level module"""
    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()
    def develop(self):
        self.backend.python()
        self.frontend.javascript()
        return "Develop codebase"
project = Project()
print(project.develop())
```
*Класс `Project` - это модуль высокого уровня, а `Backend` и `Frontend` - это модули низкого уровня. В этом примере мы обнаружили, что модуль высокого уровня зависит от модуля низкого уровня. Следовательно, в этом примере нарушается принцип инверсии зависимостей. Решим задачу по определению DIP.*
   * **Решение**:
   ```
class BackendDeveloper:
   """This is a low-level module"""
   def develop(self):
       self.__python_code()
   @staticmethod
   def __python_code():
       print("Writing Python code")
class FrontendDeveloper:
   """This is a low-level module"""
   def develop(self):
       self.__javascript()
   @staticmethod
   def __javascript():
       print("Writing JavaScript code")
class Developers:
   """An Abstract module"""
   def __init__(self):
       self.backend = BackendDeveloper()
       self.frontend = FrontendDeveloper()
   def develop(self):
       self.backend.develop()
       self.frontend.develop()
class Project:
   """This is a high-level module"""
   def __init__(self):
       self.__developers = Developers()
   def develops(self):
       return self.__developers.develop()
project = Project()
print(project.develops())
```

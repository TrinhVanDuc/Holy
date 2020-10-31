* **Interface_seggregation principle**: Четвертый принцип соответствует букве I в SOLID, содержание этого принципа следующее: вместо использования большого интерфейса мы должны разделить на множество маленьких интерфейсов, для определенных целей Клиент не должен зависеть от интерфейса, который он не делает. использовать. Этот принцип относительно легко понять: вместо того, чтобы объединяться в большой интерфейс, мы можем разделить его на множество более мелких интерфейсов со связанными методами, чтобы им было легче управлять.
* **Примере**:
  * **Нарушение ISP**
```
class Shape:
   """A demo shape class"""
   def draw_circle(self):
       """Draw a circle"""
       raise NotImplemented
   def draw_square(self):
       """ Draw a square"""
       raise NotImplemented
class Circle(Shape):
    """A demo circle class"""
   def draw_circle(self):
       """Draw a circle"""
       pass
   def draw_square(self):
       """ Draw a square"""
       pass
 ```
*В приведенном выше примере нам нужно вызвать ненужный метод в классе Circle. Следовательно, в примере нарушен принцип разделения интерфейса.*
  * **Решение:**
```
class Shape:
   """A demo shape class"""
   def draw(self):
      """Draw a shape"""
      raise NotImplemented
class Circle(Shape):
   """A demo circle class"""
   def draw(self):
      """Draw a circle"""
      pass
class Square(Shape):
   """A demo square class"""
   def draw(self):
      """Draw a square"""
      pass
```

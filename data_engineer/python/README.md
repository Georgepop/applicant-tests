# Задания

## Python

Ниже даны 3 варианта заданий. Решить нужно какое-то одно.
Если успеваете в срок решить несколько — пожалуйста, такое будет плюсом :)

### 1 (парсинг, агрегация данных)

Необходимо:
1. Получить данные по комментариям и постам с ресурса http://jsonplaceholder.typicode.com/
    * http://jsonplaceholder.typicode.com/posts
    * http://jsonplaceholder.typicode.com/comments

2. Посчитать среднее количество комментариев к посту каждого
   пользователя, результатом должен быть словарь формата:
    * user_id
    * average_comments_per_post
   
3. Результат вывести в stdout (например `print`).


import requests
import pandas as pd

r = requests.get('http://jsonplaceholder.typicode.com/posts')
r = r.json()
r0= pd.DataFrame(r)

r = requests.get('http://jsonplaceholder.typicode.com/comments')
r = r.json()
r01= pd.DataFrame(r)

print(r01['postId'].value_counts())

У всех постов - 5 комментов, начит среднее к      пользователям - 5 

### 2 (качество кода, Dependency Injection, Dependency Inversion)

Код ниже работает без ошибок, но, возможно, требует определенного рефакторинга.
Внесите изменения в код так, чтобы добавлять новые **LampSwitcher'ы** было проще.

```python
from typing import Union


class LampSwitcher():

    def __init__(self, self.name = None):
        self.on_state = False
        self.name  = name

    def turn_on(self) -> None:
        print(f'{self.name} включена...')
        self.on_state = True

    def turn_off(self) -> None:
        print(f'{self.name} выключена...')
        self.on_state = False


 = LampSwitcher(name = )


class GlowLampSwitcher(LampSwitcher|('Лампа накаливания')):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ElectricLightSwitchManager:

    def __init__(
        self, switcher: Union[LampSwitcher],
    ) -> None:
        self.switcher = switcher

    def press(self) -> None:
        if isinstance(self.switcher, GlowLampSwitcher):
            if self.switcher.on_state:
                self.switcher.turn_off()
            else:
                self.switcher.on()
        elif isinstance(self.switcher, HalogenLampSwitcher):
            if self.switcher.on_state:
                self.switcher.off()
            else:
                self.switcher.turn_on()
        elif isinstance(self.switcher, AnotherLampSwitcher):
            if self.switcher.on_state:
                self.switcher.lamp_off()
            else:
                self.switcher.lamp_on()


def main() -> None:
    switch = ElectricLightSwitchManager(GlowLampSwitcher())
    switch.press()
    switch.press()
    switch = ElectricLightSwitchManager(HalogenLampSwitcher())
    switch.press()
    switch.press()
    switch = ElectricLightSwitchManager(AnotherLampSwitcher())
    switch.press()
    switch.press()


if __name__ == '__main__':
    main()

```

### 3 (качество кода, SOLID, принцип единой ответственности, Dependency Injection)

Выполните рефакторинг кода ниже.<br>
*Подсказка: руководствуйтесь принципом единой ответственности. Также можно применить Dependency Injection.*

```python
class Order:

   def __init__(self):
      self.items = []
      self.quantities = []
      self.prices = []
      self.status = 'open'

   def add_item(self, name, quantity, price):
      self.items.append(name)
      self.quantities.append(quantity)
      self.prices.append(price)

   def total_price(self):
      total = 0
      for i in range(len(self.prices)):
         total += self.quantities[i] * self.prices[i]
      return total


def main() -> None:
   order = Order()
   order.add_item('Keyboard', 1, 50)
   order.add_item('SSD', 1, 150)
   order.add_item('USB cable', 2, 5)
   print(order.total_price())
   order.pay('debit', '0372846')


if __name__ == "__main__":
   main()
```

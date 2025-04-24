# internet_store_app
Разработка интернет магазина в рамках домашних работ курса ООП

## Модуль base_classes

### Класс BaseProduct
Абстрактный класс BaseProduct, является родительским классом для класса Product. Создает шаблон для написания 
класса Product

## Модуль mixin_classes

### Класс MixingPrint
Родительский класс, который выводит основную информацию при создании объектов класса

## Модуль classes

### Класс Product
Атрибуты:

```python```
Copy:
`def __init__(self, name: str, description: str, price: float, quantity: int)`
Атрибут	    Тип	    Описание
name	    str	    Название товара
description	str	    Описание
price	    float	Цена
quantity	int	    Количество на складе

#### Подкласс Smartphone
Родительский класс Product
```python```
Copy:
`def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
              memory: int, color: str)`
Атрибут	    Тип	    Описание
name	    str	    Название товара
description	str	    Описание
price	    float	Цена
quantity	int	    Количество на складе
efficiency  float   Эффективность смартфона
model       str     Модель смартфона
memory      int     Объем памяти внутреннего накопителя
color       str     цвет смартфона


#### Подкласс LawnGrass
Родительский класс Product
```python```
Copy:
`def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
        color: str,)`
Атрибут	            Тип	    Описание
name	            str	    Название товара
description	        str	    Описание
price	            float	Цена
quantity	        int	    Количество на складе
country             str     Страна производства
germination_period  str     время прорастания
color               str     цвет травы



### Класс Category
Атрибуты:

```python```
Copy
`def __init__(self, name: str, description: str, products: List[Product])`
Атрибут	     Тип	        Описание
name	     str	        Название категории
description	 str	        Описание категории
products	 List[Product]	Список товаров


Статические атрибуты:

category_count: int - счетчик категорий

product_count: int - счетчик товаров

### Класс CatIter
Класс, позволяющий итерировать объекты списка продуктов класса Category

```python```
Copy
` def __init__(self, category: Category) -> None:`


## Модуль data_reader

### Функция read_json

Читает JSON-файл и возвращает список словарей.


## Модуль utils

### Функция create_objects
Создает объекты категорий и товаров из данных JSON-файла.
Читает файл из папки data/, преобразует данные в объекты Category и Product, и возвращает список готовых категорий
с товарами. По умолчанию использует файл products.json.
Читает JSON-файл и возвращает список словарей.


## Тестирование

Проект покрыт юнит-тестами pytest.

### Установка

Для установки фрэймворка pytest введите в терминале:
`poetry add --group tests pytest`
Для вывода отчета по тестированию установите библиотеку pytest-cov.
В терминале введите:
`poetry add --group tests pytest-cov`

### Запуск тестирования

Для запуска тестирования в терминале введите команду:
`pytest`
Для формирования HTML отчета о покрытии тестами в терминале введите команду:
`pytest --cov=src --cov-report=html`

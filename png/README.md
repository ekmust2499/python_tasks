# Разбор файла PNG

Автор: Мустафина Екатерина


## Описание
Данная программа является утилитой разбора графического файла формата PNG.


## Требования
* Модуль zlib
* Модуль PyQt5


## Состав
* Консольная версия: `png.py`
* Графическая версия: `png.graphic.py`
* Модули: `chunk_parser.py`, `filters.py`, `addition.py`
* Графические файлы: `Image\`
* Тестовые файлы: `tests\`

## Консольная версия
Справка по запуску: 
`png.py --help`, png.py help`

Пример запуска: 
`python png.py [image]
image - файл формата PNG

## Графическая версия
Справка по запуску: 
`png.graphic.py --help`, `png.graphic.py help` 

Пример запуска: 
`python png.graphic.py [image]
image - файл формата PNG

## Подробности реализации
В основе модуля `png.py` лежит класс PNG, который распаковывает данные из
файла формата PNG и с помощью модулей `chunk_parser.py` и `filters.py`
раскрывает информацию о каждом чанке файла, а так же вытаскивает список пикселей. 
Программа предусматривает визуализацию на основе списка пикселей, вытаскиваемых из
картинки формата PNG в модуле `png.py`. 
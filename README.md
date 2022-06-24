# Практическое занятие

В результате успешного выполнения практического задания студент будет уметь:

* устанавливать Mypy;
* запускать Mypy для анализа исходного текста программы;
* анализировать отчет Mypy;
* аннотировать код типами;

## Требования к программному обеспечению

* Операционная система: Windows, MacOS или Linux;
* Python 3.10 или старше
* Любой текстовый редактор


## Установите Mypy

Выполните в командной строке:

    pip install mypy

Сообщение об успешной установке должно содержать строку:

```
Successfully installed mypy-0.961
```

Можно выполнить проверку установки командой в консоли:

    mypy --version

Примерный ответ будет такой (версии интерпретатора и пакетов могут быть другими):

```
mypy 0.961 (compiled: yes)
```

## Аннотация типов в файле

Проставьте аннотации типов для файла `probability.py`:

* аргументы функций;
* возвращаемые значения функций;
* объявление локальных переменных.

```python
# Source: http://rosettacode.org/wiki/Dice_game_probabilities#Python
from itertools import product


def gen_dict(n_faces, n_dice):
    counts = [0] * ((n_faces + 1) * n_dice)
    for t in product(range(1, n_faces + 1), repeat=n_dice):
        counts[sum(t)] += 1
    return counts, n_faces ** n_dice


def beating_probability(n_sides1, n_dice1, n_sides2, n_dice2):
    c1, p1 = gen_dict(n_sides1, n_dice1)
    c2, p2 = gen_dict(n_sides2, n_dice2)
    p12 = float(p1 * p2)

    return sum(p[1] * q[1] / p12
               for p, q in product(enumerate(c1), enumerate(c2))
               if p[0] > q[0])


print(beating_probability(4, 9, 6, 6))
print(beating_probability(10, 5, 7, 6))
```

## Проверка корректности типов

Проверку корректности употребления типов следует делать с дополнительными ключами mypy:

    mypy probability.py --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs    

До начала добавления аннотаций сохрание отчет mypy в файл `mypy_report.txt`.

Проаннотируйте код типами, чтобы mypy не видел никаких проблем:

    Success: no issues found in 1 source file

## Отчет

Для отчета по практическому заданию необходимо:

1. Создать публичный репозиторий на GitHub на основе репозитория https://github.com/1irs/mypy-practice Можно воспользоваться страницей Generate: https://github.com/1irs/mypy-practice/generate для создания своего репозитория по шаблону.
2. В отдельном коммите проставить аннотации типов и добавить файл `mypy_report.txt`
3. Прислать ссылку на репозиторий на obrizan@1irs.net
# TODO Найдите количество книг, которое можно разместить на дискете
VOLUME = 1.44 * 1024 * 1024
PAGES = 100
STRINGS = 50
SYMBOLS = 25
CODE = 4

weight_of_1_book = PAGES * STRINGS * SYMBOLS * CODE

print("Количество книг, помещающихся на дискету:", int(VOLUME//weight_of_1_book))

# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44 * 1024 * 1024
book = 100 * 50 * 25 * 4
res = disk // book
print("Количество книг, помещающихся на дискету:", int(res))
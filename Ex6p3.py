m = int(input("Введите максимальную массу которую может выдержать лодка:"))
n = int(input("Введите количество рыбаков:"))
a = list(map(int, input("Введите вес путешественника:").split()))
a.sort()

i = 0
j = 0
boats = 0

while i < n:
    if a[i] + a[j] <= m and j < n:
        j += 1
    else:
        boats += 1
        j = 0
    i += 1

boats += 1
print("Количество лодок:", boats)

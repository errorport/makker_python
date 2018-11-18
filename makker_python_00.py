# Fibonacci számok generálása pythonnal
# Az alábbi példakód segítségével egy N elemű fibonacci számsort generálhaunk.

# 01 Az első példában csak egy for ciklus használatával tesszük ezt.
print("Példa 01.")
N=10
n_1 = n_2 = 1
for i in range(N):
	actual_number = n_1 + n_2
	n_1 = n_2
	n_2 = actual_number
	print(actual_number)
print("-- Futás vége.")

# 02 Amásodik példában a fenti kódot egy függvénybe ágyazva, a for ciklust megelőző beállításokat is elvégezzük, így egy program lefutása alatt az adott függvény tetszőleges számbna hívható.
print("Példa 02.")
def print_fibonacci(N):
	print("-- Függvényhívás: print_fibonacci(N)\nElemszám:",N)
	n_1 = n_2 = 1
	for i in range(N):
		actual_number = n_1 + n_2
		n_1 = n_2
		n_2 = actual_number
		print(actual_number)
	print("-- Futás vége.")
# itt történik a fenti függvény hívása.
print_fibonacci(5)
print_fibonacci(10)

# 03 A harmadik példában nem kiiratjuk az értékeket, hanem elmentjük egy vektorban
print("Példa 03.")
def get_fibonacci_temporary(N):
	print("-- Függvényhívás: get_fibonacci(N)\nElemszám:",N)
	vector = []
	n_1 = n_2 = 1
	for i in range(N):
		actual_number = n_1 + n_2
		n_1 = n_2
		n_2 = actual_number
		vector.append(actual_number)
	print("-- Futás vége.")
	return vector #visszaadjuk a számsort egy vektorban

# nincs kimenet, hiszen csak egy függvényt hoztunk létre, nem futtattuk le azt.

# 04 Egy kicsit csinosítva (refactor) a kódot, elhagyjuk az n_1 és n_2 változók használatát.
print("Példa 04.")
def get_fibonacci(N):
	print("-- Függvényhívás: get_fibonacci(N)\nElemszám:",N)
	vector = [1, 1]
	for i in range(N):
		actual_number = vector[i] + vector[i+1]
		vector.append(actual_number)
	print("-- Futás vége.")
	return vector #visszaadjuk a számsort egy vektorban
print(get_fibonacci(10))

# 05 Kiírjuk a generált számsor 5. és 8. elemét
print("* Figyeljük meg, hogy a kimeneten milyen sorrendben jelennek meg a szövegek! *")
print("Az 5. elem:", get_fibonacci(10)[4]) #0-tól indul a tömbök indexelése, így a 4. index az 5. elemet jelenti
print("Az 8. elem:", get_fibonacci(10)[7])

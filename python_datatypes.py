print("Вправва 1 конвертація чисел")
n = 42
print("десяткова :", n)
print("двійникова :", bin(n))
print("ішстнадцяткова :", hex(n))

print("Вправа 2 зворотнє перетворення")
a = 0b1101
b = 0o45
c = 0x1f
print("двійникове:", a)
print("вісімкове:", b)
print("шістнадцяткове:", c)

print("Вправа 3 ASCII коди символи")
print(ord('A'), ord('a'), ord('!') )

print( "Вправа 4 Адреса змінної" )
x = 10
print(("id до:"), id(x))
x = 20
print(("id після:"), id(x))

print(" Вправа 5 перевірка спільної памяті")
a = 5
b = a
print(id(a), id(b))

b = 6
print(id(a), id(b))

print(" Вправа 6 переприсвоєння обєкта")
name = "Boris"
print("id до:", id(name))

name = "Oleh"
print("id після:", id(name))

print("Вправа 7 що ствється зі старим обєктом")
x = 100
y = x
x = 200
print(x)

print("Вправа 8 повна практика")
x = 15
f = 2.5
text = "Hi"
print(type(x), "->", bin(x), hex(x))
print(type(f), "->", f)
print(type(text), "->", text)
print(" id до:", id(x))
x = 20
print(" id після:", id(x))



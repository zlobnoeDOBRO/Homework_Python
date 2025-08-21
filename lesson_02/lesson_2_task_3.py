def square(side):
    s = side * side
    return int(s) if s == int(s) else int(s) + 1


print("Площадь квадрата:", square(float(input("Введите сторону квадрата: "))))

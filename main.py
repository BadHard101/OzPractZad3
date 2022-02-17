#Задание №3
#Нахождение максимального числа подряд идущих возрастающих элементов в массиве

def Podryad(mas):
    podr = 1
    max_i=1
    for i in range(len(mas)-1):
        if (mas[i]<mas[i+1]):
            podr+=1
        else:
            if (max_i<podr):
                max_i=podr
            podr = 1
    return max_i


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input("Введите кол-во элементов массива (n): "))
    my_array = [0] * n
    for i in range(n):
        print(i, "й элемент:", sep='', end=" ")
        my_array[i] = int(input())

    print(Podryad(my_array))

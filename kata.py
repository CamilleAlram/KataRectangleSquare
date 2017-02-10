def sqInRect(square, lng, wdth):
    if lng == wdth and square == []:
        return square
    else:
        square.append(int(return_smaller(lng, wdth)))
        if lng * wdth - calcul_area(return_smaller(lng, wdth)) > 0:
            sqInRect(square, return_smaller(lng, wdth), calcul_wdth(lng, wdth))
        else:
            print(square)
            return square


def return_smaller(lng, wdth):
    if (lng < wdth):
        return lng
    else:
        return wdth


def calcul_area(lng):
    return lng * lng


def calcul_wdth(lng, wdth):
    areaRectangle = lng * wdth
    areaSquare = calcul_area(return_smaller(lng, wdth))
    wdth = (areaRectangle - areaSquare) / return_smaller(lng, wdth)
    return wdth


if __name__ == '__main__':
    square = []
    lng = 6
    wdth = 3
    sqInRect(square, lng, wdth)

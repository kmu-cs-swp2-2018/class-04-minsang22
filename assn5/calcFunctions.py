from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

romans = {
    1000 : "M", 900 : "CM", 500 : "D", 400 : "CD",
    100 : "C", 90 : "XC", 50 : "L", 40 : "XL",
    10 : "X", 9 : "IX", 5 : "V", 4 : "IV",
    1 : "I"
}
listromans = romans.items()


def decToRoman(numStr):
    try :
        result = ""
        an = int(numStr)
        if numStr == "":
            result = "입력값 없음!"
            return result
        if an >= 4000:
            result = "입력한 수가 4000 이상임!"
            return result
        for value in sorted(romans.keys(), reverse=True):
            while an >= value:
                result = result + romans[value]
                an = an - value
        return result
    except:
        an = "Error!"
        return an

def romanToDec(numStr):
    try:
        n = str(numStr)
    except:
        return 'Error!'

    roman = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL':40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
        'I': 1
    }

    result = 0
    while True:
        for i in roman.keys():
            if n.find(i) == 0:
                result += roman[i]
                if len(i) == 1:
                    n = n[1:]
                else:
                    n = n[2:]
        if n == '':
            break
    return str(result)





functionList = {
    'factorial (!)' : 'factorial()',
    '-> binary' : 'decToBin()',
    'binary -> dec' : 'binToDec()',
    '-> roman': 'decToRoman()',
    'roman -> dec' : 'romanToDec()'
}

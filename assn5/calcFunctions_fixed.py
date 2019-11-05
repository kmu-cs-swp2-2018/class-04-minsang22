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
    def dectoroman(a):
        try:
            result = ""
            an = str(a)
            int(an)  # 입력한 수가 소수인지 아닌지 판별
            an = int(a)
            if a == "":
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
        except ValueError:
            result = "입력한 수가 자연수가 아님"
            return result
        except:
            result = "Error1!"
            return result


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

    for i in romans.keys():
        if not i in n:
            result = "로마숫자 아닌 값이 있음"
            return result

    result = 0
    while True:
        for i in roman.keys():
            if n.find(i) == 0:
                #i의 위치값을 반환하는 find() 함수를 사용함!
                result += roman[i]
                if len(i) == 1:
                    n = n[1:]
                else:
                    n = n[2:]
        if n == '':
            break
            #무한loop에 빠지지 않도록 break문 사용!
    return str(result)





functionList = {
    'factorial (!)' : 'factorial()',
    '-> binary' : 'decToBin()',
    'binary -> dec' : 'binToDec()',
    '-> roman': 'decToRoman()',
    'roman -> dec' : 'romanToDec()'
}

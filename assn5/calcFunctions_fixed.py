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

    for i in roman.keys():
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
    
    '''
    조원의견 1 (앞에서 짠 함수를 이용 - 의존성 높음 ! )
    예를 들어 X가 4개 입력되고 이 버튼을 누를 시 40이라는 값이 리턴되기는 함.
    그러나 4의 올바른 로마자 표기법은 XL이므로
    최종값을 로마자로 변환하는 함수에 넣었을 때 XL가 리턴되어
    XXXX != XL가 되게 됨.
    그럴 경우 Error를 출력해줌 !
        
    if last != dectoRoman(total):
           return 'Error!'
    '''
    
    '''
    조원의견 2 (의존성을 줄이기 위해 앞에서 짠 함수 이용 x ! )
    def RomanToDec(numStr):
    try:
       # numStr.isalpha()  # 숫자로만 이뤄졌는지 확인하라

        romans = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
                 'I': 1,
                 }
        semi_result = []
        sorted(romans.items())

        half_num = ['M', 'C', 'X', 'I']
        for letters, value in romans.items():
            letters_cnt = 0  # 숫자의 중복도를 확인
            while len(numStr) != 0:  # 문자열의 길이가 없어기 전까지 반복
                if letters == numStr[0: len(letters)]:
                    numStr = numStr.replace(letters, '', 1)
                    letters_cnt += 1
                    semi_result.append(value)
                    if (letters not in half_num) and letters_cnt > 1:
                        return 'Error!'
                        # 1류를 제외하고 나머지는 'letters_cnt'가 2번 이상이면 안됨.
                    if letters_cnt > 3:  # 1류는 3번이상 반복되면 안됨
                        return 'Error!'
                else:
                    break
        if len(numStr) != 0:
            return 'Error!'
        result = sum(semi_result)
        return str(result)

    except:
        return 'Error!'
    
    '''




functionList = {
    'factorial (!)' : 'factorial()',
    '-> binary' : 'decToBin()',
    'binary -> dec' : 'binToDec()',
    '-> roman': 'decToRoman()',
    'roman -> dec' : 'romanToDec()'
}

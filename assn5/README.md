# ASSN5 보고서

### 1. 로마자 > 10진수 알고리즘

| def romanToDec(numStr): |                                              |
| ----------------------- | -------------------------------------------- |
|                         | try:                                         |
|                         | n = str(numStr)                              |
|                         | except:                                      |
|                         | return 'Error!'                              |
|                         |                                              |
|                         | roman = {                                    |
|                         | 'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,   |
|                         | 'C': 100, 'XC': 90, 'L': 50, 'XL':40,        |
|                         | 'X': 10, 'IX': 9, 'V': 5, 'IV': 4,           |
|                         | 'I': 1                                       |
|                         | }                                            |
|                         |                                              |
|                         | for i in roman.keys():                       |
|                         | if not i in n:                               |
|                         | result = "로마숫자 아닌 값이 있음"           |
|                         | return result                                |
|                         |                                              |
|                         | result = 0                                   |
|                         | while True:                                  |
|                         | for i in roman.keys():                       |
|                         | if n.find(i) == 0:                           |
|                         | #i의 위치값을 반환하는 find() 함수를 사용함! |
|                         | result += roman[i]                           |
|                         | if len(i) == 1:                              |
|                         | n = n[1:]                                    |
|                         | else:                                        |
|                         | n = n[2:]                                    |
|                         | if n == '':                                  |
|                         | break                                        |
|                         | #무한loop에 빠지지 않도록 break문 사용!      |
|                         | return str(result)                           |




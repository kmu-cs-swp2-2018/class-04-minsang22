# ASSN5 보고서

### 1. 로마자 > 10진수 알고리즘 ( romanToDec )

```python
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
```

 일단 로마자를 key로, 그에 해당하는 숫자를 value 값으로 가진 roman 딕셔너리의 키를 for문을 통해 받아온 후 i의 위치값을 반환하는 find() 함수를 사용하였다. find() 함수를 통해  찾아진 로마자의 값을 result 값에 더해준 후, 그 로마자를 슬라이싱 해서 잘라내준다.

그 후, 만약 더 이상 남은 로마자가 없으면 무한 loop에 빠지지 않도록 모든 로마자를 10진수로 바꿔주었을 때 beak문을 사용해  result 값을 리턴해주도록 하였다.



### 2.  오류 예외처리

#### 2-1. 10진수를 로마자로 바꾸는 함수의 예외처리 ( decToRoman )

##### 2-1-1. 소수가 입력되었을 때

```python
result = ""
n = str(numStr)
int(n)  # 입력한 수가 소수인지 아닌지 판별
n = int(numStr)
            
# 중간에 다른 코드들 또한 있음 
            
except ValueError:
result = "입력한 수가 자연수가 아님"
return result
```

로마자로 바꿀 수 있는 수는 1~3999 사이의 정수이다. 만약 계산기에 소수가 입력된 후 로마자로 바꾸는 함수를 실행하려 하면 오류가 뜰 것이기에, 이를 처리해 주는 코드를 추가했다. 계산기에서 받아온 스트링 형태의 n을 인트형으로 형변한을 시도해 봤는데,  만약 소수(float) 형태의 수를 받아왔다면 정수인 인트형으로 형변환 할때 ValueError가 발생하였다. 그래서 except 문으로 ValueError가 발생했을 때는 자연수가 아닌 값을 입력했다고 리턴해주도록 처리하였다.

##### 2-1-2. 입력값이 없을 때

```python
if n == "":
                result = "입력값 없음!"
                return result
```

만약 입력값이 없는 상태로 버튼을 눌렀다면, n의 값이 비어있는 "" 형태일 것이므로 입력값이 없다고 출력해주도록 하였다.

##### 2-1-3. 입력한 수가 4000 이상일 때

```python
if n >= 4000:
                result = "입력한 수가 4000 이상임!"
                return result
```

로마자는 1~3999 사이의 정수만을 표현할 수 있기 때문에, 계산기에서 받아온 값을 인트형으로 형변환 해준 값이 변수 n에 저장되어있기 때문에 n은 수 끼리의 크기 비교를 할 수 있다. 그러므로 n >= 4000일 시에 입력한 수가 4000 이상이라고 출력해주도록 처리하였다.



#### 2-2. 로마자를 10진수로 바꾸는 함수의 예외처리 (romanToDec)

##### 2-2-1. 로마자가 아닌 값이 있을 때

```python
for i in numStr:
   if not i in roman.keys():
    	result = "로마숫자 아닌 값이 있음"
        return result
```

roman이라는 딕셔너리에는 로마자가 key값에, 그에 해당하는 10진수 값이 value값에 저장되어 있다. for 반복문을 이용해 스트링형식인 numStr을 한글자씩 i에 넣어주고, 그 i 값중 roman의 key값에 없는 것이 있다면 로마자가 아닌 값이 있다고 출력해주도록 하였다.

##### 2-2-2. 로마자가 옳지 않은 표기법으로 되어 있을 때 (코드리뷰를 통해 배움 !)

처음 코드를 짜갔을 때, 로마자가 옳지 않은 표기법으로 되어있을 경우에 ( 예를 들어, 4를 IIII 같은 형식으로 표기했을 때) 예외 처리를 해주는 경우를 생각하지 않았었다. 하지만 이번 코드 리뷰를 통해, 조원들에게 이것 또한 예외 처리를 해주는 것이 좋겠다는 것을 배웠다.



```python
#조원의견 1 (유상록 조원) 
if last != dectoRoman(total):
        return 'Error!'
```

첫번째로 유상록 조원이 코드 리뷰해 준 방법은, 앞에서 짠 함수를 이용하는 방법이다. 예를 들어 X가 4개 입력되고 로마자를 함수로 변환하는 함수 실행 시 40이라는 값이 리턴되기는 한다. 그러나 4의 올바른 로마자 표기법은 XL이므로 최종값 (40) 을 로마자로 변환하는 함수에 넣었을 때 XL가 리턴되어 XXXX != XL가 된다. 그럴 경우 Error를 출력해 주도록 해서, 만약 옳지 않은 로마자 표기법을 입력할 경우를 에러 처리 해주었다. 이 코드도 정말 간단하고 좋은 방법이라고 생각했지만, 앞에서 짠 함수인 dectoRoman 을 이용해주는 방식이기 때문에 앞 함수에 오류가 있어 리턴해주는 값이 조금이라도 틀릴 시 결과에 차질이 발생하게 된다. 그러므로 이 코드는 의존성이 높은 코드라고 할수 있다.



```python
#조원의견 2 (조혜영 조원) (의존성을 줄이기 위해 앞에서 짠 함수 이용 x ! )
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
```

두 번째로 조혜영 조원이 코드 리뷰해주신 방법은, 첫 번째로 설명한 방법과 달리 앞에서 짠 함수를 이용하지 않는 방법이다.

    numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
    ]
    operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
    ]
    constantList = {
    "pi" : "3.141592",
    "빛의 이동 속도 (m/s)" : "3E+8",
    "소리의 이동 속도 (m/s)" : "340",
    "태양과의 평균 거리 (km)" : "1.5E+8",
    }
    functionList = {
    'factorial (!)' : calcFunctions.factorial,
    '-> binary' : calcFunctions.decToBin,
    'binary -> dec': calcFunctions.binToDec,
    '-> roman' : calcFunctions.decToRoman,
    }
  
  숫자와 기호 버튼들, 상수, 함수들을 구현하는데 있어 반복을 줄이기 위해 숫자와 기호 버튼은 리스트로, 상수와 함수는 딕셔너리로 구현해 주었다.
  그리고 calcFuntions를 import 해준 뒤 함수 딕셔너리의 밸류값에 넣어줘 키를 통해 찾을 경우엔 그 값이 함수를 통해 계산되도록 하되 계산하는 알고리즘은
  clacFunction.py 파일에 따로 짜 주었다.
  
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
    
  calFuntions.py 파일에선 계산 함수는 교수님께서 제시해 주신 그대로 사용하였고, 오류가 날 경우에 'Error!' 텍스트를 반환할 수 있도록
  except문을 추가해 주었다.
  
    elif key in constantList:
            if self.display.text().isdigit():
                self.display.setText(self.display.text() + "*" + constantList[key])
            else:
                self.display.setText(self.display.text() + constantList[key])
          
  그리고 메인 실행 코드인 mycalculator.py에는 다음과 같은 코드를 추가했다.(교수님께서 제시한 파일) 이 코드는 상수 버튼을 클릭하였을 때, 만약 디스플레이 text에
  미리 작성되어있는 수가 있다면 그 수 뒤에 * 기호와 상수를 입력해주고, 그렇지 않다면 상수만을 입력해 줄 수 있도록 isdigit 함수를 이용해
  텍스트에 숫자가 입력되어 있는지 아닌지 판별해 주는 코드이다.

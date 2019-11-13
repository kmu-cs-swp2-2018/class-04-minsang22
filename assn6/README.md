## 20191631 윤민상 소프트웨어 프로젝트 ASSN6 보고서

### 1. Guess 함수의 알고리즘 (단어 맞추기)

```python
def guess(self, character):
        self.guessedChars.append(character) 
        TorF = False
        if character in self.guessedChars: 
            for i in range(len(self.secretWord)):
                if character== self.secretWord[i]:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
                    TorF = True
        else:
            return False
        if not TorF:
            self.numTries += 1
        if self.secretWord == self.currentStatus: 
            return True
```

일단 현재 단어를 다 맞췄다면 True, 아니라면 False로 저장되어 있을 변수인 TorF를 만들어 False를 저장해둔다. 그 후, for문을 통해 플레이어가 입력해 준 스펠링이 저장되어 있는 인덱스 값을 찾고, 인덱스 슬라이싱을 이용해 그 인덱스 값에 '_'  대신 입력받은 스펠링을 넣어준다. 만약 입력해 준 스펠링이 지정된 단어에 없다면 False를 리턴해 준다. 이 과정을 마친 후 TorF의 값이 False라면 스펠링을 맞추지 못한 것이므로 시도 횟수를 1회 증가시켜주고, 최종적으로 모든 단어를 완성시켰을 경우 True를 리턴해준다.

### 2. 코드리뷰 하면서 비교했던 점

조원분들 중 한분이 find() 함수를 이용해 코드를 짰는데, 정상적으로 작동이 되지 않는다고 말씀해 주셨다. 그래서 코드리뷰를 하며 왜 그렇게 되는지 말해 보았는데, find() 함수는 하나의 스펠링의 인덱스 값만 찾아주기 때문에, 같은 스펠링이 단어에 여러 개가 들어있는 경우 뒤에 있는 스펠링들은 한번에 찾아내지 못해 정상 작동이 되지 않는다는 이유를 알게되었다. 처음엔 나도 인덱스 값을 찾아낼 때 find() 함수를 쓰려 하다가 for 반복문을 이용했는데, find() 함수에 이런 단점이 있을 줄은 생각하지 못했다. 코드 리뷰를 하며 평소 사용하던 함수에 대한 새로운 것을 배워서 좋았다.


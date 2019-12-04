## 20191631 윤민상 소프트웨어 프로젝트 2 ASSN8 보고서



### 1. GUI의 구현 (guessClicked 메소드의 구현)

```python
def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if self.gameOver == True:
            return self.message.setText()
            # 메시지 출력하고 - message.setText() - 리턴

        if len(self.charInput.text()) > 1:
            return self.message.setText("Not one char!")  # 입력의 길이가 1 인지를 판단하고, 아닌 경우 메시지 출력, 리턴

        if self.charInput.text() in guessedChar:
            return self.message.setText("Used char!")
        # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴

        success = self.guess.guess(guessedChar)
        if success == False:
            self.hangman.remainingLives -= 1
            # 남아 있는 목숨을 1 만큼 감소
            self.message.setText("Wrong char")
            # 메시지 출력

        self.hangmanWindow.setText(self.hangman.currentShape())
        # hangmanWindow 에 현재 hangman 상태 그림을 출력
        self.currentWord.setText(self.guess.currentStatus)
        # currentWord 에 현재까지 부분적으로 맞추어진 단어 상태를 출력
        self.guessedChars.setText(guessedChar)
        # guessedChars 에 지금까지 이용한 글자들의 집합을 출력

        if self.guess.finished():
            self.message.setText("Success!")
            self.gameOver = True
            # 메시지 ("Success!") 출력하고, self.gameOver는 True로

        elif self.hangman.getRemainingLives() == 0:
            self.message.setText("Fail!" + " " + self.guess.secretWord)
            self.gameOver = True
            # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver는 True로
```

Pseudo code에 작성되어 있는 내용을 기반으로 코드를 작성하였다. Pseudo code에 작성되어 있는 대로 return 값과 출력 값만 코드를 작성해 주면 되었기에 코드를 짜기 굉장히 편했다. 깃허브에 commit했던 코드에선 이상하게 사용했던 char를 또 다시 사용해도 에러가 뜨지 않고 진행되어서 이 오류를 고치기 위해 코드를 검토했지만, 문제가 있는 부분이 보이지 않아 고치기 힘들었다. 그런데 코드리뷰 시간 때 이 오류를 말해보니 조원분들이 if not self. charInput. text() in guessedChar 코드 부분에 not이 빠져야 한다고 내 실수를 찾아내주셨고, 위처럼 not을 삭제하니 사용했던 char를 다시 사용했을 때 정상적으로 "Wrong char" 라는 문자열을 출력해 주었다.

### 2. 기능의 확장 ( 최소 단어 길이 제한)

```python
        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            if len(word) > self.maxLength:
                self.maxLength = len(word)
            self.count += 1

        print('%d words in DB' % self.count)

    def randFromDB(self, minLength):
        
        if minLength > self.maxLength:
            minLength = self.maxLength

        while True:
            r = random.randrange(self.count)
            if len(self.words[r]) < minLength:
                continue
            else:
                return self.words[r]

```

접근법 2를 이용해 최소 단어의 길이를 제한해주었다. randFromDB 메소드를 호출할 때 단어의 최소 길이 minLength를 입력해주고, 랜덤으로 나온 수인 r을 인덱스로 가지는 word의 길이가 입력해 준 minLentgh 보다 작을경우 계속 다시 랜덤으로 r을 구해주고 그 수를 인덱스로 가지는 word를 찾아준다. 만약 r을 인덱스로 가진 word의 길이가 minLength보다 클 경우 그 word를 리턴해준다. 그러나, 이 접근법을 사용할 경우 만약 minLength가 데이터베이스에 있는 모든 단어들의 길이보다 큰 숫자인 경우 무한 loop에 빠질 수 있다는 문제가 있다. 그런 일을 방지하기 위해 코드를 추가해 주었는데, 일단 for 반복문을 통해 데이터베이스에 있는 word들 중 가장 긴 단어의 길이를 self.maxLength에 저장해준다. 그리고 randFromDB 메소드를 호출할 때 입력해준 minLength가 만약 self.maxLength보다 클 경우 minLength를 self.maxLength로 설정해주었다. 교수님께서 수업시간에 lambda 함수를 사용하여 한줄만에 self.maxLength를 구할 수 있는 방법도 설명해 주셨는데, 그 또한 굉장히 코드를 간단하게 만들 수 있기 때문에 좋은 방법이라고 생각한다.

### 3. 버그의 제거 ( 너무 긴 단어 선택시 전체가 보이지 않음)

```python
 # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)

        # 글자길이 디버깅해결하는 방법 비밀단어보다 길이를 2배로 늘린상태의 qlineedi사이즈를 어떤단어가 들어와도 그것의 2배 길이니까 버그가 안생기게 유동적으로 사이즈를 변경하
        self.currentWord.setMaxLength(len(self.secretWord) * 2)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)
```

QLineEdit이 가지고 있는 여러 메소드를 구글링해 보았지만 너무 긴 단어 선택시 전체가 보이지 않는 버그를 고치기 위한 메소드를 잘 찾지 못하였다. 그래서 코드리뷰 시간 때 다같이 이에 대해 이야기를 해 보았는데, 그 결과 우리 조는 QLineEdit 메소드가 가지고 있는 메소드를 사용하지 않고 그 대신 QLineEdit의 사이즈를 변경해주는 방법이 좋겠다는 결론을 내렸다. secretWord로 골라진 단어의 길이에 2배를 곱해주어서 어떤 단어가 골라져도 유동적으로 그것의 2배 길이로 QLineEdit의 사이즈가 설정되어 단어 전체가 보이지 않는 에러가 발생하지 않도록 하였다.

### 4. 코드리뷰 & 과제를 하며 느낀점

Pseudo code를 기반으로 코드를 짜니 정말 편했던 것 같다. 구현해야 할 사항을 미리 주석으로 표현해 놓으니 그에 대한 생각만 하며 코드를 짤 수 있어 작업의 처리 속도와 효율 모두 상승한 것 같아 좋았다. AD 프로젝트에서 긴 코드를 작성할 때 혹은 다음에 코드를 짤 때는 미리  Pseudo code를 작성해 둔 후 코드를 구현하는 방법을 이용해 좀 더 쉽게 코딩을 해야겠다고 생각했다. 이번 코드리뷰 시간에도 새로운 방법을 많이 배웠고, 내가 실수했지만 찾지 못했던 부분을 조원들이 찾아주며 부족한 부분에 대한 지적도 받았기 때문에 한단계 더 배우고 발전할 수 있는 값진 코드리뷰 시간이었다고 생각한다.

### 5. 한 학기의 마지막 보고서를 작성하며...

처음엔 코드리뷰와 보고서를 작성하는 활동이 너무 낯설기도 하고, 조원들과도 어색해 코드리뷰와 보고서 활동이 어렵게 느껴지기도 했습니다. 하지만 시간이 지나가며 조원들과도 친해져 서로 어렵지 않게 코드에 대한 지적과 부족한 점도 말해줄 수 있게 되었고, 수업시간이 아니더라도 과제에 어려움을 겪으면 서로 물어보며 조원들에게 많은 것을 배웠던 것 같습니다. 또, 항상 코드리뷰가 끝난 후 보고서를 작성하며 코드리뷰 시간에 배우거나 알게된 내용을 되돌아볼 수 있었고, 복습도 하며 많은 것을 얻어간 것 같습니다. 2학기가 처음 시작해 학생들의 DB를 관리하는 코드를 짜는 과제를 할 때만 해도 200줄 가까이 되는 코드를 작성하는 것이 처음이라 많은 어려움을 겪었지만, 지금은 나름 익숙해 져 있는 모습을 보며 "소프트웨어 프로젝트 2" 라는 수업을 수강함에 있어 많은 것을 배웠다는 것을 느낍니다. 아직 기말 평가도 남았고, 학기 중에는 항상 과제에 쩔쩔매며 힘들어하고 피곤해 했지만 마지막 과제를 제출하는 지금에서 돌아보면 이번 학기 가장 보람찼던 수업 같습니다. 과제를 성공했을 때는 정말로 기뻤고, 저에게 소프트웨어 학부라는 전공에 대해 좀 더 흥미를 가지게 해준 수업이라고도 생각합니다. 1학기 "소프트웨어 프로젝트 1" 수업에 이어 2학기 이번 수업 또한 교수님께 수업을 들을 수 있어 참 좋았습니다. 항상 질문과 메일도 잘 받아주시고 질 높은 수업을 제공해 주셔서 감사하다고 말씀드리고 싶습니다. 감사합니다 교수님.

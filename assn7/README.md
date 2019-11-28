## 20191631 윤민상 소프트웨어 프로젝트 2 ASSN7 보고서

##### - 보편적인 형태의 단어를 넣어보기 위해 테스트 케이스는 'abcedbcda' 로 하였다.

### 1.  Guess의 단위 테스트 (TestGuess.py)

##### 1-1. testDisplayCurrent

```python
    def testDisplayCurrent(self):
        self.p1.guess('e')
        self.assertEqual(self.p1.displayCurrent(), '_ _ _ _ e _ _ _ _ ')
        self.p1.guess('a')
        self.assertEqual(self.p1.displayCurrent(), 'a _ _ _ e _ _ _ a ')
        self.p1.guess('t')
        self.assertEqual(self.p1.displayCurrent(), 'a _ _ _ e _ _ _ a ')
        self.p1.guess('a') 
        self.assertEqual(self.p1.displayCurrent(), 'a _ _ _ e _ _ _ a ')
```

DisplayCurrent 함수는 현재까지 단어를 어디까지 맞췄는지 진행 사항을 표시해주는 함수이다. 처음엔 하나만 들어가 있는 스펠링을 입력했을 경우를 테스트 해주기 위해 e를 입력했고, 두번째로는 두개 이상 들어가있는 스펠링을 입력했을 경우를 테스트 해주기 위해 a를 입력했다. 세번째로는 단어에 들어가있지 않은 스펠링을 입력했을 경우를 테스트 해주기 위해 t를, 마지막으로는 이미 입력했던 스펠링을 다시 입력했을 경우를 테스트 해주기 위해 a를 다시 입력해 보았다.

##### 1-2. testDisplayGuessed

```python
    def testDisplayGuessed(self):
        self.p1.guess('e')
        self.p1.guess('n')
        self.assertEqual(self.p1.displayGuessed(), 'e n ')
        self.p1.guess('a')
        self.assertEqual(self.p1.displayGuessed(), 'a e n ')
        self.p1.guess('t')
        self.assertEqual(self.p1.displayGuessed(), 'a e n t ')
        self.p1.guess('u')
        self.assertEqual(self.p1.displayGuessed(), 'a e n t u ')
        self.p1.guess('c')
        self.assertEqual(self.p1.displayGuessed(), 'a c e n t u ')
```

DisplayGuessed 함수는 지금까지 입력한 스펠링을 표시해주는 함수이다. 처음에 e와 n을 입력해 준 후 테스트 해주었고, 그 다음엔 단어에 들어있는 스펠링과 들어있지 않은 스펠링들을 넣어주며 테스트 해 보았다.

##### 1-3. testGuess

```python
    def testGuess(self):
        self.assertEqual(self.p1.guess('e'), True)
        self.assertEqual(self.p1.currentStatus, '____e____')
        self.assertEqual(self.p1.guessedChars, ['e'])
        self.assertEqual(self.p1.guess('a'), True)
        self.assertEqual(self.p1.currentStatus, 'a___e___a')
        self.assertEqual(self.p1.guessedChars, ['e', 'a'])
        self.assertEqual(self.p1.guess('d'), True)
        self.assertEqual(self.p1.currentStatus, 'a__ded__a')
        self.assertEqual(self.p1.guessedChars, ['e', 'a', 'd'])
        self.assertEqual(self.p1.guess('u'), False)
        self.assertEqual(self.p1.currentStatus, 'a__ded__a')
        self.assertEqual(self.p1.guessedChars, ['e', 'a', 'd', 'u'])
```

testGuess에서 테스트해준 guess 함수는 입력한 스펠링이 단어에 들어있는지 아닌지를 True or False를 통해 리턴해주고, currentStatus는 현재 맞춘 단어의 상태를, guessedChars는 입력해 본 스펠링들을 리스트 형태로 리턴해준다. 단어에 들어가는 스펠링인 e, a, d를 테스트 해 준 후 단어에 들어가지 않는 스펠링인 u를 테스트 해주었다.

 ##### 1-4. testFinished

```python
    def testFinished(self): 
        self.p1.guess('a')
        self.p1.guess('b')
        self.p1.guess('c')
        self.p1.guess('d')
        self.p1.guess('e')
        self.p1.guess('d')
        self.p1.guess('c')
        self.p1.guess('b')
        self.p1.guess('a')
        self.assertTrue(self.p1.finished())
```

새로 추가해준 testFinshed 함수는 만약 단어를 다 맞추었다면 true를 리턴해주는 함수이다. 중복을 포함해 단어의 모든 스펠링을 입력해준 후 testFinshed 함수가 제대로 True를 리턴해 주는지 테스트 해 보았다.



### 2. Word의 단위 테스트 (TestWord.py)

```python
class TestWord(unittest.TestCase):
    def setUp(self):
        self.w1 = Word('words.txt')
    def tearDown(self):
        pass
    def testInput(self):
        self.assertEqual(self.w1.words, ['aback', 'abacus', ...이하 생						략...])
```

Word 클래스에서 테스트 해줄 것은 제대로 텍스트 파일을 리스트로 받아올 수 있는지 밖에 없다고 생각되어 그것을 테스트 해 주었다.



### 3. Hangman의 단위 테스트 (TestHangman.py)

##### 3-1. testDecreaseLife

```python
    def testDecreaseLife(self):
        self.assertEqual(self.h1.remainingLives, 6)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 5)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 4)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 3)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 2)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 1)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 0)
```

이번에 새로 추가해준 DecreaseLife 함수는 함수를 호출할 경우 남은 목숨이 1씩 줄어들게 해주는 함수이다. 이를 이용해 한번 함수를 호출할 때 마다 올바르게 목숨이 1씩 줄어드는지 테스트 해 주었다.

##### 3-2. testcurrentShape

```python
    def testcurrentShape(self):
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')
```

currentShape 함수는 현재 남은 목숨에 따른 행맨의 모습을 보여주는 함수이다. decreaseLife 함수를 호출할 때 마다 올바르게 목숨이 1씩 줄어들며 그에 따라 행맨의 모습이 올바르게 바뀌는지 테스트 해 주었다.



### 4. 코드리뷰와 수업을 통해

내가 이번 단위 테스트를 하며 

class Guess:

    def __init__(self, word):
        self.secretWord = word #무작위단어를 생성한다
        self.currentStatus = "_" * len(word) #무작위 단어의 길이만큼 언더바를 생성한다
        self.numTries = 0 #시도횟수를 0으로 초기화하여 생성한다
        self.guessedChars = [] #사용했던 단어를 넣어놓는 리스트

    def display(self):
        print("Current: ",self.currentStatus) #현재상태
        print("Tries: ", self.numTries) #시도횟수

    def guess(self, character):
        self.guessedChars.append(character) #guessedChars에 사용한 단어를 넣는다
        TorF = False
        if character in self.guessedChars: #guessedChars에 character가 없다면 포문을 실행한다
            for i in range(len(self.secretWord)):
                if character== self.secretWord[i]:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:] #알맞은 자리에 character를 넣는다
                    TorF = True
        else:
            return False
        if not TorF: #TorF가 True로 바뀌지 않는다면 시도횟수를 증가시킨다
            self.numTries += 1
        if self.secretWord == self.currentStatus: #현재상태와 비밀단어가 같다면 True를 리턴한다
            return True
import unittest

from guess import Guess

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.p1 = Guess('abcdedcba')

    def tearDown(self):
        pass
# test cases
    def testDisplayCurrent(self):
        self.p1.guess('e')
        self.assertEqual(self.p1.displayCurrent(), '_ _ _ _ e _ _ _ _ ')
        self.p1.guess('a')
        self.assertEqual(self.p1.displayCurrent(), 'a _ _ _ e _ _ _ a ')
        self.p1.guess('t')
        self.assertEqual(self.p1.displayCurrent(), 'a _ _ _ e _ _ _ a ')
        self.p1.guess('a')  # 이미 시도한 문자 입력시
        self.assertEqual(self.p1.displayCurrent(), 'a _ _ _ e _ _ _ a ')

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
        self.p1.guess('c') #틀린 소문자
        self.assertEqual(self.p1.displayGuessed(), 'a c e n t u ')


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

    def testFinished(self):  # 단어의 전체를 다 맞춘경우 True를 반환하는지 테스트
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
if __name__ == '__main__':
    unittest.main()
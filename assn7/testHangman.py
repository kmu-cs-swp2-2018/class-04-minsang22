import unittest

from hangman import Hangman

class TestHangman(unittest.TestCase):
    def setUp(self):
        self.h1 = Hangman()
    def tearDown(self):
        pass
# test cases
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

    def testcurrentShape(self): #Life가 줄어들때 그림도 그에 맞게 출력 되는지 확인
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
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |    |
  |    |
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
  |   /|
  |    |
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
  |   /|\\
  |    |
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
  |   /|\\
  |    |
  |   /
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
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''')
if __name__ == '__main__':
    unittest.main()
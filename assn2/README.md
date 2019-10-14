UI의 구성은 PDF를 보며 작성했는데, 코드 리뷰를 해 본 결과 거의 모든 조원분들과 비슷한 형식으로 짜여 있었고 에러 없이 잘 작동되었다.

    def readScoreDB( self ) :
        try :
            fH = open( self.dbfilename, 'rb' )
        except FileNotFoundError as e :
            self.scoredb = [ ]
            return
        try :
            self.scoredb = pickle.load( fH )
        except :
            pass
        fH.close( )
        
 readScoreDB 함수는 예외 처리를 해주면서 교수님께서 수업해 주신대로 코드를 짰다. 원래 except문 밑에 else : pass 코드가 있었는데, 코드 리뷰를 하면서 조원분들이 없어도 작동되는 else : pass 같은 코드는 읽기 편하게 하다보니 습관적으로 추가해 준 코드라 말해주시면서 없어도 정상적으로 작동이 되니 빼는게 맞는 코드라 조언해주셔서 코드를 제거했다.
 
그리고 정상적으로 GUI 프로그램이 작동은 되었지만 계속 

    QLayout::addChildLayout: layout "" already has a parent
    
라는 오류가 떴다. 조별 코드 리뷰를 하면서도 오류를 수정하지 못했고, 수업 이후 구글 검색을 통해 오류의 원인을 알아보았는데 이미 레이아웃에 부모 클래스가 있지만 다른 부모 클래스에 자식 클래스로 추가하려 하니 발생하는 오류라 했다. 

    h = QHBoxLayout( )
        Amount = QLabel( "Amount : " )
        self.Line4 = QLineEdit( )
        Key = QLabel( "Key : " )
        h.addWidget( Amount )
        h.addWidget( self.Line4 )
        h.addWidget( Key )
        h.addWidget( self.Box )
        v.addLayout( h )
        v.addStretch( 1 )
        h = QHBoxLayout( )
        h.addStretch( 1 )
        h.addStretch( 2 )

수업 이후로 조별 분들께 상의를 해서 add 레이아웃을 위처럼 수정했더니 정상 작동되는것을 확인했다.

또, 교수님께서 코드 리뷰 수업을 진행하면서 변수명을 "AbcDef" 식으로 지정하는 것보다 파이썬에선 "abc_def" 형식으로 지정해 주는 것이 더 공식적인 방법이라 말씀해 주셨다. 그래도 변수명이 둘 중 한 방식으로 통일되어있다면 괜찮다고 말씀해주셔서 앞의 방식으로 이미 변수명을 지정해놨기에 통일해주었지만, 다음 부턴 코드를 짤 때 두번째 방식을 이용하도록 노력해야겠다고 생각했다.

마지막으로, 다른 조의 발표를 들으며 교수님께서 함수 하나에서 텍스트를 받아와 거기에 그 함수 텍스트가 add 등 무엇인지에 따라 기능이 작동되도록 코드를 짜는 방식도 언급해주셨다. 내가 짠 코드처럼 버튼 하나당 def로 하나씩 기능을 만들어 코드를 짜는 방식도 있었지만, 첫번째 방식도 코드를 보기 깔끔하게 짜는 데에는 좋은 방법이라 생각되었고 코드를 짜는데는 여러 방법이 있겠다는 생각을 다시 한번 해보게 되었다.

이렇게 긴 코드를 직접 짜 본적이 처음이었기 때문에 오류가 나더라도 DB가 정상적으로 작동될 때 굉장히 뿌듯함을 느꼈다. 긴 코드더라도 부분부분 쪼개서 코드를 짠다면 어렵더라도 한 층 수월하게 코드를 짤 수 있다는 것도 느끼게 되어 앞으로도 열심히 코드를 짜도록 노력해야겠다는 생각이 들었다. 

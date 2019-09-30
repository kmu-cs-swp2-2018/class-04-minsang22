import pickle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ScoreDB( QWidget ) :
    def __init__( self ) :
        super( ).__init__( )
        self.initUI( )
        self.dbfilename = 'assignment6.dat'
        self.scoredb = [ ]
        self.readScoreDB( )
        self.showScoreDB( )



    def initUI( self ) :
        self.setGeometry( 300, 300, 500, 250 )
        self.setWindowTitle( 'Assignment6' )
        self.Box = QComboBox( )
        self.Box.addItems( [ 'Name', 'Age', 'Score' ] )
        Add = QPushButton( 'Add', self )
        Del = QPushButton( 'Del', self )
        Find = QPushButton( 'Find', self )
        Inc = QPushButton( 'Inc', self )
        Show = QPushButton( 'Show', self )

        Name = QLabel( "Name : " )
        self.Line1 = QLineEdit( )
        Age = QLabel( "Age : " )
        self.Line2 = QLineEdit( )
        Score = QLabel( "Score : " )
        self.Line3 = QLineEdit( )

        h = QHBoxLayout( )
        h.addWidget( Name )
        h.addWidget( self.Line1 )
        h.addWidget( Age )
        h.addWidget( self.Line2 )
        h.addWidget( Score )
        h.addWidget( self.Line3 )
        v = QVBoxLayout( )
        v.addLayout( h )
        v.addStretch( 1 )

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


        lbls = QLabel( " Result : " )
        h.addWidget( Add )
        h.addWidget( Del )
        h.addWidget( Find )
        h.addWidget( Inc )
        h.addWidget( Show )
        v.addLayout( h )
        v.addStretch( 1 )
        h.addWidget( lbls )
        v.addLayout( h )
        v.addStretch( 1 )

        h = QHBoxLayout( )
        self.text = QTextEdit( self )
        h.addWidget( self.text )
        v.addLayout( h )

        self.Box = QComboBox( )
        self.Box.addItems( [ 'Name', 'Age', 'Score' ] )
        Add.clicked.connect( self.Add_buttonClicked )
        Del.clicked.connect( self.Del_buttonClicked )
        Find.clicked.connect( self.Find_buttonClicked )
        Inc.clicked.connect( self.Inc_buttonClicked )
        Show.clicked.connect( self.showScoreDB )
        self.setLayout( v )
        self.show( )

    def closeEvent( self, event ) :
        self.writeScoreDB( )

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
        else :
            pass
        fH.close( )

    def writeScoreDB( self ) :
        fH = open( self.dbfilename, 'wb' )
        pickle.dump( self.scoredb, fH )
        fH.close( )

    def showScoreDB( self ) :
        self.text.clear( )
        self.DB = ""
        key = str( self.Box.currentText( ) )
        for p in sorted( self.scoredb, key=lambda person : person[key] ):
            for attr in sorted( p ) :
                self.DB += attr + "=" + str(p[attr]) + "\t"
                if attr == "Score" :
                    self.text.append( ( self.DB ) )
            self.DB += "\n"
        self.text.setText( self.DB )




    def Add_buttonClicked( self ) :
        try :
            name_Line = self.Line1.text( )
            age_Line = self.Line2.text( )
            score_Line = self.Line3.text( )
            if name_Line == '' :
                self.text.setText( "no name" )
            elif int(age_Line) > 0 and int(score_Line) >= 0 :
                remem = {'Name' : name_Line, 'Age' : int( age_Line ), 'Score' : int( score_Line ) }
                self.scoredb += [remem]
                self.showScoreDB( )
            else :
                self.text.setText( "양의 정수 입력" )
        except ValueError :
            self.text.setText( "error" )

    def Del_buttonClicked( self ) :
        try :
            name_Line = self.Line1.text( )
            if name_Line == '' :
                self.text.setText( "no name" )
            else :
                for i in range( len(self.scoredb) // 2 + 1 ) :
                    for p in self.scoredb :
                        while p['Name'] == name_Line :
                            if p['Name'] == name_Line :
                                self.scoredb.remove( p )
                                break
                self.showScoreDB( )
        except :
            pass

    def Find_buttonClicked( self ) :
        self.text.clear( )
        name_Line = self.Line1.text( )
        if name_Line == '' :
            self.text.setText( "no name" )
        else :
            for p in self.scoredb :
                if p['Name'] == name_Line :
                    Result = ''
                    for attr in sorted(p) :
                        Result += str(attr) + "=" + str(p[attr]) + " "
                        if attr == "Score" :
                            self.text.append((Result))

    def Inc_buttonClicked( self ) :
        try :
            name_Line = str( self.Line1.text( ) )
            amount_Line = int( self.Line4.text( ) )
        except ValueError :
            self.text.setText( "Error" )
        else :
            if name_Line == '' :
                self.text.setText( "no name" )
            else :
                for p in self.scoredb :
                    if p["Name"] == name_Line :
                        if p["Score"] + amount_Line < 0 :
                            self.text.setText( "양의 정수 입력" )
                        else :
                            p[ "Score" ] = int(int ( p [ "Score" ] ) + int( amount_Line ) )
                self.showScoreDB( )

if __name__ == '__main__' :
    app = QApplication( sys.argv )
    ex = ScoreDB( )
    sys.exit( app.exec_( ) )
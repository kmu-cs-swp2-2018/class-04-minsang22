        def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)

            except ZeroDivisionError:
                self.display.setText("0으로는 나눌 수 없습니다!")

            except SyntaxError:
                self.display.setText("수식이 올바르지 않습니다!")
                
        elif key == 'C':
            self.display.setText("")
            
        else:
            self.display.setText(self.display.text() + key)
            

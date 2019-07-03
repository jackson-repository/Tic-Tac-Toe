from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QVBoxLayout, QLabel, QMessageBox
from sys import argv, exit

class TicTacToe(QWidget):
    CurrentPlayer = 'X'
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        mainGrid = QVBoxLayout()
        self.setLayout(mainGrid)
        GridLayout = QGridLayout() # Makes buttons layout
        mainGrid.addLayout(GridLayout)
        self.message = QLabel("Current Player:" + TicTacToe.CurrentPlayer)
        mainGrid.addWidget(self.message)

        buttonNames = [i for i in range(1, 10)]
        self.buttons = {}
        for position, name in zip([(i, j) for i in range(3) for j in range(3)], buttonNames):
            self.buttons[name] = QPushButton()
            self.buttons[name].clicked.connect(self.Move)
            GridLayout.addWidget(self.buttons[name], *position) # adding button to layout
        
        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle("Tic Tac Toe")
        self.show()
    
    def Move(self):
        if self.sender().text() == '': # Checks if the pushed button is not taken
            self.sender().setText(TicTacToe.CurrentPlayer)
            self.Check_Winner()
            self.ChangeCurrent()
            self.message.setText("Current Player:" + TicTacToe.CurrentPlayer)
        else:
            self.message.setText("This is Taken")

        if self.fullBoard(): # Checks if there is free (not taken) buttons to continue the game
            Message = QMessageBox.question(self, "Draw!!", "Do You Want To Play Again?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if Message == QMessageBox.No:
                exit()
            else:
                self.Restart()
            self.ChangeCurrent()
            self.message.setText("Current Player:" + TicTacToe.CurrentPlayer)

    
    def fullBoard(self):
        # if all buttons are taken then it returns True , otherwise it returns False
        for i in range(1, 10):
            if self.buttons[i].text() == '': return False
        return True
    
    def Check_Winner(self):
        # if someone won the game, it executes self.Won() method
        if self.buttons[1].text() == self.buttons[2].text() == self.buttons[3].text() and self.buttons[1].text() != '':
            self.message.setText("Winner" + self.buttons[1].text())
            self.Won()
        elif self.buttons[4].text() == self.buttons[5].text() == self.buttons[6].text() and self.buttons[4].text() != '':
            self.message.setText("Winner" + self.buttons[4].text())
            self.Won()
        elif self.buttons[7].text() == self.buttons[8].text() == self.buttons[9].text() and self.buttons[7].text() != '':
            self.message.setText("Winner" + self.buttons[7].text())
            self.Won()
        elif self.buttons[1].text() == self.buttons[4].text() == self.buttons[7].text() and self.buttons[1].text() != '':
            self.message.setText("Winner" + self.buttons[1].text())
            self.Won()
        elif self.buttons[2].text() == self.buttons[5].text() == self.buttons[8].text() and self.buttons[2].text() != '':
            self.message.setText("Winner" + self.buttons[2].text())
            self.Won()
        elif self.buttons[3].text() == self.buttons[6].text() == self.buttons[9].text() and self.buttons[3].text() != '':
            self.message.setText("Winner" + self.buttons[3].text())
            self.Won()
        elif self.buttons[1].text() == self.buttons[5].text() == self.buttons[9].text() and self.buttons[1].text() != '':
            self.message.setText("Winner" + self.buttons[1].text())
            self.Won()
        elif self.buttons[3].text() == self.buttons[5].text() == self.buttons[7].text() and self.buttons[3].text() != '':
            self.message.setText("Winner" + self.buttons[3].text())
            self.Won()
        
    def Won(self):
        Message = QMessageBox.question(self, TicTacToe.CurrentPlayer + " player won!!", "Do You Want To Play Again?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if Message == QMessageBox.No:
            exit()
        else:
            self.Restart()
    
    def Restart(self):
        # You can restart the game just by clearing the board
        for i in range(1, 10):
            self.buttons[i].setText("")

    def ChangeCurrent(self):
        if self.buttons[1] == self.buttons[2] == self.buttons[3] == self.buttons[4] == self.buttons[5] == self.buttons[6] == self.buttons[7] == self.buttons[8] == self.buttons[9] == '':
            TicTacToe.CurrentPlayer = 'X'
        elif TicTacToe.CurrentPlayer == 'X':
            TicTacToe.CurrentPlayer = 'O'
        else:
            TicTacToe.CurrentPlayer = 'X'     

if __name__ == "__main__":
    app = QApplication(argv)
    TicTacToeGame = TicTacToe()
    exit(app.exec_())

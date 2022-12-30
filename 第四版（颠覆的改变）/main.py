import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from Ui_log import Ui_MainWindow as window_1
from Ui_test import Ui_MainWindow as window_2
import password_check as pw
import back



class Win_1(QMainWindow, window_1):
    def __init__(self, parent=None):
        super(Win_1, self).__init__(parent)
        self.setupUi(self)
    
    def login(self):
        i = pw.check_password(self.lineEdit.text(),self.lineEdit_2.text())
        if i ==1:
            win_1.close()
            win_2.show()
        elif i == 0 or i == -1:
            msg_box = QMessageBox(QMessageBox.Warning, '错误', '账号或密码错误')
            msg_box.exec_()

    def clear_text(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

class Win_2(QMainWindow, window_2):
    def __init__(self, parent=None):
        super(Win_2, self).__init__(parent)
        self.setupUi(self)
    
    def over(self):
        
        choice_num=self.spinBox.value()+self.spinBox_2.value()+self.spinBox_3.value()+self.spinBox_4.value()+self.spinBox_5.value()
        choice_each_score=self.doubleSpinBox.value()
        fill_num=self.spinBox_6.value()+self.spinBox_7.value()+self.spinBox_8.value()+self.spinBox_9.value()+self.spinBox_10.value()
        fill_each_score=self.doubleSpinBox_2.value()
        answer_num=self.spinBox_14.value()+self.spinBox_12.value()+self.spinBox_13.value()+self.spinBox_11.value()+self.spinBox_15.value()
        answer_each_score=self.doubleSpinBox_3.value()
        calculte_num=self.spinBox_16.value()+self.spinBox_17.value()+self.spinBox_18.value()+self.spinBox_19.value()+self.spinBox_20.value()
        calculte_each_score=self.doubleSpinBox_4.value()
        begin,num=1,self.spinBox_21.value()
        back.choic(choice_num,choice_each_score,begin,num)
        back.fill(fill_num,fill_each_score,begin,num)
        back.answer(answer_num,answer_each_score,begin,num)
        back.calculte(calculte_num,calculte_each_score,begin,num)
        
        msg_box = QMessageBox(QMessageBox.Information, '完成', '出题完成，请到test文件夹中查看试卷')
        msg_box.exec_()
        
    def back(self):
        win_2.close()
        win_1.show()
        win_1.clear_text()
    
    def choice(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def fill(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def answer(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def calculte(self):
        self.stackedWidget.setCurrentIndex(3)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_1 = Win_1()
    win_2 = Win_2()
    win_1.show()

    sys.exit(app.exec_())

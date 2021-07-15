import datetime
import time
import sys

class Kartica:
    def __init__(self, idKartice, ime, stanje):
        self.idKartice = idKartice
        self.ime = ime
        self.stanje = stanje

    def podizanjeNovca(self, iznos):
        self.stanje -= iznos

class Bankomat:
    def __init__(self, serijskiBroj, imeBanke, lokacija):
        self.serijskiBroj = serijskiBroj
        self.imeBanke = imeBanke
        self.lokacija = lokacija

k1 = Kartica(102, "Uros Stanojkov", 1000)
k2 = Kartica(401, "Milan Avramovic", 3500)
k3 = Kartica(85, "Ivan Milenkovic", 4500)
k4 = Kartica(212, "Milos Pejic", 2700)

b = Bankomat(3310034, "Vojvodjanska banka", "Kragujevac")

kartice = [k1, k2, k3, k4]

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        self.izabranaKartica = 0
        Form.setObjectName("Form")
        Form.resize(720, 623)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.btn1 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("1"))
        self.btn1.setGeometry(QtCore.QRect(40, 290, 121, 101))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("2"))
        self.btn2.setGeometry(QtCore.QRect(190, 290, 121, 101))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("3"))
        self.btn3.setGeometry(QtCore.QRect(340, 290, 121, 101))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("4"))
        self.btn4.setGeometry(QtCore.QRect(40, 400, 121, 101))
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("5"))
        self.btn5.setGeometry(QtCore.QRect(190, 400, 121, 101))
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("6"))
        self.btn6.setGeometry(QtCore.QRect(340, 400, 121, 101))
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("7"))
        self.btn7.setGeometry(QtCore.QRect(40, 510, 121, 101))
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("8"))
        self.btn8.setGeometry(QtCore.QRect(190, 510, 121, 101))
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("9"))
        self.btn9.setGeometry(QtCore.QRect(340, 510, 121, 101))
        self.btn9.setObjectName("btn9")
        self.btn0 = QtWidgets.QPushButton(Form, clicked=lambda: self.press_it("0"))
        self.btn0.setGeometry(QtCore.QRect(490, 510, 131, 101))
        self.btn0.setObjectName("btn0")
        self.outputlabel = QtWidgets.QLabel(Form)
        self.outputlabel.setGeometry(QtCore.QRect(40, 10, 641, 161))
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputlabel.setLineWidth(2)
        self.outputlabel.setObjectName("outputlabel")
        self.inputlabel = QtWidgets.QLabel(Form)
        self.inputlabel.setGeometry(QtCore.QRect(140, 200, 441, 71))
        self.inputlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.inputlabel.setLineWidth(1)
        self.inputlabel.setText("")
        self.inputlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inputlabel.setObjectName("inputlabel")

        
        self.enter1 = QtWidgets.QPushButton(Form)
        self.enter1.setGeometry(QtCore.QRect(490, 290, 211, 211))
        self.enter1.setObjectName("enter1")
        self.enter1.clicked.connect(self.opcija1)
            
        self.enter2 = QtWidgets.QPushButton(Form)
        self.enter2.setGeometry(QtCore.QRect(490, 290, 211, 211))
        self.enter2.setObjectName("enter2")
        self.enter2.clicked.connect(self.opcija2)
        
        self.enter3 = QtWidgets.QPushButton(Form)
        self.enter3.setGeometry(QtCore.QRect(490, 290, 211, 211))
        self.enter3.setObjectName("enter3")
        self.enter3.clicked.connect(self.opcija3)

        self.enter4 = QtWidgets.QPushButton(Form)
        self.enter4.setGeometry(QtCore.QRect(490, 290, 211, 211))
        self.enter4.setObjectName("enter4")
        self.enter4.clicked.connect(self.opcija4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.enter2.hide()
        self.enter3.hide()
        self.enter4.hide()

    def press_it(self, pressed):
        self.inputlabel.setText(pressed)

    def opcija1(self):
        self.enter1.show()
        self.enter2.hide()
        self.enter3.hide()
        self.enter4.hide()
        self.outputlabel.setText("DOBRODOSLI!\n\nIzaberite jednu od ponudjenih opcija:\n\n1) Predji na ucitavanje kartice\n\n0) Napusti program")
        
        p = self.inputlabel.text()
        self.inputlabel.setText("")

        if(p=="1"):
            self.opcija2()
        elif(p=="0"):
            #treba i da stampa izvestaj
            current_time = datetime.datetime.now()
            time = current_time.strftime("%Hh_%Mmin_%Ss_%d_%m_%y")
            filename = "atm_" + time + ".out"
            f = open(filename, 'w+')
            f.write('----------------------------------------------------\n\n')
            f.write("Serijski broj bankomata:        " + str(b.serijskiBroj))
            f.write("\nNaziv banke:                    " + b.imeBanke)
            f.write("\nLokacija bankomata:             " + b.lokacija)
            f.write('\n\n----------------------------------------------------')
            f.close()
            sys.exit()
        else:
            self.outputlabel.setText("DOBRODOSLI!\n\nIzaberite jednu od ponudjenih opcija:\n\n1) Predji na ucitavanje kartice\n\n0) Napusti program\n\nMolimo vas unesite jednu od ponudjenih opcija")


    def opcija2(self):
        self.enter1.hide()
        self.enter2.show()
        self.enter3.hide()
        self.enter4.hide()

        s = "Molimo vas izaberite karticu!\n\n"
        for i in range(len(kartice)):
            s = s + str(i+1) + ") Kartica " + str(kartice[i].idKartice) + "\n"
        s = s + "\n0) Vrati se na pocetni ekran!"

        self.outputlabel.setText(s)
        
        p = self.inputlabel.text()
        self.inputlabel.setText("")

        if(p=="0"):
            self.opcija1()
        elif(p > "0" and p <= str(len(kartice))):
            self.izabranaKartica = int(p)
            self.opcija3()
        else:
            s = s + "\nMolimo vas izaberite postojecu opciju!"
            self.outputlabel.setText(s)


    def opcija3(self):
        self.enter1.hide()
        self.enter2.hide()
        self.enter3.show()
        self.enter4.hide()

        
        
        self.outputlabel.setText("Vasa kartica je sa id-jem " + str(kartice[self.izabranaKartica-1].idKartice) + "\n\n1) Podizanje gotovine\n2) Stampanje izvestaja\n\n0) Vrati se na pocetno stanje\n\nMolimo vas unesite jednu od ponudjenih opcija")

        
        p = self.inputlabel.text()
        self.inputlabel.setText("")

        

        if(p == "1"):
            self.opcija4()
        elif(p == "2"):
            current_time = datetime.datetime.now()
            format_time = current_time.strftime("%Hh_%Mmin_%Ss_%d_%m_%y")
            filename = "report_" + format_time + ".out"
            f = open(filename, 'w+')
            f.write('----------------------------------------------------\n\n')
            f.write("Redni broj kartice:         " + str(kartice[self.izabranaKartica-1].idKartice))
            f.write("\nIme vlasnika kartice:       " + kartice[self.izabranaKartica-1].ime)
            f.write("\nStanje na racunu:           " + str(kartice[self.izabranaKartica-1].stanje))
            f.write('\n\n----------------------------------------------------')
            f.close()

            time.sleep(1.5)
            
            self.opcija1()
        elif(p == "0"):
            self.opcija1()
        else:
            s = self.outputlabel.text()
            self.outputlabel.setText(s)
    
    def opcija4(self):
        self.enter1.hide()
        self.enter2.hide()
        self.enter3.hide()
        self.enter4.show()

        self.outputlabel.setText("ID kartice: " + str(kartice[self.izabranaKartica-1].idKartice) + ", Ime vlasnika: " + str(kartice[self.izabranaKartica-1].ime) + ", Stanje na racunu: " + str(kartice[self.izabranaKartica-1].stanje) + "\nIzaberite opciju za zeljeni iznos koji zelite da podignete:\n\n1) 500                 2) 1000\n3) 2000                4) 5000\n\n0) Vrati se na pocetni ekran")

        p = self.inputlabel.text()
        self.inputlabel.setText("")

        iznos = 0

        if(p=="1"):
            iznos = 500
        elif(p=="2"):
            iznos = 1000
        elif(p=="3"):
            iznos = 2000
        elif(p=="4"):
            iznos = 5000
        elif(p=="0"):
            self.opcija1()
        else:
            s = self.outputlabel.text()
            s = s + "\n\nMolimo vas unesite jednu od dozvoljenih opcija"
            self.outputlabel.setText(s)

        if(kartice[self.izabranaKartica-1].stanje >= iznos and iznos != 0):
            s = self.outputlabel.text()
            s = s + "\n\nUspesno ste podigli novac, novo stanje na racunu je: " + str(kartice[self.izabranaKartica-1].stanje - iznos)

            self.outputlabel.setText(s)

            kartice[self.izabranaKartica-1].podizanjeNovca(iznos)
            
        elif(kartice[self.izabranaKartica-1].stanje < iznos):
            s = self.outputlabel.text()
            s = s + "\n\nNemate dovoljno sredstava na racunu! Pokusajte ponovo"
            self.outputlabel.setText(s)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ATM Machine"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn3.setText(_translate("Form", "3"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn0.setText(_translate("Form", "0"))
        self.outputlabel.setText(_translate("Form", "<html><head/><body><p>DOBRODOSLI!<br/><br/>Izaberite jednu od ponudjenih opcija:<br/><br/>1) Predji na ucitavanje kartica<br/><br/>0) Napusti program</p><p><br/></p><p><br/></p></body></html>"))
        self.enter1.setText(_translate("Form", "ENTER"))
        self.enter2.setText(_translate("Form", "ENTER"))
        self.enter3.setText(_translate("Form", "ENTER"))
        self.enter4.setText(_translate("Form", "ENTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

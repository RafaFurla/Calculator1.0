from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox


def dot():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0].count('.') == 0:
            displayed_content[0] += '.'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2].count('.') == 0:
            displayed_content[2] += '.'
            return uifile.lcd.display(displayed_content[2])


def number0():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '0'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '0'
            return uifile.lcd.display(displayed_content[2])


def number1():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '1'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '1'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '1'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '1'
            return uifile.lcd.display(displayed_content[2])


def number2():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '2'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '2'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '2'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '2'
            return uifile.lcd.display(displayed_content[2])


def number3():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '3'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '3'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '3'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '3'
            return uifile.lcd.display(displayed_content[2])


def number4():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '4'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '4'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '4'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '4'
            return uifile.lcd.display(displayed_content[2])


def number5():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '5'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '5'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '5'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '5'
            return uifile.lcd.display(displayed_content[2])


def number6():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '6'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '6'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '6'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '6'
            return uifile.lcd.display(displayed_content[2])


def number7():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '7'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '7'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '7'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '7'
            return uifile.lcd.display(displayed_content[2])


def number8():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '8'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '8'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '8'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '8'
            return uifile.lcd.display(displayed_content[2])


def number9():
    global displayed_content
    if displayed_content[1] is None:
        if displayed_content[0] == '0':
            displayed_content[0] = '9'
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] += '9'
            return uifile.lcd.display(displayed_content[0])
    elif displayed_content[1]:
        if displayed_content[2] == '0':
            displayed_content[2] = '9'
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] += '9'
            return uifile.lcd.display(displayed_content[2])


def percent():
    global t
    global displayed_content
    global h
    global c
    global d
    global p
    global r
    if d == 1:
        if displayed_content != '' and p == True:
            displayed_content = ''
            p = False
        if displayed_content == '':
            if len(n) == 0:
                uifile.lcd.display(0)
            else:
                h = str(n[0])
        else:
            h = displayed_content
        d += 1
    if d != 1:
        if len(n) == 0:
            displayed_content = ''
            uifile.lcd.display(0)
        if len(n) == 2:
            t += '%'
            if n[1] == '+':
                if displayed_content == '':
                    r = (n[0]**(t.count('%')+1))/(100**t.count('%'))
                    displayed_content = str(r)
                    t = ''
                else:
                    r = (float(h)) * ((n[0]/100)**(t.count('%')))
                    displayed_content = str(r)
            elif n[1] == '-':
                if displayed_content == '':
                    r = (n[0]**(t.count('%')+1))/(100**t.count('%'))
                    displayed_content = str(r)
                    t = ''
                else:
                    r = (float(h)) * ((n[0]/100)**(t.count('%')))
                    displayed_content = str(r)
            elif n[1] == '*':
                if displayed_content == '':
                    r = n[0]/(100**t.count('%'))
                    displayed_content = str(r)
                else:
                    r = float(h)/(100**t.count('%'))
                    displayed_content = str(r)
            elif n[1] == '/':
                if displayed_content == '':
                    r = n[0]/(100**t.count('%'))
                    displayed_content = str(r)
                else:
                    r = float(h)/(100**t.count('%'))
                    displayed_content = str(r)
            uifile.lcd.display(r)


def sum():
    global displayed_content
    if (displayed_content[1]) is None or (displayed_content[1] != '+'):
        displayed_content[1] = '+'
    else:
        if float(displayed_content[2]) != 0:
            displayed_content[0] = str(float(displayed_content[0]) + float(displayed_content[2]))
            displayed_content[2] = '0'
            return uifile.lcd.display(displayed_content[0])


def sub():
    global displayed_content
    if (displayed_content[1]) is None or (displayed_content[1] != '-'):
        displayed_content[1] = '-'
    else:
        if float(displayed_content[2]) != 0:
            displayed_content[0] = str(float(displayed_content[0]) - float(displayed_content[2]))
            displayed_content[2] = '0'
            return uifile.lcd.display(displayed_content[0])


def x():
    global displayed_content
    if (displayed_content[1]) is None or (displayed_content[1] != '*'):
        displayed_content[1] = '*'
    else:
        displayed_content[0] = str(float(displayed_content[0]) * float(displayed_content[2]))
        displayed_content[2] = '0'
        return uifile.lcd.display(displayed_content[0])


def div():
    global displayed_content
    if (displayed_content[1]) is None or (displayed_content[1] != '/'):
        displayed_content[1] = '/'
    else:
        if float(displayed_content[2]) == 0:
            uifile.lcd.display('Err')
            QMessageBox.about(uifile, 'Alert', 'Division By Zero')
        else:
            displayed_content[0] = str(float(displayed_content[0]) / float(displayed_content[2]))
            displayed_content[2] = '0'
            return uifile.lcd.display(displayed_content[0])


def equal():
    global displayed_content
    if displayed_content[1] is None:
        return uifile.lcd.display(displayed_content[0])
    else:
        if displayed_content[1] == '+':
            return sum()
        if displayed_content[1] == '-':
            return sub()
        if displayed_content[1] == '*':
            return x()
        if displayed_content[1] == '/':
            return div()


def clear():
    global displayed_content
    displayed_content = ['0', None, '0']
    return uifile.lcd.display(displayed_content[0])


def cancel_entry():
    global displayed_content
    if displayed_content[1] is None:
        displayed_content[0] = '0'
        displayed_content[2] = '0'
        return uifile.lcd.display(displayed_content[0])
    # elif (displayed_content[1] != None) and displayed_content[]
    else:
        displayed_content[2] = '0'
        return uifile.lcd.display(displayed_content[2])


def del_last():
    global displayed_content
    if displayed_content[1] is None:
        if len(displayed_content[0]) > 1:
            displayed_content[0] = displayed_content[0][:-1]
            return uifile.lcd.display(displayed_content[0])
        else:
            displayed_content[0] = '0'
            displayed_content[2] = '0'
            return uifile.lcd.display(displayed_content[0])
    else:
        if len(displayed_content[2]) > 1:
            displayed_content[2] = displayed_content[2][:-1]
            return uifile.lcd.display(displayed_content[2])
        else:
            displayed_content[2] = '0'
            return uifile.lcd.display(displayed_content[2])


displayed_content = ['0', None, '0']
app = QtWidgets.QApplication([])
uifile = uic.loadUi('calculator.ui')
uifile.b0.clicked.connect(number0)
uifile.b1.clicked.connect(number1)
uifile.b2.clicked.connect(number2)
uifile.b3.clicked.connect(number3)
uifile.b4.clicked.connect(number4)
uifile.b5.clicked.connect(number5)
uifile.b6.clicked.connect(number6)
uifile.b7.clicked.connect(number7)
uifile.b8.clicked.connect(number8)
uifile.b9.clicked.connect(number9)
uifile.bsum.clicked.connect(sum)
uifile.bsub.clicked.connect(sub)
uifile.bx.clicked.connect(x)
uifile.bdiv.clicked.connect(div)
uifile.bequal.clicked.connect(equal)
uifile.bc.clicked.connect(clear)
uifile.bce.clicked.connect(cancel_entry)
uifile.bdot.clicked.connect(dot)
uifile.bdel.clicked.connect(del_last)
uifile.bperc.clicked.connect(percent)
uifile.show()
app.exec()

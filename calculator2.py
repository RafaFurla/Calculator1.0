from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
def dot():
    global k
    if k == '':
        k = '0.'
    else:
        if k.count('.') > 0:
            k = k
        else:
            if float(k) == 0:
                k = '0.'
            elif float(k) != 0:
                k += '.'
    uifile.lcd.display(k)
def number0():
    global k
    global t
    if t.count('%') > 0:
        k = '0'
    elif k == '':
        k = '0'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '0'
        else:
            k = '0'
    elif float(k) != 0:
        k += '0'
    uifile.lcd.display(k)
def number1():
    global k
    global t
    if t.count('%') > 0:
        k = '1'
    elif k == '':
        k = '1'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '1'
        else:
            k = '1'
    elif float(k) != 0:
        k += '1'
    uifile.lcd.display(k)
def number2():
    global k
    global t
    if t.count('%') > 0:
        k = '2'
    elif k == '':
        k = '2'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '2'
        else:
            k = '2'
    elif float(k) != 0:
        k += '2'
    uifile.lcd.display(k)
def number3():
    global k
    global t
    if t.count('%') > 0:
        k = '3'
    elif k == '':
        k = '3'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '3'
        else:
            k = '3'
    elif float(k) != 0:
        k += '3'
    uifile.lcd.display(k)
def number4():
    global k
    global t
    if t.count('%') > 0:
        k = '4'
    elif k == '':
        k = '4'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '4'
        else:
            k = '4'
    elif float(k) != 0:
        k += '4'
    uifile.lcd.display(k)
def number5():
    global k
    global t
    if t.count('%') > 0:
        k = '5'
    elif k == '':
        k = '5'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '5'
        else:
            k = '5'
    elif float(k) != 0:
        k += '5'
    uifile.lcd.display(k)
def number6():
    global k
    global t
    if t.count('%') > 0:
        k = '6'
    elif k == '':
        k = '6'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '6'
        else:
            k = '6'
    elif float(k) != 0:
        k += '6'
    uifile.lcd.display(k)
def number7():
    global k
    global t
    if t.count('%') > 0:
        k = '7'
    elif k == '':
        k = '7'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '7'
        else:
            k = '7'
    elif float(k) != 0:
        k += '7'
    uifile.lcd.display(k)
def number8():
    global k
    global t
    if t.count('%') > 0:
        k = '8'
    elif k == '':
        k = '8'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '8'
        else:
            k = '8'
    elif float(k) != 0:
        k += '8'
    uifile.lcd.display(k)
def number9():
    global k
    global t
    if t.count('%') > 0:
        k = '9'
    elif k == '':
        k = '9'
    elif float(k) == 0:
        if k.count('.') > 0:
            k += '9'
        else:
            k = '9'
    elif float(k) != 0:
        k += '9'
    uifile.lcd.display(k)
def percent():
    global t
    global k
    global h
    global c
    global d
    global p
    global r
    if d == 1:
        if k != '' and p == True:
            k = ''
            p = False
        if k == '':
            if len(n) == 0:
                uifile.lcd.display(0)
            else:
                h = str(n[0])
        else:
            h = k
        d += 1
    if d != 1:
        if len(n) == 0:
            k = ''
            uifile.lcd.display(0)
        if len(n) == 2:
            t += '%'
            if n[1] == '+':
                if k == '':
                    r = (n[0]**(t.count('%')+1))/(100**t.count('%'))
                    k = str(r)
                    t = ''
                else:
                    r = (float(h)) * ((n[0]/100)**(t.count('%')))
                    k = str(r)
            elif n[1] == '-':
                if k == '':
                    r = (n[0]**(t.count('%')+1))/(100**t.count('%'))
                    k = str(r)
                    t = ''
                else:
                    r = (float(h)) * ((n[0]/100)**(t.count('%')))
                    k = str(r)
            elif n[1] == '*':
                if k == '':
                    r = n[0]/(100**t.count('%'))
                    k = str(r)
                else:
                    r = float(h)/(100**t.count('%'))
                    k = str(r)
            elif n[1] == '/':
                if k == '':
                    r = n[0]/(100**t.count('%'))
                    k = str(r)
                else:
                    r = float(h)/(100**t.count('%'))
                    k = str(r)
            uifile.lcd.display(r)
def sum():
    global n
    global k
    global r
    global c
    global p
    global d
    global t
    global h
    global s
    c = 1
    d = 1
    t = ''
    if k != '' and p == True:
        k = ''
        p = False
    if len(n) == 0:
        if k == '':
            n.append(0)
            n.append('+')
        else:
            n.append(float(k))
            n.append('+')
            k = ''
    elif len(n) == 2:
        if k == '':
            n[1] = '+'
            n[0] = float(uifile.lcd.value())
        else:
            n.append(float(k))
            k = ''
            if n[1] == '+':
                r = n[0] + n[2]
            elif n[1] == '-':
                r = n[0] - n[2]
            elif n[1] == '*':
                r = n[0] * n[2]
            elif n[1] == '/':
                try:
                    r = n[0] / n[2]
                except ZeroDivisionError:
                    QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                    del n
                    n = []
                    c = 1
                    d = 1
                    r = float(0)
                    s = ''
                    h = ''
                    k = ''
                    t = ''
                    p = False
                    uifile.lcd.display(r)
            if len(n) != 0:
                n[0] = r
                n[1] = '+'
                n.pop(2)
            uifile.lcd.display(r)
def sub():
    global n
    global k
    global r
    global c
    global p
    global d
    global t
    global h
    global s
    c = 1
    d = 1
    t = ''
    if k != '' and p == True:
        k = ''
        p = False
    if len(n) == 0:
        if k == '':
            n.append(0)
            n.append('-')
        else:
            n.append(float(k))
            n.append('-')
            k = ''
    elif len(n) == 2:
        if k == '':
            n[1] = '-'
            n[0] = float(uifile.lcd.value())
        else:
            n.append(float(k))
            k = ''
            if n[1] == '+':
                r = n[0] + n[2]
            elif n[1] == '-':
                r = n[0] - n[2]
            elif n[1] == '*':
                r = n[0] * n[2]
            elif n[1] == '/':
                try:
                    r = n[0] / n[2]
                except ZeroDivisionError:
                    QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                    del n
                    n = []
                    c = 1
                    d = 1
                    r = float(0)
                    s = ''
                    h = ''
                    k = ''
                    t = ''
                    p = False
                    uifile.lcd.display(r)
            if len(n) != 0:
                n[0] = r
                n[1] = '-'
                n.pop(2)
            uifile.lcd.display(r)
def x():
    global n
    global k
    global r
    global c
    global p
    global d
    global t
    global h
    global s
    c = 1
    d = 1
    t = ''
    if k != '' and p == True:
        k = ''
        p = False
    if len(n) == 0:
        if k == '':
            n.append(0)
            n.append('*')
        else:
            n.append(float(k))
            n.append('*')
            k = ''
    elif len(n) == 2:
        if k == '':
            n[1] = '*'
            n[0] = float(uifile.lcd.value())
        else:
            n.append(float(k))
            k = ''
            if n[1] == '+':
                r = n[0] + n[2]
            elif n[1] == '-':
                r = n[0] - n[2]
            elif n[1] == '*':
                r = n[0] * n[2]
            elif n[1] == '/':
                try:
                    r = n[0] / n[2]
                except ZeroDivisionError:
                    QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                    del n
                    n = []
                    c = 1
                    d = 1
                    r = float(0)
                    s = ''
                    h = ''
                    k = ''
                    t = ''
                    p = False
                    uifile.lcd.display(r)
            if len(n) != 0:
                n[0] = r
                n[1] = '*'
                n.pop(2)
            uifile.lcd.display(r)
def div():
    global n
    global k
    global r
    global c
    global p
    global d
    global t
    global h
    global s
    c = 1
    d = 1
    t = ''
    if k != '' and p == True:
        k = ''
        p = False
    if len(n) == 0:
        if k == '':
            n.append(0)
            n.append('/')
        else:
            n.append(float(k))
            n.append('/')
            k = ''
    elif len(n) == 2:
        if k == '':
            n[1] = '/'
            n[0] = float(uifile.lcd.value())
        else:
            n.append(float(k))
            k = ''
            if n[1] == '+':
                r = n[0] + n[2]
            elif n[1] == '-':
                r = n[0] - n[2]
            elif n[1] == '*':
                r = n[0] * n[2]
            elif n[1] == '/':
                try:
                    r = n[0] / n[2]
                except ZeroDivisionError:
                    QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                    del n
                    n = []
                    c = 1
                    d = 1
                    r = float(0)
                    s = ''
                    h = ''
                    k = ''
                    t = ''
                    p = False
                    uifile.lcd.display(r)
            if len(n) != 0:
                n[0] = r
                n[1] = '/'
                n.pop(2)
            uifile.lcd.display(r)
def equal():
    global n
    global k
    global r
    global c
    global p
    global d
    global t
    global h
    global s
    d = 1
    t = ''
    if len(n) == 0 and k == '':
        n.append(0)
        r = n[0]
        uifile.lcd.display(r)
    elif len(n) == 0 and k != '':
        n.append(float(k))
        k = ''
        r = n[0]
        uifile.lcd.display(r)
    if len(n) == 2 and k == '':
        if c == 1:
            n.append(n[0])
            if n[1] == '+':
                r = n[0] + n[2]
            elif n[1] == '-':
                r = n[0] - n[2]
            elif n[1] == '*':
                r = n[0] * n[2]
            elif n[1] == '/':
                try:
                    r = n[0] / n[2]
                except ZeroDivisionError:
                    QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                    del n
                    n = []
                    c = 1
                    d = 1
                    r = float(0)
                    s = ''
                    h = ''
                    k = ''
                    t = ''
                    p = False
                    uifile.lcd.display(r)
            if len(n) != 0:
                n.pop(2)
                s = n[0]
            uifile.lcd.display(r)
            c += 1
        else:
            n.append(s)
            n[0] = r
            if n[1] == '+':
                r = n[0] + n[2]
            elif n[1] == '-':
                r = n[0] - n[2]
            elif n[1] == '*':
                r = n[0] * n[2]
            elif n[1] == '/':
                try:
                    r = n[0] / n[2]
                except ZeroDivisionError:
                    QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                    del n
                    n = []
                    c = 1
                    d = 1
                    r = float(0)
                    s = ''
                    h = ''
                    k = ''
                    t = ''
                    p = False
                    uifile.lcd.display(r)
            if len(n) != 0:
                n.pop(2)
            uifile.lcd.display(r)
            c += 1
    if len(n) == 2 and k != '':
        if c == 1:
            p = True
            s = k
            n.append(float(s))
            if n[1] == '+':
                r = n[0] + n[2]
            elif n[1] == '-':
                r = n[0] - n[2]
            elif n[1] == '*':
                r = n[0] * n[2]
            elif n[1] == '/':
                try:
                    r = n[0] / n[2]
                except ZeroDivisionError:
                    QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                    del n
                    n = []
                    c = 1
                    d = 1
                    r = float(0)
                    s = ''
                    h = ''
                    k = ''
                    t = ''
                    p = False
                    uifile.lcd.display(r)
            if len(n) != 0:
                n[0] = r
                n.pop(2)
            c += 1
            uifile.lcd.display(r)
        else:
            n[0] = r
            n.append(float(s))
            if n[1] == '+':
                r = n[0] + n[2]
            elif n[1] == '-':
                r = n[0] - n[2]
            elif n[1] == '*':
                r = n[0] * n[2]
            elif n[1] == '/':
                try:
                    r = n[0] / n[2]
                except ZeroDivisionError:
                    QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                    del n
                    n = []
                    c = 1
                    d = 1
                    r = float(0)
                    s = ''
                    h = ''
                    k = ''
                    t = ''
                    p = False
                    uifile.lcd.display(r)
            if len(n) != 0:
                n[0] = r
                n.pop(2)
            c += 1
            uifile.lcd.display(r)
def clear():
    global n
    global k
    global r
    global c
    global p
    global d
    global t
    global h
    global s
    del n
    n = []
    c = 1
    d = 1
    r = float(0)
    s = ''
    h = ''
    k = ''
    t = ''
    p = False
    uifile.lcd.display(r)
#def cancel_entry():
#    global k
#    k = '0'
#    uifile.lcd.display(k)
def cancel_entry():
    global k
    k = '0'
    uifile.lcd.display(k)
'''def del_last():
    global k
    global r
    print(k)
    if uifile.lcd.value() == str(k):
        if len(k) > 1:
            k = k[:-1]
            print('corta')
        elif len(k) <= 1:
            k = '0'
            print('transforma em zero')
        uifile.lcd.display(k)
        print('display k')
    elif uifile.lcd.value() == str(r):
        uifile.lcd.display(r)
        print('display r')'''
def del_last():
    global k
    global r
    if len(k) > 1:
        k = k[:-1]
    elif len(k) <= 1:
        k = '0'
    uifile.lcd.display(k)


n = []
c = 1
d = 1
s = ''
h = ''
k = ''
t = ''
r = float(0)
p = False
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
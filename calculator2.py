from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox


def dot():
    global result
    if result.count('.') == 0:
        if result == 'None':
            result = '0.'
        else:
            result += '.'
        return uifile.lcd.display(result)


def numbers(number):
    global result
    if (result == '0') or (result == 'None'):
        result = number
    else:
        result += number
    return uifile.lcd.display(result)


def number0():
    numbers('0')


def number1():
    numbers('1')


def number2():
    numbers('2')


def number3():
    numbers('3')


def number4():
    numbers('4')


def number5():
    numbers('5')


def number6():
    numbers('6')


def number7():
    numbers('7')


def number8():
    numbers('8')


def number9():
    numbers('9')


def percent():
    global displayed_content
    if displayed_content[1] is None:
        displayed_content[0] = '0'
        return uifile.lcd.display(displayed_content[0])
    else:
        if displayed_content[2] == '0':
            displayed_content[2] = str(float(displayed_content[0]) * (float(displayed_content[0]) / 100))
            return uifile.lcd.display(displayed_content[2])
        if displayed_content[2] != '0':
            displayed_content[2] = str(float(displayed_content[0]) * (float(displayed_content[2]) / 100))
            return uifile.lcd.display(displayed_content[2])


def operations(operator):
    global displayed_content
    global result
    if (result == 'None') and (displayed_content == ['None', None, 'None']):
        displayed_content[0] = '0'
        displayed_content[1] = operator
    elif (result != 'None') and (displayed_content[0] == 'None'):
        displayed_content[0] = result
        displayed_content[1] = operator
        displayed_content[2] = 'None'
        result = 'None'
    elif (result == 'None') and (displayed_content[0] != 'None'):
        displayed_content[1] = operator
        displayed_content[2] = 'None'
    elif (result != 'None') and (displayed_content[0] != 'None'):
        if displayed_content[1] == operator:
            if (operator == '/') and (result == '0'):
                uifile.lcd.display('Err')
                QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                displayed_content = ['None', None, 'None']
                result = 'None'
                return
            if operator == '+':
                result = str(float(displayed_content[0]) + float(result))
            elif operator == '-':
                result = str(float(displayed_content[0]) - float(result))
            elif operator == '*':
                result = str(float(displayed_content[0]) * float(result))
            elif operator == '/':
                result = str(float(displayed_content[0]) / float(result))
            displayed_content[0] = result
            uifile.lcd.display(result)
        if displayed_content[1] != operator:
            if displayed_content[1] == '+':
                sum()
                displayed_content[1] = operator
            elif displayed_content[1] == '-':
                sub()
                displayed_content[1] = operator
            elif displayed_content[1] == '*':
                x()
                displayed_content[1] = operator
            elif displayed_content[1] == '/':
                div()
                displayed_content[1] = operator
        result = 'None'


def sum():
    operations('+')


def sub():
    operations('-')


def x():
    operations('*')


def div():
    operations('/')


def equal():
    global displayed_content
    global result
    if (result == 'None') and (displayed_content == ['None', None, 'None']):
        result = '0'
        uifile.lcd.display(result)
    elif (result != 'None') and (displayed_content == ['None', None, 'None']):
        return uifile.lcd.display(result)
    elif (result == 'None') and (displayed_content[1] is not None):
        if displayed_content[2] == 'None':
            displayed_content[2] = displayed_content[0]
        if displayed_content[1] == '+':
            result = str(float(displayed_content[0]) + float(displayed_content[2]))
        elif displayed_content[1] == '-':
            result = str(float(displayed_content[0]) - float(displayed_content[2]))
        elif displayed_content[1] == '*':
            result = str(float(displayed_content[0]) * float(displayed_content[2]))
        elif displayed_content[1] == '/':
            result = str(float(displayed_content[0]) / float(displayed_content[2]))
        uifile.lcd.display(result)
        displayed_content[0] = result
        result = 'None'
    elif (result != 'None') and (displayed_content[1] is not None):
        displayed_content[2] = result
        if displayed_content[1] == '+':
            sum()
        elif displayed_content[1] == '-':
            sub()
        elif displayed_content[1] == '*':
            x()
        elif displayed_content[1] == '/':
            div()


def clear():
    global displayed_content
    global result
    displayed_content = ['None', None, 'None']
    result = 'None'
    return uifile.lcd.display('0')


def cancel_entry():
    global displayed_content
    global result
    result = '0'
    uifile.lcd.display(result)


def del_last():
    global result
    if result != 'None':
        if len(result) > 1:
            result = result[:-1]
        elif len(result) == 1:
            result = '0'
        return uifile.lcd.display(result)


displayed_content = ['None', None, 'None']
result = 'None'
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

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox


def number0():
    """This function is activated when the user press the number 0 button in the calculator."""
    numbers('0')


def number1():
    """This function is activated when the user press the number 1 button in the calculator."""
    numbers('1')


def number2():
    """This function is activated when the user press the number 2 button in the calculator."""
    numbers('2')


def number3():
    """This function is activated when the user press the number 3 button in the calculator."""
    numbers('3')


def number4():
    """This function is activated when the user press the number 4 button in the calculator."""
    numbers('4')


def number5():
    """This function is activated when the user press the number 5 button in the calculator."""
    numbers('5')


def number6():
    """This function is activated when the user press the number 6 button in the calculator."""
    numbers('6')


def number7():
    """This function is activated when the user press the number 7 button in the calculator."""
    numbers('7')


def number8():
    """This function is activated when the user press the number 8 button in the calculator."""
    numbers('8')


def number9():
    """This function is activated when the user press the number 9 button in the calculator."""
    numbers('9')


def numbers(number):
    """This function is called by the number functions (number0, number1, ...). Its purpose is to put the right
    number, pressed by the calculator's user, inside the variable 'screen'."""
    global screen
    if (screen == '0') or (screen == 'None'):
        screen = number
    else:
        screen += number
    return uifile.lcd.display(screen)


def dot():
    """This function is activated when the user press the dot button in the calculator. Its purpose is to put the
    '.' (dot) symbol inside the variable 'screen', if the situation permits."""
    global screen
    if screen.count('.') == 0:
        if screen == 'None':
            screen = '0.'
        else:
            screen += '.'
        return uifile.lcd.display(screen)


def percent():
    """This function is activated when the user press the percent button (%) in the calculator. When pressed, this
    function calculates de percentage of the last value number pressed by the user. This value is saved inside 'screen'
    variable."""
    global memory
    global screen
    if (screen == 'None') and (memory[0] != 'None'):
        screen = memory[0]
    if screen != 'None':
        screen = str((float(screen) / 100))
    return uifile.lcd.display(screen)


def add():
    """This function is activated when the user press the add (+) button in the calculator."""
    operations('+')


def sub():
    """This function is activated when the user press the subtraction (-) button in the calculator."""
    operations('-')


def x():
    """This function is activated when the user press the multiplication (x) button in the calculator."""
    operations('*')


def div():
    """This function is activated when the user press the division (/) button in the calculator."""
    operations('/')


def operations(operator):
    """This function is called by the operation functions (add, sub, x and div). Its purpose is to save the operation
    chose by the user in the memory[1] variable. But in some cases it can calculate the result of the operation."""
    global memory
    global screen
    if (screen == 'None') and (memory == ['None', None, 'None']):
        memory[0] = '0'
        memory[1] = operator
    elif (screen != 'None') and (memory[0] == 'None'):
        memory[0] = screen
        memory[1] = operator
        memory[2] = 'None'
        screen = 'None'
    elif (screen == 'None') and (memory[0] != 'None'):
        memory[1] = operator
        memory[2] = 'None'
    elif (screen != 'None') and (memory[0] != 'None'):
        if memory[1] == operator:
            if (operator == '/') and (screen == '0'):
                uifile.lcd.display('Err')
                QMessageBox.about(uifile, 'Alert', 'Division By Zero')
                memory = ['None', None, 'None']
                screen = 'None'
                return
            if operator == '+':
                screen = str(float(memory[0]) + float(screen))
            elif operator == '-':
                screen = str(float(memory[0]) - float(screen))
            elif operator == '*':
                screen = str(float(memory[0]) * float(screen))
            elif operator == '/':
                screen = str(float(memory[0]) / float(screen))
            memory[0] = screen
            uifile.lcd.display(screen)
        if memory[1] != operator:
            if memory[1] == '+':
                add()
                memory[1] = operator
            elif memory[1] == '-':
                sub()
                memory[1] = operator
            elif memory[1] == '*':
                x()
                memory[1] = operator
            elif memory[1] == '/':
                div()
                memory[1] = operator
        screen = 'None'


def equal():
    """This function is activated when the user press the equal symbol (=) button in the calculator. This purpose is
    to calculate the operation chose by the user."""
    global memory
    global screen
    if (screen == 'None') and (memory == ['None', None, 'None']):
        # situation when the user click the equal button when the calculator starts.
        screen = '0'
        uifile.lcd.display(screen)
    elif (screen != 'None') and (memory == ['None', None, 'None']):
        # situation when the user click the equal button after starts the calculator and click in a number.
        return uifile.lcd.display(screen)
    elif (screen == 'None') and (memory[1] is not None):
        # situation when the user click the equal button after starts the calculator and click in an operation button.
        if memory[2] == 'None':
            memory[2] = memory[0]
        if memory[1] == '+':
            screen = str(float(memory[0]) + float(memory[2]))
        elif memory[1] == '-':
            screen = str(float(memory[0]) - float(memory[2]))
        elif memory[1] == '*':
            screen = str(float(memory[0]) * float(memory[2]))
        elif memory[1] == '/':
            screen = str(float(memory[0]) / float(memory[2]))
        uifile.lcd.display(screen)
        memory[0] = screen
        screen = 'None'
    elif (screen != 'None') and (memory[1] is not None):
        # situation when the user click the equal button after input the first, operation and the last number.
        memory[2] = screen
        if memory[1] == '+':
            add()
        elif memory[1] == '-':
            sub()
        elif memory[1] == '*':
            x()
        elif memory[1] == '/':
            div()


def clear():
    global memory
    global screen
    """This function is activated when the user press the clear button (C) in the calculator. Its purpose is to clear 
    the screen and all the memory data."""
    memory = ['None', None, 'None']
    screen = 'None'
    return uifile.lcd.display('0')


def cancel_entry():
    """This function is activated when the user press the cancel entry button (CE) in the calculator. Its purpose is to
    clear the screen and the variable 'screen'."""
    global screen
    screen = '0'
    uifile.lcd.display(screen)


def del_last():
    """This function is activated when the user press the backspace button (<-) in the calculator. Its purpose is to
        clear the last entry inside the 'screen' variable."""
    global screen
    if screen != 'None':
        if len(screen) > 1:
            screen = screen[:-1]
        elif len(screen) == 1:
            screen = '0'
        return uifile.lcd.display(screen)


if __name__ == "__main__":
    memory = ['None', None, 'None']
    """The variable memory is used to save the first number entry by the user in memory[0] space. Is also used to save 
    the operation chose by the user in memory[1] and the last number entry by the user in memory[2]. All entries are 
    saved as strings, converted in float numbers to make the operations and then reconverted in strings."""

    screen = 'None'
    """The variable screen is used to save the data that goes to the calculator screen."""

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
    uifile.bsum.clicked.connect(add)
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

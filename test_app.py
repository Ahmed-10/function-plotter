import pytest
import PySide2.QtCore as QtCore
from view import WinView


@pytest.fixture
def app(qtbot):
    test_app = WinView()
    qtbot.addWidget(test_app)
    return test_app


def test(app):
    assert app.output_terminal.toPlainText() == ">  type a function you want to plot \n>  ex:-  x^2 + 4*x + 5"

# more test cases can be added for testing
valid_inputs_func = ['5*x^3 + 2*x', 'x^2 + 4*x + 5']

"Invalid Input character: {self.current_char}"
def test_valid_inputs(app, qtbot):
    for input in valid_inputs_func:
        app.func_input.setText(input)
        app.start_input.setText('1')
        app.stop_input.setText('4')
        app.step_input.setText('1')
        qtbot.mouseClick(app.plot_btn, QtCore.Qt.LeftButton)
        assert app.output_terminal.toPlainText() == ">  function is plotted successfully"
        assert app.plot != None

def test_invalid_func(app, qtbot):
    app.func_input.setText('X*3')
    app.start_input.setText('1')
    app.stop_input.setText('4')
    app.step_input.setText('1')
    qtbot.mouseClick(app.plot_btn, QtCore.Qt.LeftButton)
    assert app.output_terminal.toPlainText() == "Invalid Input character"
    assert app.plot == None


def test_uncovered_case_func(app, qtbot):
    app.func_input.setText('(x + 3)^2')
    app.start_input.setText('1')
    app.stop_input.setText('4')
    app.step_input.setText('1')
    qtbot.mouseClick(app.plot_btn, QtCore.Qt.LeftButton)
    assert app.output_terminal.toPlainText() == 'this case is under development, please redistribute the power over the expression'
    assert app.plot == None


def test_invalid_start(app, qtbot):
    app.func_input.setText(valid_inputs_func[0])
    app.start_input.setText('a')
    app.stop_input.setText('4')
    app.step_input.setText('1')
    qtbot.mouseClick(app.plot_btn, QtCore.Qt.LeftButton)
    assert app.output_terminal.toPlainText() == "> start value is not a valid number: a"
    assert app.plot == None


def test_invalid_stop(app, qtbot):
    app.func_input.setText(valid_inputs_func[0])
    app.start_input.setText('1')
    app.stop_input.setText('a')
    app.step_input.setText('1')
    qtbot.mouseClick(app.plot_btn, QtCore.Qt.LeftButton)
    assert app.output_terminal.toPlainText() == f"> stop value is not a valid number: {app.stop_input.text()}"
    assert app.plot == None

def test_stop_is_less_than_start(app, qtbot):
    app.func_input.setText(valid_inputs_func[0])
    app.start_input.setText('1')
    app.stop_input.setText('1')
    app.step_input.setText('1')
    qtbot.mouseClick(app.plot_btn, QtCore.Qt.LeftButton)
    assert app.output_terminal.toPlainText() == f">  stop value can't be less or equal start value : {app.stop}"
    assert app.plot == None

def test_invalid_step(app, qtbot):
    app.func_input.setText(valid_inputs_func[0])
    app.start_input.setText('1')
    app.stop_input.setText('4')
    app.step_input.setText('a')
    qtbot.mouseClick(app.plot_btn, QtCore.Qt.LeftButton)
    assert app.output_terminal.toPlainText() == f"> step value is not a valid number: {app.step_input.text()}"
    assert app.plot == None

def test_step_is_less_than_zero(app, qtbot):
    app.func_input.setText(valid_inputs_func[0])
    app.start_input.setText('1')
    app.stop_input.setText('4')
    app.step_input.setText('-1')
    qtbot.mouseClick(app.plot_btn, QtCore.Qt.LeftButton)
    assert app.output_terminal.toPlainText() == f">  step value can't be less or equal 0 : {app.step}"
    assert app.plot == None
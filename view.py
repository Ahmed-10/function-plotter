import os
from plot import Plot
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QTextEdit
import PySide2.QtCore as QtCore
from PySide2.QtGui import QFontDatabase, QFont
from config import (
    fonts_paths, 
    primary_font, 
    secondary_font,
    app_background, 
    label_style, 
    input_style, 
    btn_style,
    output_style,
)

class WinView(QWidget):
    def __init__(self):
        super().__init__()

        # main widget config
        self.setFixedSize(800, 600)
        self.setStyleSheet(app_background)

        fonts = QFontDatabase()
        for path in fonts_paths:
            fonts.addApplicationFont(os.path.join(os.path.dirname(__file__), path))
        
        self.setFont(QFont(primary_font))

        # function input text and label
        self.func_label, self.func_input = self.__add_input(
            self, 
            'type a function in one variable x', 
            label_pos_x=80, 
            label_pos_y=0, 
            input_pos_x=80, 
            input_pos_y= 40, 
            label_width=350, 
            label_height=40, 
            input_width=350, 
            input_height=30
        )

        # start, stop, and step values input
        self.start_label, self.start_input = self.__add_input(
            self,
            'start value',
            label_pos_x=470,
            label_pos_y=15,
            input_pos_x=550,
            input_pos_y=20
        )
        self.stop_label, self.stop_input = self.__add_input(
            self,
            'stop value',
            label_pos_x=470,
            label_pos_y=45,
            input_pos_x=550,
            input_pos_y=50
        )
        self.step_label, self.step_input = self.__add_input(
            self,
            'step',
            label_pos_x=630,
            label_pos_y=15,
            input_pos_x=670,
            input_pos_y=20
        )

        # plot button
        self.plot_btn = self.__add_action_btn(self, "> plot")
        self.plot_btn.clicked.connect(self.handle_click)
        
        # output teminal
        self.output_terminal = self.__add_output_terminal(
            self, 
            """>  type a function you want to plot \n>  ex:-  x^2 + 4*x + 5"""    
        )

        # plot 
        self.plot = None

        self.show()
    

    # default values are for the small inputs (start value, stop value, step)
    def __add_input(self, parent, text, label_pos_x, label_pos_y, input_pos_x, input_pos_y, label_width=100, label_height=24, input_width=50, input_height=20):
        label = QLabel(text, parent=parent)
        label.setFont(QFont(primary_font))
        label.setStyleSheet(label_style)
        label.resize(label_width, label_height)
        label.move(label_pos_x, label_pos_y)

        input = QLineEdit(parent=parent)
        input.setFont(QFont(secondary_font))
        input.setStyleSheet(input_style)
        input.resize(input_width, input_height)
        input.move(input_pos_x, input_pos_y)

        return label, input


    def __add_action_btn(self, parent, text, width=90, height=20, pos_x=630, pos_y=50):
        button = QPushButton(text, parent=parent)
        button.resize(width, height)
        button.move(pos_x , pos_y)
        button.setStyleSheet(btn_style)

        return button


    def __add_output_terminal(self, parent, text, width=640, height=50, pos_x=80, pos_y=80):
        output = QTextEdit(parent=parent)
        output.setFont(QFont(primary_font))
        output.setStyleSheet(output_style)
        output.resize(width, height)
        output.move(pos_x, pos_y)
        output.setText(text)

        return output


    @QtCore.Slot()
    def handle_click(self):
        output = self.__validate_input()
        if output == 'valid':
            try:
                if self.plot:
                    self.plot.deleteLater()
                self.plot = Plot(self, self.func_input.text(), self.start, self.stop, self.step)
                self.plot.show()
                self.plot.move(80, 150)
                self.__set_output_txt('>  function is plotted successfully')
            except Exception as error:
                self.__set_output_txt(str(error))
        else:
            self.__set_output_txt(str(output))


    def __validate_input(self):
        try:
            self.start = float(self.start_input.text())
        except ValueError:
            return f"> start value is not a valid number: {self.start_input.text()}"

        try:
            self.stop = float(self.stop_input.text())
            if self.start >= self.stop:
                raise Exception(f">  stop value can't be less or equal start value : {self.stop}")
        except ValueError:
            return f"> stop value is not a valid number: {self.stop_input.text()}"
        except Exception as error:
            return error

        try:
            self.step = float(self.step_input.text())
            if self.step <= 0:
                raise Exception(f">  step value can't be less or equal 0 : {self.step}")
        except ValueError:
            return f"> step value is not a valid number: {self.step_input.text()}"
        except Exception as error:
            return error
        
        return 'valid'


    def __set_output_txt(self, text):
        self.output_terminal.setText(text)

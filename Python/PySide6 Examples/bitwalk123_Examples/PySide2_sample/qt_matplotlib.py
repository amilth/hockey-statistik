#!/usr/bin/env python
# coding: utf-8

import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pandas as pd


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('SPC Chart')
        self.show()

    def initUI(self):
        # example dataframe
        df = pd.DataFrame({
            'Sample': list(range(1, 11)),
            'Y': [9.030, 8.810, 9.402, 8.664, 8.773, 8.774, 8.416, 9.101, 8.687, 8.767]
        })
        # SPC metrics
        spec_usl = 9.97
        spec_target = 8.70
        spec_lsl = 7.43
        value_mean = df.describe().at['mean', 'Y']

        # spc chart
        fig = plt.figure(dpi=100)
        ax = fig.add_subplot(111, title="SPC Chart Example")
        plt.subplots_adjust(bottom=0.2, left=0.2, right=0.8, top=0.9)
        ax.grid(True)

        # horizontal lines
        ax.axhline(y=spec_usl, linewidth=1, color='red', label='USL')
        ax.axhline(y=spec_target, linewidth=1, color='blue', label='Target')
        ax.axhline(y=spec_lsl, linewidth=1, color='red', label='LSL')
        ax.axhline(y=value_mean, linewidth=1, color='green', label='Avg')

        # trend
        ax.plot(df['Sample'], df['Y'], color="gray", marker="o", markersize=10)
        ax.yaxis.label.set_color('gray')
        ax.tick_params(axis='y', colors='gray')

        # add extra ticks
        extraticks = [spec_lsl, spec_target, spec_usl]
        ax.set_yticks(list(ax.get_yticks()) + extraticks)
        fig.canvas.draw()

        # label
        labels = [item.get_text() for item in ax.get_yticklabels()]
        n = len(labels)
        labels[n - 3] = 'LSL = ' + str(spec_lsl)
        labels[n - 2] = 'Target = ' + str(spec_target)
        labels[n - 1] = 'USL = ' + str(spec_usl)
        ax.set_yticklabels(labels)

        # color
        yticklabels = ax.get_yticklabels()
        n = len(yticklabels)
        yticklabels[n - 3].set_color('red')
        yticklabels[n - 2].set_color('blue')
        yticklabels[n - 1].set_color('red')

        # add second y axis wish same range as first y axis
        ax2 = ax.twinx()
        ax2.set_ylim(ax.get_ylim())
        ax2.tick_params(axis='y', colors='gray')

        # add extra ticks
        extraticks2 = [value_mean]
        ax2.set_yticks(list(ax2.get_yticks()) + extraticks2)
        # fig.canvas.draw(); # no need to update

        # label for second y axis
        labels2 = [item.get_text() for item in ax2.get_yticklabels()]
        n = len(labels2)
        labels2[n - 1] = 'Avg = ' + str(value_mean)
        ax2.set_yticklabels(labels2)

        # color for second y axis
        yticklabels2 = ax2.get_yticklabels()
        n = len(yticklabels2)
        yticklabels2[n - 1].set_color('green')

        canvas = FigureCanvas(fig)
        toolbar = NavigationToolbar(canvas, self)
        # reference: https://stackoverflow.com/questions/55779944/how-to-remove-toolbar-buttons-from-matplotlib
        unwanted_buttons = ['Back', 'Forward']
        for x in toolbar.actions():
            if x.text() in unwanted_buttons:
                toolbar.removeAction(x)
        layout = QVBoxLayout(self)
        layout.addWidget(toolbar)
        layout.addWidget(canvas)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

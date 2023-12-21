import sys
from typing import Type, Callable
from types import TracebackType
from PyQt5 import QtWidgets
from PyQt5.QtGui import QWindow


def create_exceptions_hook(window: QWindow) -> Callable:
    def exceptions_hook(exception_type: Type[BaseException], value: BaseException,
                        traceback: TracebackType | None):
        QtWidgets.QMessageBox.critical(
            window, "Exception", str(value),
            QtWidgets.QMessageBox.Close
        )

        sys.__excepthook__(exception_type, value, traceback)
    return exceptions_hook

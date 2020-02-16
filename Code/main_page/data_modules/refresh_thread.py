from PyQt5.QtCore import QThread, pyqtSignal
import time


class RefreshThread(QThread):
    quit_thread = pyqtSignal(name='close_thread')

    def __init__(self, mainwindow, status):
        super(RefreshThread, self).__init__()
        self.mainwindow = mainwindow
        self.status = status

    def run(self):
        """Prints 'Program is running' message, so User can understand, if program is working."""
        while self.status == "start":
            self.mainwindow.progressLabel.setText("Program is running .")
            time.sleep(0.35)
            self.mainwindow.progressLabel.setText("Program is running ..")
            time.sleep(0.35)
            self.mainwindow.progressLabel.setText("Program is running ...")
            time.sleep(0.35)

    def terminate_thread(self):
        """Terminates Refresh Thread and informs User about it, printing 'Done' message."""
        self.mainwindow.progressLabel.setText("Done")
        self.terminate()

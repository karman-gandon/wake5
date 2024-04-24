import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import subprocess

class FullscreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загрузка пользовательского интерфейса из файла desktop.ui
        loadUi('desktop.ui', self)

        # Установка изображения в метке label из файла wallpaper.png
        self.label.setPixmap(QPixmap("wallpaper.png"))

        # Установка окна в полноэкранный режим
        self.showFullScreen()

        self.actionShutdown.triggered.connect(self.shutdown)
        self.actionReboot.triggered.connect(self.reboot)
        self.actionEnd_session.triggered.connect(self.close)
        self.actionLibreOffice.triggered.connect(self.open_libreoffice)
        self.actionSurface.triggered.connect(self.open_surface)
        self.actionThunar.triggered.connect(self.open_thunar)
        self.actionVLC.triggered.connect(self.open_vlc)
        self.actionBlender_3D.triggered.connect(self.open_blender)
        

    def shutdown(self):
        # Здесь можно добавить команду для завершения работы системы
        subprocess.Popen(['shutdown', 'now'])

    def reboot(self):
        # Здесь можно добавить команду для перезагрузки системы
        subprocess.Popen(['reboot'])

    def open_libreoffice(self):
        # Запуск LibreOffice в полноэкранный режим
        subprocess.Popen(['libreoffice', '--fullscreen'])

    def open_surface(self):
        # Запуск Surface
        subprocess.Popen(['python', '/wake4/surface.py'])

    def open_thunar(self):
        # Запуск Surface
        subprocess.Popen(['thunar'])

    def open_vlc(self):
        # Запуск Surface
        subprocess.Popen(['vlc'])

    def open_blender(self):
        # Запуск Surface
        subprocess.Popen(['blender'])

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FullscreenWindow()
    sys.exit(app.exec_())

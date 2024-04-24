import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        self.setCentralWidget(self.browser)

        self.showFullScreen()
        
        navtb = QToolBar()
        self.addToolBar(navtb)

        quit_btn = QAction("Quit", self)
        quit_btn.triggered.connect(self.close)
        navtb.addAction(quit_btn)

        back_btn = QAction("Назад", self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction("Вперед", self)
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("Перезагрузить", self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        # Запретить перемещение кнопок навигации и поля ввода
        navtb.setMovable(False)
        self.urlbar.setDragEnabled(False)

        self.show()

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)

        # Установка фильтра для обработки событий боковых кнопок мыши
        self.installEventFilter(self)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - wakeOS Browser" % title)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("https")
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    # Обработчик события фильтрации событий мыши
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.ForwardButton:
                self.browser.forward()
                return True
            elif event.button() == Qt.BackButton:
                self.browser.back()
                return True
        return super(MainWindow, self).eventFilter(obj, event)

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()

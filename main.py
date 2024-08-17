import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class Browser(QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()

        # Initialize the browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.browser.urlChanged.connect(self.update_url)
        self.browser.loadFinished.connect(self.update_title)
        self.showMaximized()

        # Create a layout for the top section (banner + navbar)
        top_layout = QVBoxLayout()

        # Banner with logo and name
        banner_widget = QWidget()
        banner_layout = QHBoxLayout()
        banner_widget.setLayout(banner_layout)
        banner_layout.setContentsMargins(10, 10, 10, 10)
        banner_layout.setSpacing(15)
        banner_widget.setStyleSheet("background-color: #1a1a1a;")

        # Logo
        logo = QLabel()
        logo.setPixmap(QPixmap("logo-a7-browser.png").scaled(50, 50, Qt.KeepAspectRatio))
        banner_layout.addWidget(logo)

        # Name
        name_label = QLabel("A7 Browser")
        name_label.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        banner_layout.addWidget(name_label)
        banner_layout.addStretch()

        top_layout.addWidget(banner_widget)

        # Navigation bar
        navbar = QToolBar()
        navbar.setMovable(False)
        navbar.setIconSize(QSize(32, 32))
        navbar.setStyleSheet("""
            QToolBar {
                background: #2c2c2c;
                padding: 8px;
            }
            QToolButton {
                background: #444;
                color: white;
                border: none;
                border-radius: 15px;
                padding: 12px;
                margin-right: 10px;
                font-size: 18px;
                width: 100px;
            }
            QToolButton:hover {
                background: #666;
            }
            QLineEdit {
                padding: 10px;
                border-radius: 15px;
                border: 2px solid #444;
                background-color: #333;
                color: white;
                font-size: 18px;
                margin-left: 10px;
            }
        """)
        top_layout.addWidget(navbar)

        # Create a container widget for top_layout
        top_widget = QWidget()
        top_widget.setLayout(top_layout)
        self.setMenuWidget(top_widget)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Stop button
        stop_btn = QAction('Stop', self)
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(f"{title} - A7 Browser")


app = QApplication(sys.argv)
QApplication.setApplicationName('A7 Browser')
window = Browser()
app.exec_()

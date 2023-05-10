import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize


class ManagementPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Steam 2.0")
        self.setGeometry(100, 100, 1200, 800)

        self.sample_data1 = {
            "Product1": {"status": "in review", "price": 100, "revenue": 700},
            "Product2": {"status": "accepted", "price": 200, "revenue": 800},
            "Product3": {"status": "in review", "price": 300, "revenue": 1200},
            "Product4": {"status": "accepted", "price": 400, "revenue": 400},
            "Product5": {"status": "accepted", "price": 100, "revenue": 700},
            "Product6": {"status": "in review", "price": 200, "revenue": 800},
            "Product7": {"status": "in review", "price": 300, "revenue": 1200},
            "Product8": {"status": "accepted", "price": 400, "revenue": 400},
            "Product9": {"status": "in review", "price": 400, "revenue": 400},
        }

        self.init_menu_bar()
        self.init_tool_bar()
        self.init_main_layout()


    def init_menu_bar(self):
        menu_bar = self.menuBar()

        steam_menu = menu_bar.addMenu("Steam")
        view_menu = menu_bar.addMenu("View")
        friends_menu = menu_bar.addMenu("Friends")
        games_menu = menu_bar.addMenu("Games")
        help_menu = menu_bar.addMenu("Help")

    def init_tool_bar(self):
        tool_bar = QToolBar()

        store_action = QAction("Store", self)
        store_action.triggered.connect(self.switch_to_store)

        library_action = QAction("Library", self)
        library_action.triggered.connect(self.switch_to_library)

        management_action = QAction("Management", self)
        management_action.setDisabled(True)

        tool_bar.addAction(store_action)
        tool_bar.addAction(library_action)
        tool_bar.addAction(management_action)

        self.addToolBar(tool_bar)

    def init_main_layout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        post_new_widget = QFrame()
        post_new_widget.setFrameShape(QFrame.StyledPanel)
        post_new_widget.setFrameShadow(QFrame.Raised)
        post_new_widget.setLineWidth(1)
        post_new_widget.setStyleSheet("border: 1px solid #CCCCCC;")

        post_new_layout = QHBoxLayout()
        post_new_layout.setSpacing(0)

        plus_label = QLabel("+")
        plus_label.setFont(QFont("Arial", 48))
        plus_label.setStyleSheet("color: #CCCCCC;")
        plus_label.setStyleSheet("border: 0px;")
        post_new_layout.addWidget(plus_label)

        post_new_text = QLabel("New job")
        post_new_text.setFont(QFont("Arial", 18))
        post_new_text.setStyleSheet("border: 0px;")
        post_new_layout.addWidget(post_new_text)

        post_new_widget.setLayout(post_new_layout)
        main_layout.addWidget(post_new_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        products_widget = QWidget()
        products_layout = QVBoxLayout(products_widget)

        for product_name, product_info in self.sample_data1.items():
            product_widget = self.create_product_widget(product_name, product_info)
            products_layout.addWidget(product_widget)

        scroll_area.setWidget(products_widget)
        main_layout.addWidget(scroll_area)

        self.setCentralWidget(main_widget)


    def create_product_widget(self, product_name, product_info):
        product_widget = QFrame()
        product_widget.setFrameShape(QFrame.StyledPanel)
        product_widget.setFrameShadow(QFrame.Raised)
        product_widget.setLineWidth(1)
        product_widget.setStyleSheet("border: 1px solid #CCCCCC;")

        product_layout = QHBoxLayout()

        name_and_status_layout = QVBoxLayout()
        name_label = QLabel(product_name)
        name_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px;")
        name_and_status_layout.addWidget(name_label)

        status_label = QLabel("Status: {}".format(product_info["status"]))
        status_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px;")
        name_and_status_layout.addWidget(status_label)

        price_and_revenue_layout = QVBoxLayout()
        price_label = QLabel("Price: ${}".format(product_info["price"]))
        price_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px;")
        price_and_revenue_layout.addWidget(price_label)

        revenue_label = QLabel("Revenue: ${}".format(product_info["revenue"]))
        revenue_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px;")
        price_and_revenue_layout.addWidget(revenue_label)

        raport_label = QLabel("Raport...")

        product_layout.addLayout(name_and_status_layout)
        product_layout.addStretch(1)
        product_layout.addLayout(price_and_revenue_layout)
        product_layout.addStretch(4)
        product_layout.addWidget(raport_label)
        product_widget.setLayout(product_layout)

        return product_widget


    def switch_to_store(self):
        from StorePage import StorePage

        self.store_page = StorePage()
        self.store_page.show()
        self.hide()

    def switch_to_library(self):
        from LibraryPage import LibraryPage

        self.library_page = LibraryPage()
        self.library_page.show()
        self.hide()


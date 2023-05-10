import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

#todo
def GetUserType():
    return 0

class StorePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Steam 2.0 - Store")
        self.setGeometry(100, 100, 1200, 800)

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

        user_type = GetUserType()
        
        store_action = QAction("Store", self)
        store_action.setDisabled(True)

        library_action = QAction("Library", self)
        library_action.triggered.connect(self.switch_to_library)

        management_action = QAction("Management", self)
        management_action.triggered.connect(self.switch_to_management)

        products_action = QAction("Products", self)
        products_action.triggered.connect(self.switch_to_products)

        tool_bar.addAction(store_action)
        tool_bar.addAction(library_action)
        if user_type == 0:
            tool_bar.addAction(management_action)
        else:
            tool_bar.addAction(products_action)

        self.addToolBar(tool_bar)

    def switch_to_library(self):
        from LibraryPage import LibraryPage

        self.library_page = LibraryPage()
        self.library_page.show()
        self.hide()
    
    def switch_to_management(self):
        from ManagementPage import ManagementPage

        self.management_page = ManagementPage()
        self.management_page.show()
        self.hide()

    def switch_to_products(self):
        from ProductsPage import ProductsPage

        self.products_page = ProductsPage()
        self.products_page.show()
        self.hide()

    def on_search_button_clicked(self):
        search_text = self.search_edit.text().lower()
        selected_category = self.category_combo.currentText()

        filtered_apps = [app for app in self.app_data if search_text in app["title"].lower() and app["category"] == selected_category]

        while self.apps_layout.count():
            item = self.apps_layout.takeAt(0)
            item.widget().deleteLater()

        for app in filtered_apps:
            app_widget = self.create_app_widget(app)
            self.apps_layout.addWidget(app_widget)

    def init_main_layout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        search_layout = QHBoxLayout()

        search_edit = QLineEdit()
        search_edit.setPlaceholderText("Search...")
        search_layout.addWidget(search_edit)

        search_button = QPushButton("Search")
        search_layout.addWidget(search_button)

        category_combo = QComboBox()
        category_combo.addItem("Apps")
        category_combo.addItem("Games")
        category_combo.addItem("Tools")
        search_layout.addWidget(category_combo)

        search_button.clicked.connect(self.on_search_button_clicked)
        
        main_layout.addLayout(search_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        apps_widget = QWidget()
        apps_layout = QVBoxLayout(apps_widget)
        
        app_data = [
        {
            "title": "App1",
            "image": "path/to/app1_image.png",
            "description": "This is a sample application.",
            "price": "$9.99",
            "category": "Apps"
        },
        {
            "title": "Game1",
            "image": "path/to/game1_image.png",
            "description": "This is a sample game.",
            "price": "$19.99",
            "category": "Games"
        },
        {
            "title": "App1",
            "image": "path/to/app1_image.png",
            "description": "This is a sample application.",
            "price": "$9.99",
            "category": "Apps"
        },
        {
            "title": "Game1",
            "image": "path/to/game1_image.png",
            "description": "This is a sample game.",
            "price": "$19.99",
            "category": "Games"
        },
        {
            "title": "App1",
            "image": "path/to/app1_image.png",
            "description": "This is a sample application.",
            "price": "$9.99",
            "category": "Apps"
        },
        {
            "title": "Game2",
            "image": "path/to/game1_image.png",
            "description": "This is a sample game.",
            "price": "$19.99",
            "category": "Games"
        },
        {
            "title": "App1",
            "image": "login-img.png",
            "description": "This is a sample application.",
            "price": "$9.99",
            "category": "Apps"
        },
        {
            "title": "Game3",
            "image": "path/to/game1_image.png",
            "description": "This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample gameThis is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample gameThis is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game",
            "price": "$19.99",
            "category": "Games"
        },
        ]


        for app in app_data:
            app_widget = self.create_app_widget(app)
            apps_layout.addWidget(app_widget)

        scroll_area.setWidget(apps_widget)
        main_layout.addWidget(scroll_area)

        self.setCentralWidget(main_widget)
        self.search_edit = search_edit
        self.category_combo = category_combo
        self.apps_layout = apps_layout
        self.app_data = app_data



    def create_app_widget(self, app):
        app_widget = QFrame()
        app_widget.setFrameShape(QFrame.StyledPanel)
        app_widget.setFrameShadow(QFrame.Raised)
        app_widget.setLineWidth(1)
        app_widget.setStyleSheet("border: 1px solid #CCCCCC;")

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        app_widget.setSizePolicy(size_policy)
        app_widget.setFixedHeight(100)

        app_layout = QHBoxLayout()

        title_label = QLabel(app["title"])
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px;")
        image_label = QLabel()
        image_label.setStyleSheet("border: 0px;")
        pixmap = QPixmap(app["image"])
        image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        description_label = QLabel(app["description"])
        description_label.setWordWrap(True)
        description_label.setStyleSheet("border: 0px;")

        price_label = QLabel(app["price"])
        price_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px;")

        right_arrow_button = QPushButton()
        right_arrow_icon = QPixmap("next.png")
        right_arrow_button.setIcon(QIcon(right_arrow_icon))
        right_arrow_button.setIconSize(QSize(24, 24))

        app_layout.addWidget(image_label)
        app_layout.addWidget(title_label)
        app_layout.addStretch(1)
        app_layout.addWidget(description_label)
        app_layout.addStretch(1)
        app_layout.addWidget(price_label)
        app_layout.addStretch(1)
        app_layout.addWidget(right_arrow_button)

        app_widget.setLayout(app_layout)

        return app_widget


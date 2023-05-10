import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

#todo
def GetUserType():
    return 1

class LibraryPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Steam 2.0")
        self.setGeometry(100, 100, 1200, 800)

        self.init_menu_bar()
        self.init_tool_bar()
        self.init_main_layout()
        #to do
        self.sample_data = {
            "App1": {"category": "Applications", "description": "This is a sample application. This is a sample application. This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application.This is a sample application. This is a sample application. This is a sample application.This is a sample application. This is a sample application."},
            "Game1": {"category": "Games", "description": "This is a sample game."},
            "Tool1": {"category": "Tools", "description": "This is a sample tool."},
            "App2": {"category": "Applications", "description": "This is another sample application."},
            "Game2": {"category": "Games", "description": "This is another sample game."},
        }

        self.update_items()

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
        store_action.triggered.connect(self.switch_to_store)

        library_action = QAction("Library", self)
        library_action.setDisabled(True)

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

    def init_main_layout(self):
        init_layout = QHBoxLayout()

        toolbar_layout = QVBoxLayout()
        init_layout.addLayout(toolbar_layout, 1)

        home_button = QPushButton("HOME")
        toolbar_layout.addWidget(home_button)

        category_combo = QComboBox()
        category_combo.addItem("All")
        category_combo.addItem("Applications")
        category_combo.addItem("Games")
        category_combo.addItem("Tools")
        category_combo.currentTextChanged.connect(self.update_items)
        toolbar_layout.addWidget(category_combo)

        search_edit = QLineEdit()
        search_edit.setPlaceholderText("Search...")
        search_edit.returnPressed.connect(self.update_items)
        toolbar_layout.addWidget(search_edit)

        self.item_list = QListWidget()
        self.item_list.itemClicked.connect(self.on_item_clicked)
        toolbar_layout.addWidget(self.item_list)

        self.main_content = QStackedLayout()
        init_layout.addLayout(self.main_content, 3)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_widget.setLayout(self.content_layout)

        self.main_content.addWidget(self.content_widget)

        main_widget = QWidget()
        main_widget.setLayout(init_layout)
        self.setCentralWidget(main_widget)


    def update_items(self):
        search_text = self.findChild(QLineEdit).text()
        category = self.findChild(QComboBox).currentText()

        self.item_list.clear()

        for name, data in self.sample_data.items():
            if (category == "All" or data["category"] == category) and (search_text.lower() in name.lower()):
                item = QListWidgetItem(name)
                item.setData(Qt.UserRole, data)
                self.item_list.addItem(item)

    def on_item_clicked(self, item):
        item_name = item.text()
        item_data = self.sample_data.get(item_name, {})

        old_widget = self.main_content.widget(0)
        self.main_content.removeWidget(old_widget)
        old_widget.deleteLater()

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 0, 0, 0) 
        self.content_widget.setLayout(self.content_layout)

        title_label = QLabel(item_name)
        title_label.setStyleSheet("font-weight: bold; font-size: 24px;")
        self.content_layout.addWidget(title_label)

        action_button = QPushButton("Do Something")
        self.content_layout.addWidget(action_button)

        description_label = QLabel(item_data.get("description", ""))
        description_label.setWordWrap(True)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(description_label)
        self.content_layout.addWidget(scroll_area)

        self.main_content.addWidget(self.content_widget)
    
    def switch_to_store(self):
        from StorePage import StorePage

        self.store_page = StorePage()
        self.store_page.show()
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

    def show_item_details(self, item):
        data = item.data(Qt.UserRole)
        self.content_label.setText(f"{item.text()}\n\n{data['description']}")
        self.content_label.adjustSize()

    def show_store_page(self):
        self.stack_widget.setCurrentWidget(self.store_page)

    def show_library_page(self):
        self.stack_widget.setCurrentWidget(self.library_page)
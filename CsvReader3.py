# Form implementation generated from reading ui file '.\Csvreader.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.file_path = None  # 添加file_path屬性，初始化為None
        self.limit = 5  # 添加file_path屬性，初始化為None
        self.delimiter = '\t'  # TSV文件使用tab作為分隔符
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow.resize(800, 600)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TitleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout.addWidget(self.TitleLabel, 3, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setLineWidth(1)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 3)
        self.SubmitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SubmitButton.setObjectName("SubmitButton")
        self.gridLayout.addWidget(self.SubmitButton, 3, 2, 1, 1)
        self.PreviousButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PreviousButton.setObjectName("PreviousButton")
        self.gridLayout.addWidget(self.PreviousButton, 1, 0, 1, 1)
        self.NextButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.gridLayout.addWidget(self.NextButton, 1, 2, 1, 1)
        self.ClearButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ClearButton.setObjectName("ClearButton")
        self.gridLayout.addWidget(self.ClearButton, 2, 2, 1, 1)
        self.SelectButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SelectButton.setObjectName("SelectButton")
        self.gridLayout.addWidget(self.SelectButton, 2, 1, 1, 1)
        self.InputTextBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputTextBox.sizePolicy().hasHeightForWidth())
        self.InputTextBox.setSizePolicy(sizePolicy)
        self.InputTextBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.InputTextBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.InputTextBox.setObjectName("InputTextBox")
        self.gridLayout.addWidget(self.InputTextBox, 3, 1, 1, 1)
        #self.SaveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        #self.SaveButton.setObjectName("SaveButton")
        #self.gridLayout.addWidget(self.SaveButton, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NowPageLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.NowPageLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.NowPageLabel.setObjectName("NowPageLabel")
        self.horizontalLayout.addWidget(self.NowPageLabel)
        self.TotalPageLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.TotalPageLabel.setObjectName("TotalPageLabel")
        self.horizontalLayout.addWidget(self.TotalPageLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        
        self.SelectButton.clicked.connect(self.load_csv_data)  # Connect load_csv_data method
        self.ClearButton.clicked.connect(self.clearTable)
        self.SubmitButton.clicked.connect(self.submit_handler)
        self.PreviousButton.clicked.connect(self.prevRow)
        self.NextButton.clicked.connect(self.nextRow)
        #self.SaveButton.clicked.connect(self.updateTextBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "Limit:"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.PreviousButton.setText(_translate("MainWindow", "<"))
        self.NextButton.setText(_translate("MainWindow", ">"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.SelectButton.setText(_translate("MainWindow", "Load"))
        #self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.NowPageLabel.setText(_translate("MainWindow", "NowPage"))
        self.TotalPageLabel.setText(_translate("MainWindow", "/TotalPageLabel"))

    def clearTable(self):
        model = self.tableView.model()
        if model is None:
            return
        model.removeColumns(0,model.columnCount())
        model.removeRows(0, model.rowCount())
        #self.tableView.selectionModel().selectionChanged.disconnect
    
    def load_csv_data(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Open CSV File", "", "CSV Files (*.csv);;TSV Files (*.tsv)")
        print(file_path)
        print(_)
        if file_path:
            self.file_path = file_path  # 將文件路徑設置為file_path屬性
            self.model = QtGui.QStandardItemModel()  # 將 model 定義為成員變量
            self.current_row = 1  # 初始化當前行數
            self.total_rows = 0  # 初始化總行數
            self.delimiter = '\t'  # TSV文件使用tab作為分隔符
            if file_path.endswith('.csv'):
                self.delimiter = ','  # CSV文件使用逗號作為分隔符
            with open(file_path, "r", encoding='utf-8') as file:
                line = file.readline().strip()  # 讀取第一行資料
                items = line.split(self.delimiter)
                for col_idx, item in enumerate(items):
                    self.model.setItem(0, col_idx, QtGui.QStandardItem(item))
                for i in range(self.limit):
                    line = file.readline().strip()  # 讀取第一行資料
                    if not line:
                        break  # 如果沒有更多行了，則退出迴圈
                    items = line.split(self.delimiter)
                    for col_idx, item in enumerate(items):
                        self.model.setItem(i+1, col_idx, QtGui.QStandardItem(item))
            
            with open(file_path, "r",encoding='utf-8') as file:
                for row_idx, line in enumerate(file):
                    self.total_rows += 1  # 增加總行數
            self.tableView.setModel(self.model)
            #self.tableView.selectionModel().selectionChanged.connect(self.selection_changed)
            self.updateRowCountLabel()  # 更新行數標籤

    def updateRowCountLabel(self):
        self.NowPageLabel.setText(f"{self.current_row}")
        self.TotalPageLabel.setText(f"/{self.total_rows-1}")

    def prevRow(self):
        if self.current_row > self.limit:
            self.current_row -= self.limit
            self.readAndUpdateCurrentRow()
            return
        self.current_row = 1
        self.readAndUpdateCurrentRow()
            

    def nextRow(self):
        if self.current_row + self.limit <= self.total_rows:
            self.current_row += self.limit
            self.readAndUpdateCurrentRow()

    def readAndUpdateCurrentRow(self):
        self.model.removeRows(1, self.model.rowCount() - 1)
        with open(self.file_path, "r", encoding='utf-8') as file:
            # 定位到當前行的起始位置
            start_row = self.current_row
            # 定位到當前行的結束位置
            end_row = start_row + self.limit
            if start_row==0:
                start_row+=1
                end_row+=1
            for _ in range(start_row):
                next(file)
            # 讀取self.limit行並更新模型
            for i in range(start_row, end_row):
                line = file.readline().strip()
                items = line.split(self.delimiter)
                for col_idx, item in enumerate(items):
                    # 將資料設置到模型中的正確位置
                    self.model.setItem((i - start_row)+1, col_idx, QtGui.QStandardItem(item))
        self.tableView.setModel(self.model)
        self.tableView.scrollToTop()
        self.updateRowCountLabel()

    def submit_handler(self):
        text = self.InputTextBox.toPlainText()
        self.limit=int(text)
        self.readAndUpdateCurrentRow()
        #self.TitleLabel.setText(text)
        #QtWidgets.QMessageBox.information(None, "Alert", "You clicked the button!")
        
    def updateTextBox(self):
        #indexes = selected.indexes()
        #if indexes:
        #    selected_text = indexes[0].data()
        #    self.InputTextBox.setPlainText(selected_text)
        selected_indexes = self.tableView.selectionModel().selectedIndexes()
        selected_rows = set(index.row() for index in selected_indexes)
        num_columns = self.model.columnCount()
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.clear()  # 清空剪貼板
        print(selected_rows)
        for row in selected_rows:
            print(row)
            row_data = [self.model.data(self.model.index(row, col)) for col in range(num_columns)]
            print(row_data)
        #clipboard.setText(self.delimiter.join(row_data))  # 將選中的行數據以TSV格式複製到剪貼板

    def selection_changed(self, selected, deselected):
        selected_indexes = selected.indexes()
        selected_data = []
        for index in selected_indexes:
            row = index.row()
            column = index.column()
            item = self.model.item(row, column)
            if item is not None:
                selected_data.append(item.text())
        print(selected_data)
        # 将选定的数据转换为字符串，并将其写入剪贴板
        selected_text = self.delimiter.join(selected_data)
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.clear()  # 清空剪貼板
        clipboard.setText(selected_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

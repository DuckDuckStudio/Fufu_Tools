# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME main
AUTHOR Pfolg
TIME 2025/6/14 16:57
"""
import os
import sys
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QListView,
    QAbstractItemView,
    QFileDialog,
    QMessageBox,
)

# 相关链接
"https://github.com/Pfolg/PfolgBlog/blob/master/Passages/%E5%AF%B9%E6%AF%94%E6%96%87%E4%BB%B6%E6%B8%85%E7%90%86/main.md"


def get_screen_info() -> tuple:
    """读取屏幕长宽，用于窗口定位"""
    # 获取现有的 QApplication 实例
    _app = QApplication.instance()
    if _app is not None:
        # 获取显示器数据
        screen = _app.primaryScreen().geometry()
        # 返回长宽
        return screen.width(), screen.height()
    else:
        return 800, 600


def get_out_repeat_element(a: list) -> list:
    """去重"""
    return list(set(a))


def read_folders_files(data: list):
    """读取文件夹内的所有文件，不包含子目录中的文件"""
    all_files = []
    for i in data:
        current_dir = Path(i)
        if Path.exists(current_dir):
            all_items = current_dir.iterdir()
            # 过滤出文件（排除文件夹）
            for item in all_items:
                if item.is_file():
                    all_files.append(item)
    print(all_files)
    return all_files


class Window(QWidget):
    """主窗口"""

    def __init__(self):
        super().__init__()
        # 加载UI到类
        QUiLoader().load(ui_path, self)
        # 缓存文件夹
        self.folders = []
        # 缓存文本/代码文件
        self.files = []
        # 缓存将删除的文件
        self.delete_files = []
        # 子线程
        self.timer = QTimer()

        # 列表所需模型
        self.model1 = QStandardItemModel()
        self.model2 = QStandardItemModel()
        self.model3 = QStandardItemModel()
        # 引用
        self.global_label1: QLabel = self.findChild(QLabel, "label")
        self.global_label2: QLabel = self.findChild(QLabel, "label_2")
        self.global_label3: QLabel = self.findChild(QLabel, "label_3")

        self.func1_btn1: QPushButton = self.findChild(QPushButton, "pushButton")
        self.func1_btn2: QPushButton = self.findChild(QPushButton, "pushButton_2")
        self.func1_btn3: QPushButton = self.findChild(QPushButton, "pushButton_3")
        self.func2_btn1: QPushButton = self.findChild(QPushButton, "pushButton_4")
        self.func2_btn2: QPushButton = self.findChild(QPushButton, "pushButton_5")
        self.func2_btn3: QPushButton = self.findChild(QPushButton, "pushButton_6")
        self.func3_btn1: QPushButton = self.findChild(QPushButton, "pushButton_7")
        self.func3_btn2: QPushButton = self.findChild(QPushButton, "pushButton_8")
        self.func3_btn3: QPushButton = self.findChild(QPushButton, "pushButton_9")
        self.func3_btn4: QPushButton = self.findChild(QPushButton, "pushButton_10")

        self.listView1: QListView = self.findChild(QListView, "listView")
        self.listView2: QListView = self.findChild(QListView, "listView_2")
        self.listView3: QListView = self.findChild(QListView, "listView_3")

        self.global_label3.hide()
        self.init()

    def remove_files(self):
        """删除待删区文件"""
        if self.delete_files:
            # 确认
            if (
                QMessageBox.question(
                    self,
                    "Confirm",
                    "确认删除吗？",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Cancel,
                )
                == QMessageBox.StandardButton.Ok
            ):  # 同意则删除，不同意则取消
                for i in self.delete_files:
                    Path.unlink(Path(i))
                self.delete_files.clear()
                self.update_listView()
                msg = "清理完毕！"
            else:
                return
        else:
            msg = "无可清理文件！"

        QMessageBox.information(self, "Tip", msg, QMessageBox.StandardButton.Ok)

    def start_remove(self):
        """删除待删区文件"""
        if self.timer.isActive():
            self.timer.stop()
        self.timer = QTimer()
        # 绑定清理
        self.timer.timeout.connect(self.remove_files)
        # 运行一次
        self.timer.setSingleShot(True)
        self.timer.start()

    def start_compare(self):
        """执行筛选"""
        # 如果该线程存活则kill后再创建
        if self.timer.isActive():
            self.timer.stop()
        self.timer = QTimer()
        # 绑定比较
        self.timer.timeout.connect(self.compare_content)
        # 只运行一次
        self.timer.setSingleShot(True)
        # 启动
        self.timer.start()

    def compare_content(self):
        """[核心] 将文件夹中的文件(a)与文本/代码中的内容(b)比较。如果a存在于b中，则保留，否则添加到待删除区"""
        _msg = ""
        if self.folders and self.files:
            # 清除上次筛选的文件，避免本次文件的误删
            self.delete_files.clear()
            # 读取被引用文件列表
            all_files: list[Path] = read_folders_files(self.folders)
            # ------- by DeepSeek
            # 存储所有输入文件的内容
            all_content = ""
            for file_path in self.files:
                if Path(file_path).exists():
                    with open(file_path, "r", encoding="utf-8") as f:
                        all_content += f.read()  # 合并所有文件内容

            # 收集所有需要匹配的文件名（使用集合去重）
            target_names = {file.name for file in all_files}

            # 检查哪些文件名出现在内容中
            matched_names = set()
            for name in target_names:
                if name in all_content:  # 在合并内容中查找
                    matched_names.add(name)

            # 构建绿色文件列表
            green_files = {file for file in all_files if file.name in matched_names}

            # 生成待删除文件列表
            self.delete_files = [
                str(file)
                for file in all_files
                if file not in green_files and file.exists()
            ]
            # ------
            print(self.delete_files)
            self.update_listView()
            msg = "筛选完毕！"
            if not self.delete_files:
                msg = "筛选完毕，无未使用文件！"
            QMessageBox.information(self, "Tip", msg, QMessageBox.StandardButton.Ok)
        elif not self.folders:
            _msg = "请选择文件夹！"
        else:
            _msg = "请选择目标文件！"
        if _msg:
            QMessageBox.warning(self, "Warning", _msg)

    def remove_selected(self, list_view: QListView, model: QStandardItemModel) -> None:
        """移除所有选中项（支持多选）"""
        # 获取选中项的索引（按行号降序排序）
        selected_indexes = sorted(
            [index.row() for index in list_view.selectedIndexes()], reverse=True
        )
        # 从后向前移除避免索引变化导致错误
        for row in selected_indexes:
            item = model.item(row).text()
            model.removeRow(row)
            if model == self.model1:
                self.folders.remove(item)
                print("文件夹：", self.folders)
            elif model == self.model2:
                self.files.remove(item)
                print("文件：", self.files)
            elif model == self.model3:
                self.delete_files.remove(item)
                print("欲删除文件：", self.delete_files)

    def clear_listView(self, target: int) -> None:
        """清除三个表格的数据"""
        if target == 1:
            self.model1.clear()
            self.folders.clear()
        elif target == 2:
            self.model2.clear()
            self.files.clear()
        elif target == 3:
            self.model3.clear()
            self.delete_files.clear()

    def bind_functions(self):
        """按钮功能绑定"""
        self.func1_btn1.clicked.connect(self.select_folder)  # 选择文件夹
        self.func1_btn2.clicked.connect(
            lambda: self.remove_selected(self.listView1, self.model1)
        )  # 清除选中
        self.func1_btn3.clicked.connect(lambda: self.clear_listView(1))  # 清除列表1

        self.func2_btn1.clicked.connect(self.select_files)  # 选择文件
        self.func2_btn2.clicked.connect(
            lambda: self.remove_selected(self.listView2, self.model2)
        )  # 清除选中
        self.func2_btn3.clicked.connect(lambda: self.clear_listView(2))  # 清除列表2

        self.func3_btn1.clicked.connect(self.start_compare)  # 比较
        self.func3_btn2.clicked.connect(
            lambda: self.remove_selected(self.listView3, self.model3)
        )  # 清除选中
        self.func3_btn3.clicked.connect(lambda: self.clear_listView(3))  # 清除列表3
        self.func3_btn4.clicked.connect(self.start_remove)  # 删除文件

    def update_listView(self):
        """更新三个表格中的数据"""
        # 清除模型数据
        self.model1.clear()
        self.model2.clear()
        self.model3.clear()
        if self.folders:
            for i in self.folders:
                self.model1.appendRow(QStandardItem(i))
        if self.files:
            for i in self.files:
                self.model2.appendRow(QStandardItem(i))
        if self.delete_files:
            for i in self.delete_files:
                self.model3.appendRow(QStandardItem(i))

    def select_folder(self):
        """获取文件夹"""
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.Directory)
        fd.setViewMode(QFileDialog.ViewMode.List)
        if fd.exec():
            a: list[str] = fd.selectedFiles()
            print(a)
            # 将数据加载到类变量
            self.folders += a
            # 去重
            self.folders = get_out_repeat_element(self.folders)
            self.update_listView()

    def select_files(self):
        """选择文件"""
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 获取已存在的文件
        fd.setViewMode(QFileDialog.ViewMode.List)  # 列表视图
        if fd.exec():
            a: list[str] = fd.selectedFiles()
            print(a)
            # 将数据加载到类变量
            self.files += a
            self.files = get_out_repeat_element(self.files)
            self.update_listView()

    def init(self):
        """初始化窗口"""
        w, h = get_screen_info()
        self.setGeometry(int((w - 800) / 2), int((h - 600) / 2), 800, 600)
        self.setMaximumSize(800, 600)
        self.setWindowTitle("对比清理")
        self.listView1.setModel(self.model1)
        self.listView2.setModel(self.model2)
        self.listView3.setModel(self.model3)
        for i in [self.listView1, self.listView2, self.listView3]:
            i.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            i.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.bind_functions()


if __name__ == '__main__':
    # 获取当前路径
    script_dir = Path(sys.argv[0]).resolve().parent
    print(script_dir)
    # ui文件路径
    ui_path = os.path.join(script_dir, "main.ui")
    # 图片使用根目录的图标
    icon_path = "ico.ico"
    # 创建应用
    app = QApplication(sys.argv)
    # 设定图标
    app.setWindowIcon(QIcon(icon_path))
    # 创建界面
    window = Window()
    window.show()
    sys.exit(app.exec())

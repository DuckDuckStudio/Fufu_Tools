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
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListView, QAbstractItemView, QFileDialog, \
    QMessageBox

# 打包命令 将依赖文件直接嵌入到exe中
"""pyinstaller --onefile --windowed --add-data "main.ui;." --add-data "ico.ico;." main.pyw"""
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
    # 返回去重的结果，可能没必要
    return get_out_repeat_element(all_files)


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

        self.f1_b1: QPushButton = self.findChild(QPushButton, "pushButton")
        self.f1_b2: QPushButton = self.findChild(QPushButton, "pushButton_2")
        self.f1_b3: QPushButton = self.findChild(QPushButton, "pushButton_3")
        self.f2_b1: QPushButton = self.findChild(QPushButton, "pushButton_4")
        self.f2_b2: QPushButton = self.findChild(QPushButton, "pushButton_5")
        self.f2_b3: QPushButton = self.findChild(QPushButton, "pushButton_6")
        self.f3_b1: QPushButton = self.findChild(QPushButton, "pushButton_7")
        self.f3_b2: QPushButton = self.findChild(QPushButton, "pushButton_8")
        self.f3_b3: QPushButton = self.findChild(QPushButton, "pushButton_9")
        self.f3_b4: QPushButton = self.findChild(QPushButton, "pushButton_10")

        self.lv1: QListView = self.findChild(QListView, "listView")
        self.lv2: QListView = self.findChild(QListView, "listView_2")
        self.lv3: QListView = self.findChild(QListView, "listView_3")

        self.global_label3.hide()
        self.init()

    def remove_files(self):
        """删除待删区文件"""
        if self.delete_files:
            # 确认
            if QMessageBox.question(
                    self, "Confirm",
                    "确认删除吗？",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Cancel
            ) == QMessageBox.StandardButton.Ok:  # 同意则删除，不同意则取消
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
            file_content = []
            green_files = []
            # 读取文件s内容
            for i in self.files:
                with open(i, "r", encoding="utf-8") as file:
                    file_content.append(file.read())
            # 读取被引用文件列表
            all_files: list[Path] = read_folders_files(self.folders)
            for i in all_files:
                for j in file_content:
                    # [核心] 比对：存在则保留，不存在则继续比较，直到找到或用尽循环
                    if i.name in j:
                        # 将文件添加到绿色区
                        green_files.append(i)
                        # 退出二级循环
                        break
            for i in all_files:
                if i not in green_files and Path.exists(i):
                    self.delete_files.append(str(i))
            self.delete_files = get_out_repeat_element(self.delete_files)
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
            [index.row() for index in list_view.selectedIndexes()],
            reverse=True
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
        """清除新三个表格的数据"""
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
        self.f1_b1.clicked.connect(self.select_folder)
        self.f1_b2.clicked.connect(lambda: self.remove_selected(self.lv1, self.model1))
        self.f1_b3.clicked.connect(lambda: self.clear_listView(1))

        self.f2_b1.clicked.connect(self.select_files)
        self.f2_b2.clicked.connect(lambda: self.remove_selected(self.lv2, self.model2))
        self.f2_b3.clicked.connect(lambda: self.clear_listView(2))

        self.f3_b1.clicked.connect(self.start_compare)
        self.f3_b2.clicked.connect(lambda: self.remove_selected(self.lv3, self.model3))
        self.f3_b3.clicked.connect(lambda: self.clear_listView(3))
        self.f3_b4.clicked.connect(self.start_remove)

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
            self.files += a
            self.files = get_out_repeat_element(self.files)
            self.update_listView()

    def init(self):
        """初始化窗口"""
        w, h = get_screen_info()
        self.setGeometry(int((w - 800) / 2), int((h - 600) / 2), 800, 600)
        self.setMaximumSize(800, 600)
        self.setWindowTitle("对比清理")
        self.lv1.setModel(self.model1)
        self.lv2.setModel(self.model2)
        self.lv3.setModel(self.model3)
        for i in [self.lv1, self.lv2, self.lv3]:
            i.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            i.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.bind_functions()


if __name__ == '__main__':
    # 获取当前路径
    script_dir = Path(sys.argv[0]).resolve().parent
    print(script_dir)
    ui_path = os.path.join(script_dir, "main.ui")
    icon_path = "ico.ico"
    # 创建应用
    app = QApplication(sys.argv)
    # 设定图标
    app.setWindowIcon(QIcon(icon_path))
    # 创建界面
    window = Window()
    window.show()
    sys.exit(app.exec())

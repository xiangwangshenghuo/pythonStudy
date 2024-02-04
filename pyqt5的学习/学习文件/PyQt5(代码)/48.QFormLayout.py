from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 标签关联一个控件(&n)
        name_label = QLabel('姓名(&n)：')
        age_label = QLabel('年龄(&g):')
        name_le = QLineEdit()
        age_sb = QSpinBox()
        # 标签关联一个控件的方法
        name_label.setBuddy(name_le)
        age_label.setBuddy(age_sb)

        submit_btn = QPushButton('提交')

        sex_label = QLabel('性别')
        male_rb = QRadioButton("男")
        female_rb = QRadioButton("女")
        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        # 1. 创建布局管理器
        layout = QFormLayout()
        # 2. 把布局管理器赋值为需要布局的父控件
        self.setLayout(layout)
        # 3. 把需要布局的子控件交给布局管理器进行布局
        # layout.addWidget(name_label)
        # layout.addWidget(name_le)
        # 添加行
        # 行中两个控件
        layout.addRow(name_label, name_le)

        layout.addRow(age_label, age_sb)
        # 行中一个控件
        layout.addRow(submit_btn)
        # 行中一个控件一个布局
        layout.addRow(sex_label, h_layout)
        # 行中文本+一个布局或者控件
        psd_le = QLineEdit()
        layout.addRow('密码：', psd_le)
        # 二。插入行
        reg_btn = QPushButton('注册')
        layout.insertRow(1,'注册', reg_btn)
        # 三，获取行的信息
        # 行数
        print(layout.rowCount())
        # 获取控件的位置信息（行数索引,列数索引）
        print(layout.getWidgetPosition(age_sb))
        # 获取布局信息
        print(layout.getLayoutPosition(h_layout))
        # 获取布局中的子控件的位置：会找不到的
        print(layout.getWidgetPosition(male_rb))
        # 四。修改行:根据行号和角色，设置相关控件或布局，如果有必要会延长布局

        height_lb = QLabel('身高')
        height_le = QLineEdit()
        # 行号，角色是左边还是右边（第一列还是第二列 ->0,1）
        # 如果单元格已被占用，则不会设置成功
        # layout.setWidget(0, QFormLayout.LabelRole, height_lb)
        # layout.setWidget(0, QFormLayout.FieldRole, height_le)
        layout.setWidget(6, QFormLayout.FieldRole, height_le)

        # 五。删除和移出行
        height_le.destroyed.connect(lambda :print('释放'))
        # 删除行，删除子控件
        # layout.removeRow(2)
        # layout.removeRow(name_le) # 删除namele所在的整行
        # 删除控件
        # layout.removeWidget(age_label)
        # 移出行，但是不删除控件，需要亲自隐藏或者删除，要不布局就乱了
        # layout.takeRow(2)
        # 获取移出行中对应的子控件
        # layout.takeRow(2).labelItem.widget().hide()
        # layout.takeRow(2).fieldItem.widget().hide()
        # 六、获取标签对象（控件）不生效
        print(layout.labelForField(sex_label))
        sex_label.setText('xxx' * 10)
        # 七、行的包装策略:三种
        # QFormLayout.DontWrapRows 字段总是放在标签旁边。
        # QFormLayout.WrapLongRows标签被赋予足够的水平空间以适合最宽的标签，其余的空间被赋予字段。 如果字段的最小大小比可用空间宽，则该字段将换行到下一行
        # QFormLayout.WrapAlIRows字段总是位于其标签下方。
        layout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        # 八、对齐方式
        # 布局对齐方式
        print(layout.formAlignment() == Qt.AlignLeft | Qt.AlignTop)
        # 设置对齐方式
        layout.setFormAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # 标签对齐方式
        layout.setLabelAlignment(Qt.AlignRight)
        # 间距
        # 垂直间距
        layout.setVerticalSpacing(60)
        # 水平间距
        layout.setHorizontalSpacing(60)
        # 九、字段增长策略
        # setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy)
        # fieldGrowthPolicy0 -> QFormLayout.FieldGrowthPolicy
        # QFormLayout.Fie dsStayAtSizeHint 永远不会超出其有效大小的提示。这是QMacStyle的默认值。
        # 补充
        # QFormLayout.ExpandingFieldsGrow
        # 水平大小策略为Expanding或MinimumExpanding的字段将增长以填充
        # QFormLayout.AllNonFixedFieldsGrow
        # 具有允许它们增长的大小策略的所有字段将增长以填充可用空间。这




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())
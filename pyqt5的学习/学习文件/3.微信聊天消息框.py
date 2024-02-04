import time
import requests
from PIL import Image
from PyQt5.Qt import *
import os
import
#定义一个QTextEdit的派生类消息框
class ChatTextEdit(QTextEdit):
    def _init__(self, link_=False, *args, **kwargs):
        super(ChatTextEdit, self).__init__(*args, **kwargs)
    #在拖动操作期间，需要确定是否可以接受拖放操作时调用
    def canInsertFromMimeData(self, source) -> bool:
        return super(ChatTextEdit, self).canInsertFromMimeData(source)
    #每当作为剪贴板粘贴操作的结果插入文本时，或者当文本编辑接受来自拖放操作的数据时，
    def insertFromMimeData(self, source) -> None:
        #若剪贴板中的数据为hasImage，则进行保存至本地
        if source.hasImage():
            self.copy_html_image(source. imageData())
        elif source.hasUrls():
            for url in source.urls():
                pass

    # hasImage形式的网络图片的保存
    def copy_html_image(self, image: QImage):
        if not os.path.exists('%s/data_file' % (os.path.dirname(__file__))):
            os.mkdir('%s/data_file' % (os.path.dirname(__file__)))

        save_path = "%s/data_file/%d.jpg" % (os.path.dirname(__file__), int(time.time()))
        image.save(save_path)
        show_img = QTextImageFormat()
        show_img.setName(save_path)
        # 设定指定显示高度
        show_img.setHeight(150)
        show_img.setWidth(image.width() / (image.width() / 150))
        self.textCursor().insertImage(show_img)

    # 每当作为剪贴板粘贴操作的结果插入文本时，或者当文本编辑接受来自拖放操作的数据时，
    def insertFromMimeData(self, source):

        # 若剪贴板中的数据为hasImage，则进行保存至本地
        if source.hasImage():
            self.copy_html_image(source.imageData())
        # 若为url形式
        elif source.hasUrls():
            for url in source.urls():
                file_info = QFileInfo(url.toLocalFile())
                ext = file_info.suffix().lower()
                # 判断是否为本地图片
                if ext in QImageReader.supportedImageFormats():
                    self.insert_local_image(QImage(file_info.filePath()),url)
                    # 若为网络图片url
                elif url.url()[0:4] == "http":
                    # 访问url，获取响应体
                    response = requests.get(url.ur1())
                    # 转化为Image类型
                    image = Image.open(BytesI0(response.content))
                    self.copy_html_image(ImageQt.ImageQt(image))
                else:
                    self.insert_file(url)
            else:
                super(ChatTextEdit, self).insertFromMimeData(source)


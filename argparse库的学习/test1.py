# 首先，我们需要导入argparse模块：

import argparse
# 然后创建ArgumentParser对象，用于定义命令行参数：
# prog ：程序的名称（默认：sys.argv[0]）
# usage ：描述程序用途的字符串（默认值：从添加到解析器的参数生成）
# description ：在参数帮助文档之前显示的文本（默认值：无）
# epilog ：在帮助文档之后显示的文本（默认值：无）
# parents ：一个ArgumentParser对象的列表，它们的参数也应包含在内
# formatter_class ：用于自定义帮助文档输出格式的类
# prefix_chars ：可选参数的前缀字符集合（默认值：'-‘）
# fromfile_prefix_chars ：当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None）
# argument_default ：参数的全局默认值（默认值：None）
# conflict_handler ：解决冲突选项的策略（通常是不必要的）
# add_help ：为解析器添加一个 -h/-help 选项（默认值：True）
# allow_abbrev ：如果缩写是无歧义的，则允许缩写长选项（默认值：True）
# ————————————————
# 版权声明：本文为CSDN博主「Merlin_CAE」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43555555/article/details/129143847
parser = argparse.ArgumentParser(description='命令行工具的描述信息')
# 接下来可以使用 add_argument() 方法添加命令行参数：
# 其中，第一个参数是参数名，第二个参数是帮助信息。如果参数是可选的，我们可以使用--开头的长选项，例如--count。如果参数是布尔类型的，我们可以使用action='store_true'，例如--verbose,命令行直接写该参数就表示为True，不写就是False。
parser.add_argument('filename', help='文件名')
parser.add_argument('--count', type=int, default=1, help='重复次数')
parser.add_argument('--verbose', action='store_true', help='详细输出')
# 最后，使用 parse_args() 方法解析命令行参数：这个方法会返回一个对象，其中包含了所有解析出来的参数。
args = parser.parse_args()
# 我们可以通过属性名来访问这些参数。可以使用 args. 参数名的方式获取命令行参数的值：
print(args.filename)
print(args.count)
print(args.verbose)

# 根据命令行输入的内容进行操作，实例如下：
for i in range(args.count):
    print(args.filename)

if args.verbose:
    print('完成')

# 不能再pycharm中运行该命令，必须在命令行中执行该脚本，可以输入命令行参数，例如：
#
# python test1.py file.txt --count 3 --verbose
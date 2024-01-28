# 我们可以编写一个 git 命令行工具，它有多个子命令，如 add、commit、push 等。我们可以使用 add_subparsers 方法来添加子命令，并在每个子命令中添加自己的参数。
import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Git 命令行工具')

# 添加子命令
subparsers = parser.add_subparsers(dest='command', help='子命令')
subparsers.required = True

# add 子命令
add_parser = subparsers.add_parser('add', help='添加文件')
add_parser.add_argument('file', help='文件名')
add_args = add_parser.parse_args()

# commit 子命令
commit_parser = subparsers.add_parser('commit', help='提交代码')
commit_parser.add_argument('-m', '--message', help='提交信息')

# push 子命令
push_parser = subparsers.add_parser('push', help='推送代码')
push_parser.add_argument('-f', '--force', action='store_true', help='强制推送')

print(add_args.file)
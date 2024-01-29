import string
dir(string)
# ['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__built
# ins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__packag
# e__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_u
# ppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctua
# tion', 'whitespace']
string.ascii_lowercase  #所有的小写字母
'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase  #所有的大写字母
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.hexdigits        #所有的十六进制字符
'0123456789abcdefABCDEF'
string.whitespace       #所有的空白字符
' \t\n\r\x0b\x0c'
string.punctuation      #所有的标点字符
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
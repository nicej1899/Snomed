import urllib.request
import urllib.parse
import json
from  iCIBA import iciba
from youdao import youdao
from google import *
from fy import fanyi
txt=input("请输入翻译目标")

print(youdao(txt))
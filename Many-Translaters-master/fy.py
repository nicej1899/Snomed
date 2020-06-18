import urllib.request
import urllib.parse
import json
def fanyi(txt):


                if txt == '0':
                        print("请正确输入")

                else:
                        url = 'http://fanyi.so.com/index/search'

                        data = {
                        'query':txt,
                        'eng':'0'
                        }

                        data = urllib.parse.urlencode(data).encode('utf - 8')
                        wy = urllib.request.urlopen(url,data)
                        html = wy.read().decode('utf - 8')
                        ta = json.loads(html)
                        print("360翻译结果"+ta['data']['fanyi'])



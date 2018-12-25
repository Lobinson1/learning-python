
import util.http

print('begin to get sina.html')
# 构建请求头信息
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url = 'https://www.sina.com.cn'
# 构建请求
res = util.http.send_get(url)
# req = request.Request(url=url, headers=header_dict)
# res = request.urlopen(req)
# res = res.read()
f = open('D:/sina.html', 'wb')
f.write(res)
f.close()
print('success!')

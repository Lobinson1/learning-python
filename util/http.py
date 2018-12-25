from urllib import parse, request


# 定义一个GET请求方法
def send_get(url, header=None, params=None):
    if params is None:
        params = {}
    if header is None:
        header = {}
    # 定义头信息
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    header = header if header.__sizeof__() > 0 else header_dict
    param = parse.urlencode(params) if params.__sizeof__() > 0 else ''
    # 构建请求
    req = request.Request(url='%s%s%s' % (url, '?', param), headers=header)
    res = request.urlopen(req)
    res = res.read()
    return res

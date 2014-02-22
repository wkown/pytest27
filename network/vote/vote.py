__author__ = 'weijie'
# -*- coding: utf-8 -*-
__author__ = 'weijie'
import urllib
import urllib2
import cookielib
import bs4
import re


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance


class Browser:
    """模拟浏览器"""
    __metaclass__ = Singleton

    def __init__(self, charset='utf-8'):
        self.charset = charset
        #'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        self.userAgent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116'
        self.cookiejar = cookielib.CookieJar()
        self.urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookiejar))
        self.urlOpener.addheaders = [('User-agent', self.userAgent)]
        urllib2.install_opener(self.urlOpener)

        self.currentUrl = None
        self.currentResponse = None
        self.protocol = 'http'
        self.rootUrl = None
        self.host = None
        #当前页面中的表单
        self.forms = None
        self.selectedForm = None

        self.proxy = None

    def setProxy(self, proxy='127.0.0.1:8087'):
        """设置http代理,address:port"""
        self.proxy = urllib2.ProxyHandler({'http': proxy})
        self.urlOpener.add_handler(self.proxy)

    def submitForm(self, url=None, fields={}, headers={}):
        """提交一个表单,并返回服务器的相应页面"""
        if url is None:
            return
        url = self.perfectUrl(url)

        if self.selectedForm is None:
            return False
        for k, v in fields.items():
            self.selectedForm['fields'][k] = v
        if self.selectedForm['action'] is None or self.selectedForm['action'] == '':
            self.selectedForm['action'] = url
        self.selectedForm['action'] = self.perfectUrl(self.selectedForm['action'])
        for k, v in self.selectedForm['fields'].items():
            if v is not None and isinstance(v, unicode):
                self.selectedForm['fields'][k] = v.encode(self.charset)
        if self.selectedForm['method'] is None or self.selectedForm['method'].lower() == 'get':
            req = urllib2.Request(self.selectedForm['action'] + '?' + self.urlencode(self.selectedForm['fields']))
        else:
            req = urllib2.Request(self.selectedForm['action'], self.urlencode(self.selectedForm['fields']))
        for k, v in headers.items():
            req.add_header(k, v)
        self.currentResponse = self.urlOpener.open(req).read()
        return self.currentResponse

    def createForm(self, url, fieds, method='post'):
        """创建表单"""
        self.selectedForm = {
            'action': url,
            'method': method,
            'fields': fieds
        }

    def selectForm(self, url=None, id=None, name=None, nr=None):
        """
        获取表单，得到结构如{'action':'http://xxx.com/login','method':'post’，'fields':{}}的字典。
        """
        if url is None:
            return
        html = self.read(url, True)
        soup = bs4.BeautifulSoup(html)
        if id is not None or name is not None:
            attrs = None
            if id is not None:
                attrs = {'id': id}
            elif name is not None:
                attrs = {'name': name}
            form = soup.find('form', attrs)
        elif nr is not None:
            forms = soup.findAll('form')
            i = 1
            for form in forms:
                if i == nr:
                    break
                i += 1
        self.selectedForm = self.formateForm(form)

    def formateForm(self, form):
        """
        :param form: bs4.element.Tag()
        分析form元素并返回，得到结构如{'action':'http://xxx.com/login','method':'post’，'fields':{}}的字典。
        """
        value = {
            'action': form.get('action'),
            'method': form.get('method'),
            'fields': {}
        }
        for tag in form.findAll('input'):
            if tag.get('name') is not None:
                value['fields'][tag.get('name')] = tag.get('value')
        for tag in form.findAll('textarea'):
            if tag.get('name') is not None:
                value['fields'][tag.get('name')] = tag.string
        for tag in form.findAll('select'):
            if tag.get('name') is not None:
                selected = None
                for option in tag.findAll('option'):
                    if selected is None:
                        selected = option.get('value')
                    if option.get('selected') is not None:
                        selected = option.get('value')
                        break
                value['fields'][tag.get('name')] = selected
        return value

    def requestAjaxData(self,url,data,referer=None,**headers):
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        req.add_header('X-Requested-With','XMLHttpRequest')
        req.add_header('User-Agent', self.userAgent)
        if referer:
            req.add_header('Referer',referer)
        if headers:
            for k in headers.keys():
                req.add_header(k,headers[k])
        params = self.urlencode(data)
        response = urllib2.urlopen(req, params)
        jsonText = response.read()
        return jsonText

    def request(self, url, data=None, method='get'):
        """创建请求,根据method指定的请求方式生成请求对象"""
        if method is None or method.lower() == 'get':
            if data is not None:
                url += '?' + self.urlencode(data)
            return urllib2.Request(url)
        return urllib2.Request(url, self.urlencode(data))

    def getRootUrl(self, url):
        """
        返回url中的根目录
        """
        match = self._analysisUrl(url)
        if match is None:
            return None
        return match[0]

    def urlencode(self, query, doseq=0):
        return urllib.urlencode(query, doseq)

    def urldecode(self, query):
        return urllib.unquote(query)

    def perfectUrl(self, route):
        """
        完善url，将url路由补全成'http://xxx.yyy.com/route'的样式
        """
        if route is None:
            return None
        if not (route.find('http://') > -1 or route.find('https://') > -1):
            if route.find('/') == 0:
                route = self.rootUrl + route
            else:   #所有不是以“/”开头的（“./”“../”）自动补全
                route = self.rootUrl + '/' + route

        return route

    def _analysisUrl(self, url):
        """
        分析url中的数据并返回匹配的元组：('http[s]://xxx.yyy.com','http[s]','xxx.yyy.com')
        """
        try:
            patten = re.compile('((http|https)://(.*?))/.*?', re.IGNORECASE)
            match = patten.match(url).groups()
        except:
            try:
                patten = re.compile('((http|https)://(.*))', re.IGNORECASE)
                match = patten.match(url).groups()
            except:
                return None
        return match
    def read(self, url, refresh=False):
        """读取一个网页内容"""
        url = self.perfectUrl(url)

        if self.currentUrl != url or refresh is True:
            self.currentUrl = url

            if  self.rootUrl is None or url.find(self.rootUrl) == -1:
                urlMatch = self._analysisUrl(url)
                self.rootUrl = urlMatch[0]
                self.protocol = urlMatch[1]
                self.host = urlMatch[2]

            if isinstance(self.urlOpener, urllib2.OpenerDirector):
                self.currentResponse = self.urlOpener.open(self.request(url)).read()
            else:
                self.currentResponse = urllib2.urlopen(url).read()
        return self.currentResponse

if __name__ == '__main__':
    import time
    br = Browser()
    br.setProxy()
    url1 = 'http://app.cpd.com.cn/application/index.php/fzjvote/votethis?' \
          'json=jQuery172005017485886175421_1385445016746&cid=20094276&_=1385445084326'
    url2 = 'http://app.cpd.com.cn/application/index.php/fzjvote/votethis?' \
           'json=jQuery172005017485886175421_1385445016747&cid=20097046&_=1385445146066'
    count = 1
    while True:
        print count, ':url1:', br.read(url1, True)
        time.sleep(3)
        print count, ':url2:', br.read(url2, True)
        count += 1
        time.sleep(3)

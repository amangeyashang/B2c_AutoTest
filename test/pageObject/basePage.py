# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2019/12/3 15:36'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """
    BasePage封装所有页面都用公共的方法，例如driver,url,findElement等
    """
    #初始化driver，url，pagetile等
    #实例化BasePage类时，最先执行的就是_init_方法，该方法的入参，其实就是BasePage类的入参。
    #_init_方法不能有返回值，只能返回None
    #self只实例本身，相较于类page而言。
    def __init__(self,selenium_driver,base_url,pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    #通过title断言进入的页面是否正确
    #使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    #打开页面，并检验页面链接是否加载正确
    #以单下划线_开头的方法，在使用import时，该方法不会导入，保证该方法为类私有的
    def _open(self,url,pagetitle):
        #使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maxmize_window()
        #使用assert进行校验，打开窗口title是否与配置的title一致，调用on_page()方法
        assert self.on_page(pagetitle),u"打开页面失败 %s"%url

    #定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url,self.pagetitle)


# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/20 14:25'

import configparser
from config.conf import cm

vendor = 'VENDOR'
account = 'ACCOUNT'
password = 'PASSWORD'
vendorName = 'VENDORNAME'
vendorCode = 'VENDORCODE'
shopKeeper = 'SHOPKEEPER'
shopAddress = 'SHOPADDRESS'
mobileNumber = 'MOBILENUMBER'
identityCard = 'IDNO'

class ReadConfig(object):
    """配置文件"""

    def __init__(self):
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(vendor, vendor)

    def user(self):
        return self._get(account, account)

    def pwd(self):
        return self._get(password, password)

    def vendorName(self):
        return self._get(vendorName, vendorName)

    def vendorCode(self):
        return self._get(vendorCode, vendorCode)

    def shopKeeper(self):
        return self._get(shopKeeper, shopKeeper)

    def shopAddress(self):
        return self._get(shopAddress, shopAddress)

    def mobileNumber(self):
        return self._get(mobileNumber, mobileNumber)

    def identityCard(self):
        return self._get(identityCard, identityCard)

ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)

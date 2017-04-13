# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
身份证校验程序
"""
import re
from datetime import datetime

__all__ = ["GeneratIdentityChecker"]
class ExceptionIdentityChecker(Exception):
    pass

def GeneratIdentityChecker(country = "China"):
    cls = globals().get(country+"IdentityChecker")
    if cls:
        return cls()
    else:
        raise ExceptionIdentityChecker(country+" identity's checker not found")


class ChinaIdentityChecker():

    def __init__(self):
        self.anWi = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
        self.cnAreaPart = 6
        self.cnMod = 11
        self.csYearPre = "19"
        self.csCheckCode = "10X98765432"
        self.cnMinArea = 150000
        self.cnMaxArea = 700000

    def check(self,code,**options):
        code = code.upper()
        if len(code) not in (15,18) or not re.match(r"^\d{15}$|^\d{17}[\dxX]$", code):
            return False

        area = int(code[0:self.cnAreaPart])
        if not (self.cnMinArea <= area <= self.cnMaxArea):
            return False

        birthday = self.csYearPre+code[6:12] if len(code) == 15 else code[6:14]
        try:
            datetime.strptime(birthday, "%Y%M%d")
        except:
            return False

        if len(code) == 18:
            wi = self.anWi
            total = 0
            for i in range(16,-1,-1):
                total += int(code[i])*wi[i]
            if not self.csCheckCode[total%self.cnMod] == code[17]:
                return False
        for i in options:
            try:
                checker = getattr(self,"_check_"+i)
            except:
                return False
            if not checker(code,options[i]):
                return False
        return True

    def _check_sex(self,code,sex):
        sex_flag = code[14] if len(code) == 15 else code[16]
        sex = sex.upper()
        if sex == "M":
            return int(sex_flag)%2 == 1
        elif sex == "F":
            return int(sex_flag)%2 == 0
        else:
            return False

if __name__ == "__main__":
    gic = GeneratIdentityChecker()
    while True:
        id_number = raw_input('please input a id number:') # like:340524YYYYMMDD001X
        if id_number == 'exit' or not id_number:
            exit(0)
        if gic.check(id_number):
            print "%s is a valid id number" % id_number
        else:
            print "%s is an invalid id number" % id_number
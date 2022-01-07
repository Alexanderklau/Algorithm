# coding: utf-8

__author__ = 'Yemilice'

import string

path = "/a/./b/../../c/"


print(path.replace("//", "/", -1).replace("../", "").replace("./", ""))
# -*- coding:utf-8 -*-
import os
import sys


BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from src import service


if __name__=='__name__':
    service.execute()
# -*- coding:utf-8 -*-
import subprocess

completeProcess = subprocess.run(["ls"], stdout=subprocess.PIPE, shell=True, encoding='UTF-8')
print(completeProcess.stdout)
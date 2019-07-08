#!/usr/bin/env python
#wraps up rsync to synchronize two directories
from subprocess import call
import sys
import time

source = "Sr_J1_A_N*1_A*.df" #Note the trailing slash
target = "chenlj@lxslc6.ihep.ac.cn:/cefs/higgs/Pixel/JadePix/source/20181130"
rsync = "rsync"
arguments = "-avzP --info=progress2"
cmd = "%s %s %s %s" % (rsync, arguments, source, target)

def sync():
    while True:
        print(cmd)
        ret = call(cmd, shell=True)
        if ret !=0:
            print("resubmitting rsync")
            time.sleep(30)
        else:
            print("rsync was succesful")
            sys.exit(0)

if __name__ == "__main__":
    sync()

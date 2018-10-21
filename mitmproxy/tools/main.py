"""
This file must be kept in a python2.7 and python3.5 compatible syntax!
DO NOT use type annotations or other python3.6-only features that makes this file unparsable by older interpreters!
"""

from __future__ import print_function  # this is here for the version check to work on Python 2.

import sys

if sys.version_info < (3, 6):
    # This must be before any mitmproxy imports, as they already break!
    # Keep all other imports below with the 'noqa' magic comment.
    print("#" * 76, file=sys.stderr)
    print("# mitmproxy requires Python 3.6 or higher!                                 #", file=sys.stderr)
    print("#" + " " * 74 + "#", file=sys.stderr)
    print("# Please upgrade your Python intepreter or use our mitmproxy binaries from #", file=sys.stderr)
    print("# https://mitmproxy.org. If your operating system does not include the     #", file=sys.stderr)
    print("# required Python version, you can try using pyenv or similar tools.       #", file=sys.stderr)
    print("#" * 76, file=sys.stderr)
    sys.exit(1)
else:
    # from ._main import *  # noqa
    pass

if __name__ == "__main__":
    from _main import *

    # ···调试传参说明
    """
    SF：mitmweb和mitmdump两个函数的参数，正式运行过程中，或者将程序打包成installer然后运行时)
            ，来自于操作系统解析命令行的命令后传来的参数。
        1.操作系统解析命令行语句的具体详细规则，可以搜索一下。
        2.至少操作系统会使用空格作为分隔符解析命令行中命令后面的参数字串。
            例如:
                C:\\Users\\lenovo>mitmweb --listen-host 192.168.0.106 -p 8888 -- sfs dsga'
            程序得到的arguments(这里是以win7系统为例)，也就是sys.argv:
                ['C:\\Python37\\Scripts\\mitmweb.exe', '--listen-host', '192.168.0.106', '-p', '8888', '--', 'sfs', 'dsga']
    基于以上分析，如果为了方便调试，需要在pycharm这个开发环境中运行本项目，根据对argparse.py解析参数的分析
    ·· 传参方案是:
            每个参数选项以及每个参数值，都是单独的字符串，将他们组装在一个list中。
            要注意参数选项和参数值的对应关系。
            也可以将参数选项和参数值用等号连接，放在一个字符串中作为list的一项。
            最后将list名作为参数传给mitmweb和mitmdump
    """
    args_test_ii = ['--listen-host', '192.168.0.106', '-p=7777']
    args_test_iii = ['--listen-host=192.168.0.106', '-p 7777']
    args_test_iv = ['--listen-host=192.168.0.106', '-p', '7777']
    args_test_v = ['--listen-host', '192.168.0.106', '-p', '7777']
    # ''调用功能''
    mitmweb(args_test_v)

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
    ·· SF：这里的parse参数，实际上是针对操作系统传来的参数进行解析。
        1.具体详细的规则，可以搜索一下。
        2.至少操作系统会使用空格作为分隔符解析命令行中命令后面的参数字串。
            例如:
                C:\\Users\\lenovo>mitmweb --listen-host 192.168.0.106 -p 8888 -- sfs dsga'
            程序的到的arguments，也就是sys.argv:
                ['C:\\Python37\\Scripts\\mitmweb.exe', '--listen-host', '192.168.0.106', '-p', '8888', '--', 'sfs', 'dsga']
    """
    args_test_ii = ['--listen-host', '192.168.0.106', '-p=7777']
    args_test_iii = ['--listen-host=192.168.0.106', '-p 7777']
    args_test_iv = ['--listen-host=192.168.0.106', '-p', '7777']
    args_test_v = ['--listen-host', '192.168.0.106', '-p', '7777']
    # ''调用功能''
    mitmweb(args_test_v)

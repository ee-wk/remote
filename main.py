import os
from time import sleep

import pytest

from get_cookies import get_cookies

os.system("chrome --remote-debugging-port=9222")
# def run(tag=False):
#     if tag:
#         os.system("chrome --remote-debugging-port=9222")
#         sleep(2)
#         get_cookies()
#     pytest.main(["-s", "-v"])
#
#
# if __name__ == '__main__':
#     run(tag=True)

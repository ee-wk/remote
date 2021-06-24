import os
import pytest
from time import sleep
from get_cookies import get_cookies


def run(tag=False):
    if tag:
        os.popen("chrome --remote-debugging-port=9222")
        sleep(2)
        get_cookies()
    pytest.main(["-s", "-v"])


if __name__ == '__main__':
    run()

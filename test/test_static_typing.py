import os
import glob
import subprocess
from typing import List
import pytest
from hamcrest import assert_that, equal_to, isinstanceof


class InitModTest():
    def __init__(self, *args, **kwargs) -> None:
        self.pkgname: str = "covid"
        super(InitModTest, self).__init__(*args, **kwargs)
        # my_env = os.environ.copy()
        self.rootpath: str = os.path.join(os.getcwd(), '..')
        self.mypy_opts: List[str] = ['--ignore-missing-imports']


@pytest.fixture
def init():
    return InitModTest()


def test_run_mypy_covid(init):
    """Run mypy on covid module sources"""
    mypy_call: List[str] = ["mypy"] + init.mypy_opts + ["-p", init.pkgname]
    browse_result: int = subprocess.call(mypy_call, env=os.environ, cwd=init.rootpath)
    # assert_that(browse_result, equal_to(0), 'mypy on covid')


def test_run_mypy_tests(init):
    """Run mypy on all tests in module under the tests directory"""
    for test_file in glob.iglob(f'{os.getcwd()}/tests/**/*.py', recursive=True):
        mypy_call: List[str] = ["mypy"] + init.mypy_opts + [test_file]
        test_result: int = subprocess.call(mypy_call, env=os.environ, cwd=init.rootpath)
        assert_that(test_result, equal_to(0), f'mypy on test {test_file}')


if __name__ == '__main__':
    test_run_mypy_covid(InitModTest())

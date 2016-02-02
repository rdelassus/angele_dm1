from setuptools import setup
import setuptools
from setuptools.command.test import test as TestCommand
import sys
import os


class PyTest(TestCommand):
    test_package_name = 'api'

    def finalize_options(self):
        TestCommand.finalize_options(self)
        _test_args = [
            '--ignore=build',
            '--ignore=env'
        ]
        extra_args = os.environ.get('PYTEST_EXTRA_ARGS')
        if extra_args is not None:
            _test_args.extend(extra_args.split())
        self.test_args = _test_args
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='algo angele',
    version='0.0.1',
    description='parce que je dois lui faire ses devoirs',
    url='',
    author='remi',
    author_email='',
    license='DWTFYW',
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    zip_safe=False,
    tests_require=[
        'pytest-cov',
        'pytest-cache',
        'pytest'
    ],
    cmdclass={'test': PyTest},
)

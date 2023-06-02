from os.path import exists, join
from os import makedirs, remove
import shutil
import pytest
import subprocess
import sys
from setup import VERSION, PROJECT

outputDir ='./docs/tests'

#Intall/Upgrade pytest and modules if needed
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pytest"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pytest-html"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pytest-cov"])

#Create dummy conftest.py in  src folder
dummyConftest = './src/conftest.py'
if not exists(dummyConftest):
    with open(dummyConftest, 'w'): ...

#clear previous content
if exists(outputDir):
    shutil.rmtree(outputDir)
makedirs(join(outputDir,'coverage')) 

#Run Tests
pytest.main([f'--html={outputDir}/results.html'
            , '--self-contained-html'
            ,f'--cov=src/{PROJECT}'
            , '--cov-report'
            ,f'html:{outputDir}/coverage'])

#Remove the dummy conftest.py in src folder
if exists(dummyConftest):
    remove(dummyConftest)

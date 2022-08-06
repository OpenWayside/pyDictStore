from os.path import exists, join
from os import makedirs, remove, path
import shutil
import pytest
import subprocess
import sys
from zsetup import VERSION, PROJECT
#ensure enviornment is set up before running tests
#EnvironmentSetup.py



#Intall/Upgrade pytest and modules if needed
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pytest"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pytest-html"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pytest-cov"])

dummyConftest = './src/conftest.py'

#Create dummy conftest.py in  src folder
if not exists(dummyConftest):
    with open(dummyConftest, 'w') as fp: ...

dirResults = './docs/tests/'
#clear previous content
if path.exists(dirResults):
    shutil.rmtree(dirResults) 
#Ensure output directories exist
if not exists(dirResults): 
    makedirs(dirResults)
dirCoverage = './docs/tests/coverage'
if not exists(dirCoverage): 
    makedirs(dirCoverage)

#Run Tests
#python -m pytest --html="./docs/tests/results.html" --self-contained-html --cov=src/pyDictStore --cov-report html:"./docs/tests/coverage"
pytest.main(['--html=./docs/tests/results.html'
            , '--self-contained-html'
            , f'--cov=src/{PROJECT}'
            , '--cov-report'
            , 'html:./docs/tests/coverage'])

#Remove the dummy conftest.py in src folder
if exists(dummyConftest):
    remove(dummyConftest)

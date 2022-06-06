from os.path import exists, join
from os import makedirs, remove
#ensure enviornment is set up before running tests
EnvironmentSetup.py



#Intall/Upgrade pytest and modules if needed
python -m pip install --upgrade pytest
python -m pip install --upgrade pytest-html
python -m pip install --upgrade pytest-cov

dummyConftest = './src/conftest.py'

#Create dummy conftest.py in  src folder
if not exists(dummyConftest):
    with open(dummyConftest, 'w') as fp: ...
    
#Ensure output directories exist
dirResults = './docs/tests/results/'
if not exists(dirResults): 
    makedirs(dirResults)
dirCoverage = './docs/tests/result/coverage'
if not exists(dirCoverage): 
    makedirs(dirCoverage)

#Run Tests
python -m pytest --html="./docs/tests/results.html" --self-contained-html --cov=src/pyDictStore --cov-report html:"./docs/tests/coverage"

#Remove the dummy conftest.py in src folder
if exists(dummyConftest):
    remove(dummyConftest)

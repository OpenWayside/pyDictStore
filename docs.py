from pdoc import pdoc, render
from pdoc.__main__ import parser
from pathlib import Path
from setup import VERSION, PROJECT
from os.path import exists
from os import makedirs, remove
import shutil

outputDir = './docs/pdocs'

render.configure(
      show_source = False
    , template_directory = 'pdoc_template'
    , footer_text = f'v{VERSION()}'
    , favicon = None
	, logo = None
	, logo_link = None
    )

#clear content of docs/pdocs
if exists(outputDir):
    shutil.rmtree(outputDir)
#Create output folder
makedirs(outputDir)

doc = pdoc(
    *[f'src/{PROJECT}', f'!{PROJECT}.__events__', f'!{PROJECT}.__decorators__']
    , output_directory=Path(outputDir))
    
#Remove pdocs index file that just redirecs to main module file
remove(f'{outputDir}/index.html')
#Create sub path where files are moved to
makedirs(f'{outputDir}/{PROJECT}')
#move files into sub folder in preperation for copy to public site
shutil.move(f'{outputDir}/{PROJECT}.html',f'{outputDir}/{PROJECT}/index.html')
shutil.move(f'{outputDir}/search.js',f'{outputDir}/{PROJECT}/search.js')
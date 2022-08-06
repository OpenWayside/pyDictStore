from pdoc import pdoc, render
from pdoc.__main__ import parser
from pathlib import Path
from zsetup import VERSION, PROJECT
import os, shutil

render.configure(
      show_source = False
    , template_directory = 'pdoc_template'
    , footer_text = f'v{VERSION(PROJECT)}'
    , favicon = None
	, logo = None
	, logo_link = None
    )

#clear content of docs/pdocs
if os.path.exists('docs/pdocs'):
    shutil.rmtree('docs/pdocs')

doc = pdoc(
    *[f'src/{PROJECT}', f'!{PROJECT}.__events__', f'!{PROJECT}.__decorators__']
    , output_directory=Path('docs/pdocs'))
    
#Remove pdocs index file that just redirecs to main module file
os.remove('docs/pdocs/index.html')
#Create sub path where files are moved to
os.makedirs(f'docs/pdocs/{PROJECT}')
#move files into sub folder in preperation for copy to public site
shutil.move(f'docs/pdocs/{PROJECT}.html',f'docs/pdocs/{PROJECT}/index.html')
shutil.move('docs/pdocs/search.js',f'docs/pdocs/{PROJECT}/search.js')
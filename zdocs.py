from pdoc import pdoc, render
from pathlib import Path
from zsetup import VERSION, PROJECT

render.configure(
      show_source = False
    , template_directory = 'pdoc_template'
    , footer_text = f'{PROJECT} v{VERSION(PROJECT)}'
    , favicon = None
	, logo = None
	, logo_link = None
    )
    
doc = pdoc(
    f'src/{PROJECT}'
    , output_directory=Path('docs'))
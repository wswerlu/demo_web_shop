from glob import glob
from os.path import join
from pathlib import Path
from platform import system


def get_fixtures():
    fixtures = join(Path(__file__).parent.parent, 'fixtures')
    file_path = []
    for file in glob(f'{fixtures}/*'):
        file = file.split('/') if system().lower() in ['linux', 'darwin'] else file.split('\\')
        file = file[-1].split('.')[0]
        if file not in ['__init__', '__pycache__']:
            file_path.append(f'fixtures.{file}')
    return file_path

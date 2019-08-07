import json
import os
import glob
import logging

logger = logging.getLogger(__name__)

def get_md_files():
    md_files = glob.glob('*.md')
    return md_files

notebook_files = [md_file.replace('md', 'ipynb') for md_file in get_md_files()]
missing_files = []

for i, notebook_file in enumerate(notebook_files):
    if not os.path.isfile("notebooks/" + notebook_file):
        missing_files.append(md_files[i])
        os.system("notedown " + md_files[i] + " > notebooks/" + notebook_file)


for notebook_file in notebook_files:
    with open('notebooks/' + notebook_file) as fjason:
        jason_file = json.load(fjason)

    for i, cell in enumerate(jason_file['cells']):
        try:
            if cell['cell_type'] == 'markdown' and cell['metadata']['lang'] != 'pt':
                del jason_file['cells'][i]
        except KeyError:
            logger.error(notebook_file + " Untranslated")

    with open('tmp.ipynb', 'w') as f:
        json.dump(jason_file, f)      

    os.system("notedown tmp.ipynb --to markdown --strip > " + notebook_file.replace('ipynb', 'md'))
    os.system("rm -r tmp.ipynb")
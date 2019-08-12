import json
import os
import glob
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%d-%m-%Y %H:%M',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def get_md_files():
    md_files = glob.glob('*.md')
    return md_files

def md_to_ipynb(notebook_files, md_files):
    missing_files = []
    for i, notebook_file in enumerate(notebook_files):
        if not os.path.isfile("notebooks/" + notebook_file):
            missing_files.append(md_files[i])
            os.system("notedown " + md_files[i] + " > notebooks/" + notebook_file)
            
if __name__ == "__main__":
    logger.info("Checking notebooks process started")
    md_files = get_md_files()
    notebook_files = [md_file.replace('md', 'ipynb') for md_file in get_md_files()]
    md_to_ipynb(notebook_files, md_files)

import zipfile
mane_zip = zipfile.ZipFile('C:\\Users\\main.zip')
mane_zip.extractall('C:\\Downloads\\Users')
mane_zip.close()

import os

with open('result.txt', 'a') as f:
    for current_dir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            f.write('{}\n'.format(current_dir))

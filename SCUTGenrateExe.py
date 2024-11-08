import os
import subprocess

src_name = 'SCUTLogin_click.py'

if os.path.isfile(src_name):
    subprocess.run(['pyinstaller','--onefile',src_name])
    print(f'{src_name} 已转为 exe 文件')
else:
    print(f'文件{src_name}不在同级目录下')
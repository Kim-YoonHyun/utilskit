import sys
import os
import configparser
import subprocess


def main():
    scripts_path = os.path.dirname(os.path.abspath(__file__))
    pack_path = os.path.dirname(scripts_path)
    lib_path = os.path.dirname(pack_path)

    # token.ini 읽기
    config = configparser.ConfigParser()
    config.read(os.path.join(lib_path, "token.ini"))

    username = config['PyPI']['username']
    password = config['PyPI']['password']

    # subprocess 로 twine upload 실행
    subprocess.run([
        'twine', 'upload', f'{pack_path}/dist/*',
        '-u', username,
        '-p', password
    ])

if __name__ == "__main__":
    main()


import sys
import os
import json
import copy
import tomlkit
import configparser
import subprocess
from pathlib import Path

# [1.0.0] @done_log: 필요한 함수 자체를 강제 주입
USER_PATH = Path("~").expanduser()
sys.path.insert(0, str(USER_PATH / "library" / "dev_tools")) 
sys.path.insert(0, str(USER_PATH / "library" / "utilskit" / "src"))
sys.path.insert(0, str(USER_PATH / "library" / "logie" / "src"))
from utilskit.versionutils import version_up
from logie.docsutils import documenting


def main():
    scripts_path = Path(__file__).resolve().parent
    pack_path = scripts_path.parent
    lib_path = pack_path.parent

    # lock 파일 불러오기
    with open(pack_path / "package.lock", "r", encoding="utf-8-sig") as f:
        lock_info = json.load(f)

    # pyproject.toml 파일 읽기
    with open(pack_path / "pyproject.toml", "r", encoding="utf-8-sig") as f:
        pre_toml_info = tomlkit.load(f)
    toml_info = copy.deepcopy(pre_toml_info)
    name = toml_info["project"]["name"]
    pre_version = toml_info["project"]["version"]

    new_version, tag = version_up(name, pre_version)
    print(11)
    sys.exit()
    _ = documenting(
        tag=tag,
        summary=summary,
        version=new_version,
        log_contents=log_contents,
        docs_path=pack_path
    )
    print(new_version)
    sys.exit()
    
    # # 3. 파일 저장
    # with open("config.toml", "w", encoding="utf-8") as f:
    #     f.write(tomlkit.dumps(config))

    # token.ini 읽기
    config = configparser.ConfigParser()
    config.read(os.path.join(lib_path, "token.ini"))

    username = config['PyPI']['username']
    password = config['PyPI']['password']

    # subprocess 로 build 실행
    # [1.0.0] @done_log: build 하는 부분 추가함
    subprocess.run(["python", "-m", "build"], cwd=pack_path)

    # subprocess 로 twine upload 실행
    subprocess.run([
        'twine', 'upload', f'{pack_path}/dist/*',
        '-u', username,
        '-p', password
    ])

if __name__ == "__main__":
    main()


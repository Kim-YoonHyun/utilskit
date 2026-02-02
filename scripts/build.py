import os
import sys
import json
from pathlib import Path


# [1.0.0] @done_log: 필요한 함수 자체를 강제 주입
USER_PATH = Path("~").expanduser()
sys.path.insert(0, str(USER_PATH / "library" / "utilskit" / "src"))
sys.path.insert(0, str(USER_PATH / "library" / "logie" / "src"))
from utilskit.versionutils import get_git_modified, get_git_new, version_up
from utilskit.utils import path_change


def main():
    scripts_path = Path(__file__).resolve().parent
    pack_path = scripts_path.parent

    # with open(pack_path / "manifest.json", "r", encoding="utf-8-sig") as f:
    #     manifest = json.load(f)

    with open(pack_path / "package.lock", "r", encoding="utf-8-sig") as f:
        lock_info = json.load(f)
    
    resolved = lock_info["resolved"]
    c_info_list = lock_info["component"]

    for c_info in c_info_list:
        c_name = c_info["name"]
        form_c_path = c_info["path"]
        do_build = c_info["build"]
        print(c_name, do_build)

    include = ["docs", "src", "package.lock", "pyproject.toml", "README.md"]


if __name__ == "__main__":
    main()
import sys
import os
import argparse
from datetime import datetime
import subprocess
import textwrap
import copy
import toml
import tomli_w
import json


# @log: 버전업을 통해 pyproject.toml 의 버전 값을 바꾸는 기능 추가
# @log: git 을 통해 변경이력을 확인 (status) 하고 해시검증을 통한 대상선정, 버전업, git add&commit 까지 진행하는 기능
def versioning(save, pack_path, lib_path):

    # .hash_cache.json 읽기
    if os.path.isfile(os.path.join(pack_path, ".hash_cache.json")):
        with open(os.path.join(pack_path, ".hash_cache.json"), "r", encoding="utf-8-sig") as f:
            pre_hash_cache = json.load(f)
    else:
        pre_hash_cache = {}
    hash_cache = copy.deepcopy(pre_hash_cache)

    # 기존 pyproject.toml 파일 읽기
    with open(os.path.join(pack_path, "pyproject.toml"), "r", encoding="utf-8-sig") as f:
        pre_toml_info = toml.load(f)
    toml_info = copy.deepcopy(pre_toml_info)
    name = toml_info["project"]["name"]
    pre_ver = toml_info["project"]["version"]

    # ==================================================
    # 버전 업 진행
    sys.path.append(lib_path)
    from utilskit import versionutils as vu
    from utilskit import hashutils as hu
    from logie import logie as lo

    # git status 기반 파일 추적 및 대상 리스트 추출
    git_check_list = vu.get_git_status(pack_path)

    # git 기반 체크 결과별 파악
    change_log = ""
    versioning_list = []
    for git_check in git_check_list:
        file_path = git_check["file_path"]
        status = git_check["status"]

        # 기존 해시 추출
        try:
            pre_hash = hash_cache[file_path]
        except KeyError:
            pre_hash = ""

        # 삭제 & 수정 여부 파악
        if status == "Deleted":
            new_hash = None
            _ = hash_cache.pop(file_path, None)
        else:
            new_hash = hu.file2hash(file_path)
            hash_cache[file_path] = new_hash

        # 기존 해시와 신규 해시가 다른 경우
        if pre_hash != new_hash:
            # 버저닝 대상 리스트에 추가
            versioning_list.append(git_check)
            # 로그 추출
            change_log += f"{status:}: {file_path}\n"
            log_list = lo.extract_log(file_path)
            for log_ in log_list:
                change_log += f" - {log_}\n"
            change_log += "\n"
    change_log = change_log.strip()
    print(change_log)

    # =======================================================
    # 버저닝 적용 대상이 있는 경우
    if len(versioning_list) > 0:
        # 버전 업
        new_ver, tag = vu.version_up(name, pre_ver)
        print(f"{tag}: {pre_ver} --> {new_ver}")

        # 로그를 done_log 로 변경
        for target_info in versioning_list:
            file_path = target_info["file_path"]
            if save:
                try:
                    lo.log2donelog(file_path, new_ver)
                except FileNotFoundError:
                    pass
            else:
                print(f"|예정| {file_path} 의 주석을 done 으로 변경")

        # README.md 스크립트 생성
        now = datetime.now()
        if save:
            summary = input("버전 요약 입력 : ")
            _ = lo.documenting(
                tag=tag, 
                summary=summary, 
                version=new_ver, 
                log_contents=change_log, 
                docs_path=pack_path
            )
        
            # toml.tmp 저장
            toml_info["project"]["version"] = new_ver
            with open(os.path.join(pack_path, "pyproject.toml.tmp"), "wb") as f:
                tomli_w.dump(toml_info, f)
            
            # hash_cache 저장
            with open(os.path.join(pack_path, ".hash_cache.json.tmp"), "w", encoding="utf-8-sig") as f:
                json.dump(hash_cache, f, indent="\t", ensure_ascii=False)

            # git add & commit 진행
            vu.git_addcommit(pack_path, f'*{tag}: {now.strftime("%Y-%m-%d")} ver {new_ver}')

            # .tmp 를 원본으로 교체
            do = lo.tmp2new(pack_path)
            if do == 0:
                lo.delete_tmp(pack_path)
        else:
            print(f"|예정| README.md.tmp 생성")
            print(f"|예정| pyproject.toml.tmp 생성")
            print(f"|예정| .hash_cache.json.tmp 생성")
            print(f'|예정| *{tag}: {now.strftime("%Y-%m-%d")} ver {new_ver} 으로 커밋')

    else:
        print("There is no Change")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", type=bool, default=False)
    args = parser.parse_args()
    save = args.save

    scripts_path = os.path.dirname(os.path.abspath(__file__))
    pack_path = os.path.dirname(scripts_path)
    lib_path = os.path.dirname(pack_path)
    try:
        versioning(save, pack_path, lib_path)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()


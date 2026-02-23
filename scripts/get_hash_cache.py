import sys
import os
import json
import fnmatch
import argparse
from pathlib import Path

from utilskit.utils import path_change
from utilskit.hashutils import file2hash


# [2.5.6] @done_log: file 리스트를 해시화하는 연산을 `filelist2hash` 함수로 분리
def filelist2hash(file_parent_path, component_path, file_list, hash_cache):
    for f_name in file_list:
        f_path = str(Path(file_parent_path) / f_name)
        f_hash = file2hash(f_path)
        rel_f_path = str(Path(f_path).relative_to(component_path))
        hash_cache[component_path][rel_f_path] = f_hash
    return hash_cache


def job(product_path):
    # lock 불러오기
    with open(product_path / "product.lock", "r", encoding="utf-8-sig") as f:
        lock_info = json.load(f)
    
    # manifest 불러오기
    with open(product_path / "manifest.json", "r", encoding="utf-8-sig") as f:
        manifest = json.load(f)
    
    # ===============================================================
    # lock 해시 스키마 버전 추출
    try:
        lhs_ver = lock_info["product"]["hash_schema_version"]
    except KeyError:
        lhs_ver = "v1"

    # manifest 해시 스키마 버전 추출
    try:
        mani_hash_schema = manifest["hash_schema"]
        mhs_ver = mani_hash_schema["version"]
    except KeyError:
        print("[EORROR] manifest 에 hash_schema 키가 존재하지 않습니다. manifest 내용 및 버전 확인이 필요합니다.")
        return

    # 해시 캐시 초기화
    hash_cache = {"schema_version":mhs_ver}
    if mhs_ver == lhs_ver:
        print("해시 스키마 버전이 동일합니다. 해시 변경을 취소합니다.")
        # return
    else:
        print(f"해시 스키마 버전이 변경되었습니다. ({lhs_ver} --> {mhs_ver})")
        print('전체 해시 갱신을 진행합니다...')
    
    # ===============================================================
    # 진행
    common_exclude = manifest["common_exclude"]
    common_untracked = manifest["common_untracked"]
    comp_info_list = manifest["component"]
    for c_info in comp_info_list:
        c_name = c_info["name"]
        c_manage = c_info["manage"]
        c_mode = c_info["mode"]
        form_c_path = c_info["path"]
        include = c_info["include"]
        c_exclude = c_info["exclude"]
        c_untracked = c_info["untracked"]

        # 관리 대상이 아닌 경우
        if not c_manage:
            continue

        # 변수 전처리 & 초기화
        c_path = path_change(form_c_path, product_path=product_path, name=c_name)
        exclude_list = c_exclude + common_exclude
        ignore_list = exclude_list + c_untracked + common_untracked

        # 파일군 인 경우
        # [2.5.9] @done_log: 파일군에서 untrack 와 exclude 적용
        if c_mode == "file_group":
            key = c_path
            fg_c_path = str(Path(key).parent)
            hash_cache[key] = {}
            for f_name in include:
                if f_name in ignore_list:
                    continue
                f_path = str(Path(fg_c_path) / f_name)
                f_hash = file2hash(f_path)
                rel_f_path = str(Path(f_path).relative_to(fg_c_path))
                hash_cache[key][rel_f_path] = f_hash
        # 폴더인 경우
        else:
            hash_cache[c_path] = {}
            for root, dirs, files in os.walk(c_path):
                
                # 폴더 제외
                dirs[:] = [d for d in dirs if d not in exclude_list]

                # 파일 제외
                filtered_files = [
                    f for f in files 
                    if not any(fnmatch.fnmatch(f, p) for p in ignore_list)
                ]
                for f_name in filtered_files:
                    f_path = str(Path(root) / f_name)
                    f_hash = file2hash(f_path)
                    rel_f_path = str(Path(f_path).relative_to(c_path))
                    hash_cache[c_path][rel_f_path] = f_hash
    # 임시 파일 저장
    with open(product_path / ".hash_cache.json.tmp", "w", encoding="utf-8-sig") as f:
        json.dump(hash_cache, f, indent="\t", ensure_ascii=False)

    # 원본 교체
    do = input(".hash_cache.json.tmp 를 원본으로 교체하시곘습니까? (Y/n): ")
    if do == "Y":
        os.replace(
            product_path / ".hash_cache.json.tmp",
            product_path / ".hash_cache.json"
        )


def main():
    script_path = Path(__file__).resolve().parent
    product_path = script_path.parent
    job(product_path)


if __name__ == "__main__":
    main()
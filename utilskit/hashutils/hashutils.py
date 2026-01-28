import sys
import os
import hashlib
import fnmatch
import json
import copy

# [1.0.0] @done_log: 해시 함수 전부 모음
__all__ = [
    "content2hashobj", "file2hash", "dir2hash", 
    "get_all_hash", "combined2hash", "hashlist2hash"
]


def content2hashobj(file_path, hash_obj):
    # 텍스트 모드로 읽어야 줄(line) 단위 판단이 정확합니다.
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                # 해당 키워드가 포함된 줄은 해시 계산에서 제외
                if "@log" in line or "@done_log" in line:
                    continue
                
                # 나머지 코드 줄만 해시에 반영
                hash_obj.update(line.encode("utf-8"))
    except UnicodeDecodeError:
        # 파일 내용 추가
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hash_obj.update(chunk)
    return hash_obj


def file2hash(file_path):
    # 해시 오브젝트 생성
    hash_obj = hashlib.sha256()

    # 파일 경로를 해시에 추가
    hash_obj.update(file_path.encode())
    
    # 파일 내용 추가
    hash_obj = content2hashobj(file_path, hash_obj)

    # 16진수 변환
    hash_ = hash_obj.hexdigest() 
    return hash_


def dir2hash(dir_path, ignore_list=[]):
    # hash object 생성
    hash_obj = hashlib.sha256()

    # 대상 디렉토리 순회
    for root, dirs, files in os.walk(dir_path):

        # 순회에서 제외 적용
        for ignore_ in ignore_list:
            if ignore_ in dirs:
                dirs.remove(ignore_)
        
        # 순회 파일 별 진행
        for file_name in sorted(files):
            # 제외 대상 파일인지 확인
            if file_name in ignore_list:
                continue
            
            # 기준 디렉토리부터 파일까지의 경로를 해시에 포함
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, dir_path)
            hash_obj.update(relative_path.encode())
            
            # 파일 내용 추가
            hash_obj = content2hashobj(file_path, hash_obj)

    # binary hash 데이터를 16진수 문자열 변환
    hash_ = hash_obj.hexdigest() 
    return hash_


def get_all_hash(dir_path, bundle=[], ignore_list=[]):

    result_list = []

    # 대상 디렉토리 순회
    for root, dirs, files in os.walk(dir_path):

        # 순회에서 제외 적용
        for ignore_ in ignore_list:
            if ignore_ in dirs:
                dirs.remove(ignore_)
        
        # 묶음 폴더로 지정된 경우
        if os.path.basename(root) in bundle:
            hash_ = dir2hash(root)
            result_list.append([root, hash_])
            # dirs 리스트의 내용을 비워서 os.walk 로 인한 하위 순회 방지
            dirs[:] = []
            continue
        
        # 순회 파일 별 진행
        for file_name in sorted(files):
            # 제외 대상 파일인지 확인
            # if file_name in ignore_list:
            if any(fnmatch.fnmatch(file_name, p) for p in ignore_list):
                continue
            
            file_path = os.path.join(root, file_name)
            hash_ = file2hash(file_path)    

            # 결과 추가
            result_list.append([file_path, hash_])

    return result_list

# [1.0.0] @done_log: 함수 `reset_values` 삭제
# [1.0.0] @done_log: 함수 `combined2hash` 에서 파일 이름이 manifest.json 인 경우의 논리 제거
def combined2hash(dir_path, file_list):
    result_list = []

    # 대상 파일들 경로 구체화
    file_path_list = []
    for file_name in file_list:
        file_path = os.path.join(dir_path, file_name)
        file_path_list.append(file_path)
    file_path_list.sort()

    # 각 파일의 이름과 내용을 해시에 업데이트
    for file_path in file_path_list:
        # 해시값 추출
        hash_ = file2hash(file_path)
        # 결과 추가                
        result_list.append([file_path, hash_])
    return result_list


def hashlist2hash(hash_list):
    if len(hash_list) == 0:
        return ""

    new_hash_list = []
    for hash_ in hash_list:
        if len(hash_) == 0:
            continue
        new_hash_list.append(hash_)
    hash_list = new_hash_list.copy()

    # 리스트 정렬
    sorted_hashes = sorted(hash_list)

    # 2. 모든 해시를 하나로 결합
    # 구분자('|')를 넣어 'aa','b' 와 'a','ab' 가 같은 해시를 만드는 것을 방지
    combined_string = "|".join(sorted_hashes)

    # 3. 최종 해시 계산
    hash_ = hashlib.sha256(combined_string.encode()).hexdigest()
    return hash_
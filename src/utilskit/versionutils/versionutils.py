import sys
import os
import semver
import textwrap
from pathlib import Path
from git import Repo, exc


# [1.0.2] @done_log: __all__ 추가
__all__ = ["version_up", "get_git_modified", "get_git_new", "git_addcommit"]


# [1.0.0] @done_log: tag 예시 리스트 출력시 strip 적용
def version_up(name, pre_version):
    tag_dict = {
        1:"Major-Release",
        2:"Feature",
        3:"Patch",
        4:"Refactoring",
        5:"Test",
        6:"Post-release",
        0:"Ignore"
    }
    tag_key_list = list(tag_dict.keys())
    min_tag = min(tag_key_list)
    max_tag = max(tag_key_list)

    # 버전 문자열 연산화
    if pre_version == "":
        pre_version = "0.0.0"
    v = semver.Version.parse(pre_version)

    # 버전 변경 입력값 받기
    string = textwrap.dedent(
        """
        ------------------------------------------------------------
        | 1 : Major-Release | Major      | 1.1.12 --> 2.0.0        |
        | 2 : Feature       | Minor      | 1.1.12 --> 1.2.0        |
        | 3 : Patch         | Patch      | 1.1.12 --> 1.1.13       |
        | 4 : Refactoring   | Patch      | 1.1.12 --> 1.1.13       |
        | 5 : Test          | Identifier | 1.1.12 --> 1.1.12+test1 |
        | 6 : Post-release  | Identifier | 1.1.12 --> 1.1.12post1  |
        | 0 : Ignore        | Ignore     | 1.1.12 --> 1.1.12       |
        ------------------------------------------------------------
        """
    ).strip()
    print(string)
    while True:
        try:
            tag = int(input(f"{name}({pre_version}) 버전 업 태그를 입력 :"))
            if tag not in tag_key_list:
                print(f'잘못된 입력값입니다. {min_tag} ~ {max_tag} 사이의 값을 입력해주세요')
            else:
                break
        except Exception:
            print(f'잘못된 입력값입니다. {min_tag} ~ {max_tag} 사이의 값을 입력해주세요')

    # ==============================================================
    # 새 버전 변경 적용
    if tag == 1:
        new_version = str(v.bump_major())
    elif tag == 2:
        new_version = str(v.bump_minor())
    elif tag in [3, 4]:
        new_version = str(v.bump_patch())
    elif tag in [5, 6]:
        new_version = input(f"변경 버전 직접 입력 --> ")
    elif tag == 0:
        new_version = pre_version
    tag_text = tag_dict[tag]

    return new_version, tag_text


STATUS_DICT = {
    "M":"Modified",
    "A":"Added",
    "D":"Deleted",
    "R":"Renamed",
    "C":"Copied",
    "T":"Type changed",
    "U":"Unmerged",
    "X":"Unknown"
}

# [1.0.0] @done_log: git status 정보를 추출하는 `get_git_status` 함수 추가
# [1.0.0] @done_log: 함수 `get_git_status` 함수명을 `get_git_modified` 로 변경
# [1.0.0] @done_log: 함수 `get_git_modified` 내부에서 컴포넌트별 이력 탐지 구조 추가
def get_git_modified(repo_path, search_path):
    # 깃 정보 추출
    repo = Repo(repo_path)

    # 경로 posix 화 (git 표준)
    search_path = Path(search_path).as_posix()

    # 결과 변수 초기화
    result_list = []

    # Unstaged 변경 사항 추적
    unstaged_diff_list = repo.index.diff(None, paths=[search_path])
    
    for unstaged_diff in unstaged_diff_list:
        # 파일 경로
        uns_f_path = unstaged_diff.a_path
        full_f_path = str(Path(repo_path) / uns_f_path)
        
        # 대상 파일 정보 추가
        status = STATUS_DICT[unstaged_diff.change_type]
        result_list.append({"file_path": full_f_path, "status": status})

    return result_list
    

# [1.0.0] @done_log: 함수 `get_git_new` 추가
def get_git_new(repo_path, search_path):
    # 깃 정보 추출
    repo = Repo(repo_path)

    # 결과 변수 초기화
    result_list = []

    # Untracked 파일
    untrack_list = repo.untracked_files
    for unt_path in untrack_list:
        # 대상 파일 정보 추가
        file_path = str(repo_path / unt_path)
        if search_path in file_path:
            result_list.append({"file_path": file_path, "status": "New"})
    return result_list


# [1.0.0] @done_log: 함수 `git_addcommit` 추가
def git_addcommit(repo_path, message):
    repo = Repo(repo_path)
    repo.git.add(A=True)  # git add .
    repo.index.commit(message) # git commit -m "..."
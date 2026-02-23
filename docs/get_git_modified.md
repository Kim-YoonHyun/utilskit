

# get_git_modified

Git 저장소에서 수정된(Modified) 파일 목록을 추출하는 함수.

지정된 경로 내에서 Unstaged 상태의 변경된 파일들을 탐지하고,
각 파일의 경로와 상태(Modified, Added, Deleted 등)를 리스트로 반환한다.

## parameters

| 입력변수      | type  | default |
| ------------- | ----- | ------- |
| `repo_path`   | `str` | -       |
| `search_path` | `str` | -       |

## return

| 출력 type | 설명                                                          |
| --------- | ------------------------------------------------------------- |
| `list`    | [{"file_path": 경로, "status": 상태}, ...] 형태의 딕셔너리 리스트 |

## 사용예시

```python
from utilskit import versionutils as vu
from pathlib import Path

# Git 저장소의 변경된 파일 탐지
repo_path = "/home/user/myproject"
search_path = "/home/user/myproject/src"

modified_files = vu.get_git_modified(repo_path, search_path)
print(modified_files)
"""
[
    {'file_path': '/home/user/myproject/src/main.py', 'status': 'Modified'},
    {'file_path': '/home/user/myproject/src/utils.py', 'status': 'Modified'},
    {'file_path': '/home/user/myproject/src/config.py', 'status': 'Deleted'}
]
"""

# 전체 저장소 탐색
all_modified = vu.get_git_modified("/home/user/myproject", "/home/user/myproject")

# 수정된 파일 개수 확인
print(f"Modified files: {len(all_modified)}")
```

## parameters detail

> `repo_path`  | type : `str`
>
> Git 저장소의 루트 디렉토리 경로.
> .git 폴더가 위치한 최상위 디렉토리를 지정해야 함.

> `search_path` | type: `str`
>
> 변경 사항을 탐지할 대상 경로.
> repo_path 내의 특정 하위 디렉토리나 파일을 지정할 수 있음.
> POSIX 표준 경로로 자동 변환되어 처리됨.
>
> 반환되는 status 값:
> - "Modified": 파일이 수정됨
> - "Added": 새 파일이 추가됨 (Staged)
> - "Deleted": 파일이 삭제됨
> - "Renamed": 파일명이 변경됨
> - "Copied": 파일이 복사됨
> - "Type changed": 파일 타입이 변경됨
> - "Unmerged": 병합되지 않은 상태
> - "Unknown": 알 수 없는 상태
>
> ```python
> # 예시: 특정 모듈의 변경 사항만 추적
> modified = get_git_modified(
>     repo_path="/project",
>     search_path="/project/src/api"
> )
>
> # 수정된 파일만 필터링
> modified_only = [f for f in modified if f['status'] == 'Modified']
>
> # 파일 경로만 추출
> file_paths = [f['file_path'] for f in modified]
> ```



# get_git_new

Git 저장소에서 추적되지 않는(Untracked) 새 파일 목록을 추출하는 함수.

지정된 경로 내에서 Git 에 아직 추가되지 않은 새 파일들을 탐지하고,
각 파일의 경로와 상태(New)를 리스트로 반환한다.

## parameters

| 입력변수      | type  | default |
| ------------- | ----- | ------- |
| `repo_path`   | `str` | -       |
| `search_path` | `str` | -       |

## return

| 출력 type | 설명                                                          |
| --------- | ------------------------------------------------------------- |
| `list`    | [{"file_path": 경로, "status": "New"}, ...] 형태의 딕셔너리 리스트 |

## 사용예시

```python
from utilskit import versionutils as vu
from pathlib import Path

# Git 저장소의 새 파일 탐지
repo_path = Path("/home/user/myproject")
search_path = "/home/user/myproject/src"

new_files = vu.get_git_new(repo_path, search_path)
print(new_files)
"""
[
    {'file_path': '/home/user/myproject/src/new_module.py', 'status': 'New'},
    {'file_path': '/home/user/myproject/src/test_new.py', 'status': 'New'}
]
"""

# 전체 저장소에서 새 파일 탐색
all_new = vu.get_git_new(
    Path("/home/user/myproject"),
    "/home/user/myproject"
)

# 새 파일 개수 확인
print(f"New files: {len(all_new)}")

# 새 파일 경로만 추출
new_paths = [f['file_path'] for f in new_files]
```

## parameters detail

> `repo_path`  | type : `str`
>
> Git 저장소의 루트 디렉토리 경로.
> .git 폴더가 위치한 최상위 디렉토리를 지정해야 함.
> pathlib.Path 객체도 입력 가능.

> `search_path` | type: `str`
>
> 새 파일을 탐지할 대상 경로.
> repo_path 내의 특정 하위 디렉토리를 지정하면 해당 경로를 포함하는 untracked 파일만 반환됨.
> 경로 문자열 포함 여부를 확인하므로 정확한 경로를 사용하는 것이 좋음.
>
> 모든 반환 항목의 status 는 "New" 로 고정됨.
>
> ```python
> # 예시 1: 특정 디렉토리의 새 파일만 확인
> new_in_api = get_git_new(
>     repo_path=Path("/project"),
>     search_path="/project/src/api"
> )
>
> # 예시 2: .gitignore 에 포함되지 않은 모든 새 파일
> # (.gitignore 에 명시된 파일은 untracked_files 에 나타나지 않음)
> all_new = get_git_new(
>     repo_path=Path("/project"),
>     search_path="/project"
> )
>
> # 예시 3: 새 파일이 있는지 확인
> has_new_files = len(get_git_new(repo_path, search_path)) > 0
> ```



# git_addcommit

Git 저장소의 모든 변경사항을 스테이징하고 커밋하는 함수.

`git add .` 와 `git commit -m "message"` 명령을 한 번에 수행한다.
저장소 내의 모든 변경된 파일과 새 파일이 자동으로 스테이징되어 커밋됨.

## parameters

| 입력변수    | type  | default |
| ----------- | ----- | ------- |
| `repo_path` | `str` | -       |
| `message`   | `str` | -       |

## return

| 출력 type | 설명       |
| --------- | ---------- |
| `None`    | 반환값 없음 |

## 사용예시

```python
from utilskit import versionutils as vu

# 모든 변경사항을 커밋
repo_path = "/home/user/myproject"
commit_message = "Add new feature for user authentication"

vu.git_addcommit(repo_path, commit_message)

# 커밋 후 추가 작업
print("Commit completed successfully!")
```

```python
# 버전 업데이트와 함께 사용
from utilskit import versionutils as vu

repo_path = "/project"
current_version = "1.2.3"

# 버전 업데이트
new_version, tag = vu.version_up("MyProject", current_version)

# 변경사항 커밋
commit_msg = f"[{tag}] Version {current_version} -> {new_version}"
vu.git_addcommit(repo_path, commit_msg)
```

```python
# 자동화 스크립트에서 사용
import os
from utilskit import versionutils as vu

def auto_commit(repo, msg):
    try:
        vu.git_addcommit(repo, msg)
        print(f"✓ Committed: {msg}")
    except Exception as e:
        print(f"✗ Commit failed: {e}")

auto_commit("/my/repo", "Automated daily backup")
```

## parameters detail

> `repo_path`  | type : `str`
>
> Git 저장소의 루트 디렉토리 경로.
> .git 폴더가 위치한 최상위 디렉토리를 지정해야 함.

> `message` | type: `str`
>
> 커밋 메시지.
> 변경사항을 설명하는 명확한 메시지를 작성해야 함.
>
> 주의사항:
> - 이 함수는 `git add -A` 를 실행하므로 저장소 내 모든 변경사항이 스테이징됨
> - 삭제된 파일도 포함됨
> - .gitignore 에 명시된 파일은 제외됨
> - 커밋만 수행하며 push 는 하지 않음
> - 커밋할 변경사항이 없으면 에러가 발생할 수 있음
>
> ```python
> # 예시 1: 기본 사용
> git_addcommit("/project", "Fix bug in authentication")
>
> # 예시 2: 다국어 메시지
> git_addcommit("/project", "기능 추가: 사용자 로그인")
>
> # 예시 3: 상세 메시지
> message = """Add user profile feature
>
> - Add profile page UI
> - Implement profile update API
> - Add unit tests for profile module
> """
> git_addcommit("/project", message)
> ```

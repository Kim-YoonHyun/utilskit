

# combined2hash

특정 디렉토리 내의 지정된 파일 리스트 각각에 대한 해시를 계산하는 함수.

파일 리스트를 입력받아 각 파일의 해시값을 계산하고, 결과를 [파일경로, 해시값] 형태의 리스트로 반환한다.
get_all_hash 와 달리 모든 파일을 순회하지 않고 지정된 파일만 처리한다.

@log, @done_log 가 명시되어있는 주석은 해시 계산에서 제외된다.

## parameters

| 입력변수    | type   | default |
| ----------- | ------ | ------- |
| `dir_path`  | `str`  | -       |
| `file_list` | `list` | -       |

## return

| 출력 type | 설명                                                  |
| --------- | ----------------------------------------------------- |
| `list`    | [[파일경로, 해시값], ...] 형태의 2차원 리스트         |

## 사용예시

```python
from utilskit import hashutils as hu

# 특정 파일들만 해시 계산
target_files = ["main.py", "config.json", "utils.py"]
result = hu.combined2hash("/path/to/project", target_files)
print(result)
"""
[
    ['/path/to/project/config.json', '13514451708f8c73e1e4d9f9fabf905412ab8bed65a2773f15ed697d9b769fe4'],
    ['/path/to/project/main.py', '6e826159f17ac96fda50f327f1b522230e1fe36bb5c1b1147e02480da8103682'],
    ['/path/to/project/utils.py', 'a1b2c3d4e5f6789...']
]
"""

# 결과는 파일명 기준으로 정렬됨
```

## parameters detail

> `dir_path`  | type : `str`
>
> 대상 파일들이 위치한 디렉토리의 절대경로.
> file_list 의 파일명들이 이 디렉토리 내에 존재해야 함.

> `file_list` | type: `list`
>
> 해시를 계산할 파일명 리스트.
> 파일명만 입력하면 되며 (확장자 포함), 자동으로 dir_path 와 결합되어 전체 경로가 구성됨.
> 결과는 파일명 기준으로 알파벳순 정렬됨.
>
> ```python
> # 예시: 핵심 설정 파일들만 해시 계산
> core_files = ["requirements.txt", "setup.py", "pyproject.toml"]
> result = combined2hash("/project", core_files)
>
> # 파일이 존재하지 않으면 에러 발생
> # 모든 파일명은 dir_path 디렉토리 내에 직접 위치해야 함 (하위 폴더 X)
> ```

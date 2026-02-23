

# get_all_hash

특정 디렉토리 내의 모든 파일 각각에 대한 해시를 계산하는 함수.

각 파일은 개별 해시값을 가지며, 결과는 [파일경로, 해시값] 형태의 리스트로 반환된다.
bundle 파라미터를 통해 특정 폴더를 하나의 단위로 묶어서 계산 가능하다.

@log, @done_log 가 명시되어있는 주석은 해시 계산에서 제외된다.

## parameters

| 입력변수      | type   | default |
| ------------- | ------ | ------- |
| `dir_path`    | `str`  | -       |
| `bundle`      | `list` | `[]`    |
| `ignore_list` | `list` | `[]`    |

## return

| 출력 type | 설명                                                   |
| --------- | ------------------------------------------------------ |
| `list`    | [[파일경로, 해시값], ...] 형태의 2차원 리스트          |

## 사용예시

```python
from utilskit import hashutils as hu

# 기본 사용
result = hu.get_all_hash("/path/to/dir")
print(result)
"""
[
    ['/path/to/dir/file1.py', '13514451708f8c73e1e4d9f9fabf905412ab8bed65a2773f15ed697d9b769fe4'],
    ['/path/to/dir/file2.py', '6e826159f17ac96fda50f327f1b522230e1fe36bb5c1b1147e02480da8103682'],
    ['/path/to/dir/subdir/file3.py', 'a1b2c3d4e5f6...']
]
"""

# 특정 폴더를 하나의 단위로 묶기
result = hu.get_all_hash("/path/to/dir", bundle=["subdir"])
print(result)
"""
[
    ['/path/to/dir/file1.py', '13514451708f8c73e1e4d9f9fabf905412ab8bed65a2773f15ed697d9b769fe4'],
    ['/path/to/dir/file2.py', '6e826159f17ac96fda50f327f1b522230e1fe36bb5c1b1147e02480da8103682'],
    ['/path/to/dir/subdir', 'abc123def456...']  # subdir 전체가 하나의 해시로
]
"""

# 특정 파일 무시하기
result = hu.get_all_hash("/path/to/dir", ignore_list=["*.log", "temp.txt"])
```

## parameters detail

> `dir_path`  | type : `str`
>
> 해시를 계산할 디렉토리의 절대경로.
> 해당 디렉토리 내의 모든 파일을 순회하며 각각의 해시를 계산함.

> `bundle` | type: `list`
>
> 특정 폴더명을 지정하면 해당 폴더를 하나의 단위로 묶어서 dir2hash 를 통해 단일 해시를 계산함.
> 묶인 폴더의 하위 디렉토리는 순회하지 않음.
>
> ```python
> # 예시: logs 폴더 전체를 하나의 해시로 처리
> result = get_all_hash("/project", bundle=["logs"])
> # logs 폴더는 ['/project/logs', 'hash_value'] 하나의 항목으로 나타남
> ```

> `ignore_list` | type: `list`
>
> 해시 계산에서 제외할 파일명 또는 패턴 리스트.
> fnmatch 패턴을 지원하여 와일드카드 사용 가능 (예: *.log, temp*)
>
> ```python
> # 예시: 로그 파일과 임시 파일 제외
> result = get_all_hash("/path/to/dir", ignore_list=["*.log", "*.tmp", "__pycache__"])
> ```



# dir2hash

디렉토리(폴더)의 경로값을 입력받아 해당 폴더에 대한 하나의 통합 해시값을 추출하는 함수

해당 해시값은 "내부에 존재하는 모든 파일의 해시" 를 기준으로 계산됨.
파일 중 해시계산에서 무시할 대상을 지정 가능

@log, @done_log 가 명시되어있는 주석은 해시 계산에서 제외된다.

## parameters

| 입력변수      | type   | default |
| ------------- | ------ | ------- |
| `dir_path`    | `str`  | -       |
| `ignore_list` | `list` | `[]`    |

## return

| 출력 type | 설명                                  |
| --------- | ------------------------------------- |
| `str`     | 16진수로 표현된 64자리 hash 문자열 값 |

## 사용예시

```python
from utilskit import hashutils as hu
hash_string = hu.dir2hash("/path/to/dir")
print(hash_string)
print(len(hash_string))
"""
6e826159f17ac96fda50f327f1b522230e1fe36bb5c1b1147e02480da8103682
64
"""
```

```python
from utilskit.hashutils import dir2hash
hash_string = dir2hash("./test/log")
"""
6e826159f17ac96fda50f327f1b522230e1fe36bb5c1b1147e02480da8103682
"""
```



## parameters detail

> `dir_path`  | type : `str` 
>
> 해시를 계산하고자 하는 폴더의 명칭까지 포함한 절대경로값.
>

> `ignore_list`  | type : `str` 
>
> 폴더 해시 계산시 내부에서 제외할 파일명 리스트

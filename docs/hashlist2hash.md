

# hashlist2hash

해시값들의 리스트를 입력받아 하나의 통합 해시를 계산하는 함수.

여러 개의 해시값을 결합하여 단일 해시로 만들어준다.
빈 문자열은 자동으로 제거되며, 순서에 관계없이 동일한 해시 셋은 동일한 결과를 생성한다.

## parameters

| 입력변수    | type   | default |
| ----------- | ------ | ------- |
| `hash_list` | `list` | -       |

## return

| 출력 type | 설명                                                |
| --------- | --------------------------------------------------- |
| `str`     | 16진수로 표현된 64자리 통합 hash 문자열 값          |

## 사용예시

```python
from utilskit import hashutils as hu

# 여러 해시를 하나로 통합
hash_list = [
    "13514451708f8c73e1e4d9f9fabf905412ab8bed65a2773f15ed697d9b769fe4",
    "6e826159f17ac96fda50f327f1b522230e1fe36bb5c1b1147e02480da8103682",
    "a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890"
]
combined_hash = hu.hashlist2hash(hash_list)
print(combined_hash)
print(len(combined_hash))
"""
f8e9d7c6b5a4938271605948372615049382716059483726150493827160594837
64
"""

# 빈 리스트는 빈 문자열 반환
empty_hash = hu.hashlist2hash([])
print(empty_hash)  # ""

# 빈 문자열은 자동 제거
hash_list_with_empty = ["abc123...", "", "def456..."]
result = hu.hashlist2hash(hash_list_with_empty)
# "" 는 무시되고 나머지만 계산됨

# 순서와 무관하게 동일한 결과
hash1 = hu.hashlist2hash(["aaa", "bbb", "ccc"])
hash2 = hu.hashlist2hash(["ccc", "aaa", "bbb"])
print(hash1 == hash2)  # True
```

## parameters detail

> `hash_list`  | type : `list`
>
> 통합할 해시값들의 리스트.
> 각 요소는 문자열 형태의 해시값이어야 함.
>
> - 빈 리스트가 입력되면 빈 문자열("") 을 반환
> - 리스트 내의 빈 문자열("")은 자동으로 제거됨
> - 해시값들은 내부적으로 정렬되어 계산되므로 순서와 무관하게 동일한 결과 생성
> - 구분자('|')를 사용하여 'aa'+'b' 와 'a'+'ab' 가 다른 해시를 생성하도록 보장
>
> ```python
> # 예시: 여러 파일의 해시를 하나로 통합
> file_hashes = [
>     file2hash("/path/to/file1.py"),
>     file2hash("/path/to/file2.py"),
>     file2hash("/path/to/file3.py")
> ]
> combined = hashlist2hash(file_hashes)
>
> # get_all_hash 결과에서 해시값만 추출하여 통합
> all_hashes = get_all_hash("/path/to/dir")
> hash_values = [h[1] for h in all_hashes]  # 두 번째 요소(해시값)만 추출
> final_hash = hashlist2hash(hash_values)
> ```

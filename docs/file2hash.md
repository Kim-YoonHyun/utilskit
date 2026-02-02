

# file2hash

파일의 경로값을 입력받아 해당 파일의 "내용" 을 포함한 해시값을 추출하는 함수.

단, @log, @done_log 가 명시되어있는 주석은 해시 계산에서 제외된다.
그 외에도 무시할 키워드를 지정 가능하다.

## parameters

| 입력변수       | type   | default |
| -------------- | ------ | ------- |
| `file_path`    | `str`  | -       |
| `ignore_words` | `list` | `[]`    |

## return

| 출력 type | 설명                                  |
| --------- | ------------------------------------- |
| `str`     | 16진수로 표현된 64자리 hash 문자열 값 |

## 사용예시

```python
from utilskit import hashutils as hu
hash_string = hu.file2hash("/path/to/file")
print(hash_string)
print(len(hash_string))
"""
13514451708f8c73e1e4d9f9fabf905412ab8bed65a2773f15ed697d9b769fe4
64
"""
```

## parameters detail

> `file_path`  | type : `str` 
>
> 해시값을 계산할 파일 경로.
> 파일의 이름, 확장자 및 절대경로를 전부 삽입해줘야하며 상대경로는 의도치 않은 에러 발생 확률이 높음
>
> ```python
> """
> 예시 : /home/$USER/module/test.py
> """
> file_hash = file2hash("/home/$USER/module/test.py")  # 가장 정확
> file_hash = file2hash("/home/$USER/module")  # 대상이 파일이 아닌 폴더라서 에러 발생
> file_hash = file2hash("/home/$USER/module/test")  # 해당 파일 존재하지 않음 에러 발생
> file_hash = file2hash("./test.py")  # 작업 디렉토리 꼬임으로 인해 못찾을 확률 증가
> ```

> `ignore_words` | type: `list`
>
> 파일 해시를 계산할때 내부 문자열에서 특정 지정 키워드가 있으면 그 line 자체를 해시계산에서 제외하는 인자
> @log 와 @done_log 는 기본적으로 무시하게 설정되어있음
>
> ```python
> """ test.py 내용 예시
> def add(a, b):
>     return a + b
> """
> file_hash = file2hash("/path/to/test.py", ignore_words=["not"])
> print(file_hash)
>  --> 13514451708f8c73e1e4d9f9fabf905412ab8bed65a2773f15ed697d9b769fe4
> 
> """ test.py 내용 변경 예시
> # not : 이 주석은 해시변화에 적용되지 않습니다.
> def add(a, b):
>     return a + b
> """
> file_hash = file2hash("/path/to/test.py", ignore_words=["not"])
> print(file_hash)
>  --> 13514451708f8c73e1e4d9f9fabf905412ab8bed65a2773f15ed697d9b769fe4
> ```

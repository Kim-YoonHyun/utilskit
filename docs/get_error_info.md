# get_error_info

에러발생시의 에러 텍스트를 전부 str 형식으로 추출하여 반환하는 함수.

에러발생시 모듈이 바로 정지한다는 특성상 try~except 과 같은 예외처리시에만 활용 가능하다.

예외 발생시 에러메세지가 시스템상 출력되지 않더라도 기록 용도로 활용 가능하다.

## parameters

입력받는 변수는 별도로 존재하지 않음.

## return

| 출력 type | 설명                                              |
| --------- | ------------------------------------------------- |
| `str`     | 에러발생시에 출력되는 모든 텍스트를 저장한 문자열 |

## 사용예시

```python
from utilskit import utils as u

a = 1
b = '2'
try:
    c = a + b
except TypeError:
    error_info = u.get_error_info()
    print(error_info)
'''
Traceback (most recent call last):
  File "/home/kimyh/library/utilskit/test/test.py", line 314, in main13
    c = a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str
'''
```

### parameters detail

입력받는 변수는 별도로 존재하지 않음.


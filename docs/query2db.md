

# query2db

DB 를 지정한다음 해당 DB 에 대해서 SQL query 문을 보내는 함수.

DDL (Data Definition Language), DML (Data Manipulation Language), DCL (Data Control Language) 에 대한 모든 명령문을 보내는게 가능하지만

이는 함수 사용시에 지정하는 사용자(user) 의 권한에 의해 사용 불가능한 문법이 존재할 수 있다.

예) DCL 에 속하는 GRANT, REVOKE 등

## parameters

| 입력변수     | type   | default     |
| ------------ | ------ | ----------- |
| `query`      | `str`  | -           |
| `host`       | `str`  | -           |
| `port`       | `int`  | -           |
| `user`       | `str`  | -           |
| `password`   | `all`  | -           |
| `db_name`    | `str`  | -           |
| `charset`    | `str`  | `'utf8mb4'` |
| `autocommit` | `bool` | `True`      |

## return

| 출력 type | 설명                                 |
| --------- | ------------------------------------ |
| `all`     | query 에 의해 출력될 수 있는 결과값. |

## 사용예시

```python
from utilskit import dbutils as dbu
query = f"""
SELECT col1, col2 FROM table1 
WHERE col3='aaa'
"""
info = dbu.query2db(
    query=query,
    host='123.123.123.123',
    port=3306,
    user='user_id',
    passward='user_pw',
    db_name='DB_NAME'
)
print(info)
'''
(('value1', 'value2'),)
'''
'''
만약 출력값이 존재할 수 없는 query 문법(예: DELETE, UPDATE 등)의 경우 빈 리스트 [] 가 반환된다.
'''
```

## parameters detail

> `query`  | type : `str` 
>
> DB 에 대해 적용하고자 하는 SQL 문법 기반의 쿼리문.
>
> SELECT, UPDATE, INSERT, DELETE 와 같은 DML 을 사용하는 것이 가능하다.
>
> 그외의 DDL, DCL 등, 입력한 `user` 의 권한 범위에 따라 존재하는 모든 SQL 구문에 대해 적용가능하다.
>
> 단, 오류가 없는 적절한 SQL query 문을 적어야하며 함수 내부에서 SQL 문법에 대한 조정은 이루어지지 않는다.
>
> ※ 출력에 대한 주의점
>
> 1. query 에 따라서 이 함수의 출력값이 결정되며, SELECT 와 같은 출력이 존재하는 query 를 날릴 경우 작성한 문법에 대응하는 결과값이 출력되게 된다.
> 2. DELETE, UPDATE, INSERT 와 같은 DB 로부터의 출력 결과값이 존재하지 않는 query 문을 날릴 경우 출력은 항상 빈 리스트 `[]` 가 나온다.
>
> ```python
> # SELECT 구문 예시
> """
> SELECT * FROM table1
> WHERE col1 = 'a'
> """
> # UPDATE 구문 예시
> """
> UPDATE table1 set col1='a'
> WHERE col2='b'
> """
> ```

> `host`  | type : `str` 
>
> 접속하고자 하는 DB 의 host 주소. 예: 123.123.123.123

> `port` | type: `int`
>
> 접속하고자 하는 DB 가 구축되어있는 port 값

> `user` | type : `str`
>
> DB 에 접속할때 사용할 유저 ID

> `password` | type : `all`
>
> DB 에 접속할때 사용할 유저 ID 의 비밀번호

> `db_name` | type : `str`
>
> 접속할 DB 의 명칭

> `charset` | type : `str` | default : `'utf8mb4'`
>
> 접속할 DB 의 문자 인코딩 방식. 기본값은 보편적으로 가장 많이 쓰이는 `'utf8mb4'` 로 지정되어있으며 
>
> 아무런 값을 지정하지 않을 경우 자동으로 기본값으로 지정된다.

> `autocommit` | type : `bool` | default : `True`
>
> 입력한 쿼리문에 대해서 자동 커밋을 할지의 설정 여부. 기본값은 `True` 로 되어있으며 
>
> `True` 인 경우 쿼리문 마지막에 `;` 을 넣지 않아도 자동으로 커밋 된다.
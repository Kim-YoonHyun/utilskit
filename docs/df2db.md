# df2db

pandas dataframe 의 형태로 구성되어있는 데이터 변수를 column 명칭, data 값 을 포함해서 구성된 형태 그대로 DB 에 업로드하는 함수.

만약 존재하지 않는 table 에 업로드하는 경우 해당 table 이 새로 생성된다. 단, 새로 생성시킬 경우 그 table 에 대한 상세 설정을 하는 것은 불가능하다.

예를 들어 

```python
   col1  col2
0     1    a
1     2    b
```

위의 형태의 dataframe 변수가 있다고 가정하고 이 dataframe 을 'table1' 이라는 이름으로 DB 에 업로드했을때, 만약 기존 DB 에 table1 이라는 테이블이 존재하지 않은 경우 table1 이라는 테이블이 새로 생성된다. 이때, col1 은 `BIGINT`, col2 는 `TEXT` 와 같이 데이터 유형이 자동 설정된다. 이 데이터유형을 `int`, `VARCHAR` 등과 같이 바꾸는 것은 본 함수로는 불가능하며 자체적으로 DB 에 접속해서 조정을 해야한다.

하지만 만약 기존 DB 에 table1 이라는 테이블이 이미 존재할 경우, 그 테이블에 그대로 올라간다. 이때 만약 이미 설정되어있는 데이터유형과 업로드할 dataframe 의 데이터유형이 다를 경우 업로드가 불가능하다는 에러가 발생한다.

## parameters

| 입력변수    | type               | default     |
| ----------- | ------------------ | ----------- |
| `dataframe` | `pandas dataframe` | -           |
| `table`     | `str`              | -           |
| `host`      | `str`              | -           |
| `port`      | `int`              | -           |
| `user`      | `str`              | -           |
| `password`  | `all`              | -           |
| `db_name`   | `str`              | -           |
| `charset`   | `str`              | `'utf8mb4'` |
| `index`     | `bool`             | `'False'`   |

## return

| 출력 type | 설명                                |
| --------- | ----------------------------------- |
| -         | 본 함수는 출력값이 존재하지 않는다. |

## 사용예시

```python
from utilskit import dbutils as dbu
from utilskit import dataframeutils as dfu
df = dfu.read_df('./ex.csv')
dbu.df2db(
    df=df, 
    table='test_db', 
    host='123.123.123.123', 
    port=3306, 
    user='user_id', 
    password='user_pw', 
    db_name='db_name'
)
```

## parameters detail

> `dataframe`  | type : `pandas dataframe`
>
> DB 에 업로드하고자 하는 pandas dataframe 변수

> `table`  | type : `str` 
>
> dataframe 을 DB 에 업로드 할 시 적용할 테이블이름

> `host` | type : `str`
>
> 접속할 DB 의 호스트 주소

> `port` | type : `int`
>
> 접속할 DB 에 할당되어있는 port 값

> `user` | type : `str`
>
> DB 에 접속할 경우 사용할 유저 ID

> `password` | type : `all`
>
> DB 에 접속할 때 사용할 유저 ID 의 비밀번호

> `db_name` | type : `str`
>
> 접속할 DB 의 이름

> `charset` | type : `str`
>
> 접속할 DB 의 문자 인코딩 방식. 기본값은 보편적으로 가장 많이 쓰이는 `'utf8mb4'` 로 지정되어있으며 
>
> 아무런 값을 지정하지 않을 경우 자동으로 기본값으로 지정된다.

> `index` | type : `bool`
>
> dataFrame의 인덱스를 테이블에 함께 저장할지 여부. True/False 로 지정 가능하며 기본값은 False 이다.
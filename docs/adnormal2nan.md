# adnormal2nan

pandas datafram 의 입력한 컬럼에 대해 최대, 최소값을 벗어나는 값(초과, 미만)을 NaN 값으로 치환하는 함수

## parameters

| 입력변수    | type               | default |
| ----------- | ------------------ | ------- |
| `dataframe` | `pandas dataframe` | -       |
| `column`    | `str`              | -       |
| `max_value` | `int`, `float`     | `None`  |
| `min_value` | `int`, `float`     | `None`  |

## return

| 출력 type          | 설명                      |
| ------------------ | ------------------------- |
| `pandas dataframe` | 필터링이 적용된 dataframe |

## 사용예시

```python
import numpy as np
import pandas as pd
from utilskit import dataframeutils as dfu

value_ary1 = [1, 6, 3, 8, 5]
value_ary2 = [5, 7, 2, 6, 9]
df = pd.DataFrame({'col1':value_ary1, 'col2':value_ary2})
df = dfu.adnormal2nan(
    dataframe=df,
    column='col1',
    max_value=7,
    min_value=2
)
print(df)
'''
   col1  col2
0   NaN     5
1   6.0     7
2   3.0     2
3   NaN     6
4   5.0     9
'''
```

## parameters detail

> `dataframe` | type : `pandas dataframe` 
>
> 최대, 최소 필터링을 진행할 pandas dataframe

> `column` | type : `str`
>
> 최대, 최소 필터링을 진행할 pandas dataframe 의 컬럼 명

> `max_value` & `min_value` | type : `int`, `float` | default : `None`
>
> 입력한 컬럼의 데이터에 대해서 최대, 최소 필터링을 진행할 수치값.
>
> 지정하지 않거나 `None` 으로 설정하는 경우 필터링 하지 않는다.

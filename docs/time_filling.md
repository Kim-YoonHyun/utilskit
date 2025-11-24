# time_filling

지정한 범위 내의 모든 시간을 1초단위로 확장하여 채워넣는 함수. 확장 시 시간 외 컬럼은 NaN 값으로 채워짐.

## parameters

| 입력변수    | type               | default  |
| ----------- | ------------------ | -------- |
| `dataframe` | `pandas dataframe` | -        |
| `start`     | `str`              | -        |
| `end`       | `str`              | -        |
| `column`    | `str`              | `'time'` |

## return

| 출력 type          | 설명                         |
| ------------------ | ---------------------------- |
| `pandas dataframe` | 시간 확장이 적용된 dataframe |

## 사용예시

```python
import numpy as np
import pandas as pd
from datetime import datetime
from utilskit import dataframeutils as dfu

time_ary = ['2024-05-11 03:45:12', '2024-05-11 03:45:15', '2024-05-11 03:45:16']
value_ary = [1, 5, 6]
df = pd.DataFrame({
    'time':time_ary,
    'value':value_ary
})
print(df)
'''
                  time  value
0  2024-05-11 03:45:12      1
1  2024-05-11 03:45:15      5
2  2024-05-11 03:45:16      6
'''
df = dfu.time_filling(
    dataframe=df,
    start='2024-05-11 03:45:10',
    end='2024-05-11 03:45:20',
    column='time'
)
print(df)
'''
                   time  value
0   2024-05-11 03:45:10    NaN
1   2024-05-11 03:45:11    NaN
2   2024-05-11 03:45:12    1.0
3   2024-05-11 03:45:13    NaN
4   2024-05-11 03:45:14    NaN
5   2024-05-11 03:45:15    5.0
6   2024-05-11 03:45:16    6.0
7   2024-05-11 03:45:17    NaN
8   2024-05-11 03:45:18    NaN
9   2024-05-11 03:45:19    NaN
10  2024-05-11 03:45:20    NaN
'''
```

## parameters

> `dataframe`  | type : `pandas dataframe`
>
> 시간 확장을 적용할 데이터가 들어있는 pandas dataframe

> `start` & `end` | type : `str` 
>
> 시간 확장을 적용할 시 시작하는 시간.
>
> yyyy-mm-ss HH:MM:SS 의 형식으로 입력.
>
> 이때, end 는 항상 start 보다 미래의 시간이어야 한다.

> `column` | type : `str` | default : `'time'`
>
> 시간 확장을 적용할 시 dataframe 의 컬럼명

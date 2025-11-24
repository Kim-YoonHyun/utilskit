# fill_repeat_nan

일정 횟수 이상 반복되는 NaN 구간에 대해서만 앞뒤 채우기 방식으로 결측치를 채우는 함수. 매우 긴 결측치 자체가 이상 값이 아니고, 데이터 기록중간 짧은 결측구간이 있는 경우 등에 활용 가능.

## parameters

| 입력변수    | type               | default |
| ----------- | ------------------ | ------- |
| `dataframe` | `pandas dataframe` | -       |
| `column`    | `str`              | -       |
| `repeat`    | `int`              | 5       |

## return

| 출력 type          | 설명                      |
| ------------------ | ------------------------- |
| `pandas dataframe` | 결측치가 보정된 dataframe |

## 사용예시

```python
import pandas as pd
import numpy as np
from utilskit import dataframeutils as dfu

value_ary1 = [1, np.nan, np.nan, 2, 3, np.nan, np.nan, np.nan]
value_ary2 = np.random.randint(0, 10, size=len(value_ary1))
df = pd.DataFrame({
    'value1':value_ary1,
    'value2':value_ary2
})
print(df)
'''
   value1  value2
0     1.0       1
1     NaN       7
2     NaN       7
3     2.0       7
4     3.0       3
5     NaN       2
6     NaN       1
7     NaN       1
'''
df = dfu.fill_repeat_nan(
    dataframe=df,
    column='value1',
    repeat=3
)
print(df)
'''
   value1  value2
0     1.0       1
1     NaN       7
2     NaN       7
3     2.0       7
4     3.0       3
5     3.0       2
6     3.0       1
7     3.0       1
'''
```

## parameters

> `dataframe` | type : `pandas dataframe` 
>
> 결측치 보정을 진행할 dataframe.

>`column` | type : `str` 
>
>결측치의 반복 횟수를 계산하고 보정할 컬럼명.

> `repeat` | type : `int` | default : 5
>
> 보정할 결측치의 반복 횟수 기준. 입력한 값 이상 반복되면 해당 값은 우선 앞의 값으로 채워지고, 만약 앞의 값이 존재하지 않는 경우 뒤의 값으로 채워진다.
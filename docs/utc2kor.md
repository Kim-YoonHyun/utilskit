# utc2kor

pandas dataframe 에 기록된 datetime 타입의 데이터에 대해서 utc 시간대를 kor 시간대로 변경하는 함수.

## parameters

| 입력변수 | type               | default  |
| -------- | ------------------ | -------- |
| `df`     | `pandas dataframe` | -        |
| `column` | `str`              | `'time'` |
| `extend` | `bool`             | `True`   |

## return

| 출력 type          | 설명                           |
| ------------------ | ------------------------------ |
| `pandas dataframe` | 한국 시간대로 변경된 dataframe |

## 사용예시

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from utilskit import dataframeutils as dfu

start_time = datetime.strptime('2025-07-22 10:05:15', '%Y-%m-%d %H:%M:%S')
end_time = start_time + timedelta(seconds=5)
time_range = pd.date_range(start=start_time, end=end_time, freq='S')
value_ary = np.random.randint(10, 20, len(time_range))
df = pd.DataFrame({
    'time':time_range,
    'value':value_ary
})
df = dfu.utc2kor(
    dataframe=df, 
    column='time', 
    extend=True
)
print(df)
'''
                 time  value             time_kor
0 2025-07-22 10:05:15     18  2025-07-22 19:05:15
1 2025-07-22 10:05:16     14  2025-07-22 19:05:16
2 2025-07-22 10:05:17     16  2025-07-22 19:05:17
3 2025-07-22 10:05:18     15  2025-07-22 19:05:18
4 2025-07-22 10:05:19     15  2025-07-22 19:05:19
5 2025-07-22 10:05:20     15  2025-07-22 19:05:20
'''
```

## parameters detail

> `dataframe` | type : `pandas dataframe` 
>
> 변경할 utc 시간 데이터가 포함되어있는 pandas dataframe 
>
> ```python
>      time  value
> 0 2025-07-22 10:05:15     16
> 1 2025-07-22 10:05:16     10
> 2 2025-07-22 10:05:17     18
> 3 2025-07-22 10:05:18     13
> 4 2025-07-22 10:05:19     13
> 5 2025-07-22 10:05:20     13
> ```

> `column` | type : `str` | default : `'time'`
>
> 한국시간대로 변경하기 위해 입력할 UTC 시간대로 이루어져 있는 데이터 컬럼명.
>
> 이때 해당 컬럼 값은 python 의 `datetime` 형식이어야 하며 `str` 타입인 경우 에러 발생 가능성 존재.

> `extend` | type : `bool` | default : `True`
>
> 새로운 컬럼에 생성할지 기존 컬럼에 덮어쓸지 설정.
>
> True 인 경우 새로운 컬럼으로 확장시켜 생성하고 False 인 경우 기존 컬럼에 덮어쓴다.
>
> 새로운 컬럼의 명칭은 `입력한 컬럼명_kor` 이다.

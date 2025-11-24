# isdfvalid

`pandas dataframe` 이 입력한 컬럼 리스트를 전부 지니고 있는지 여부를 판단하여 True, False 를 출력하는 함수

## parameters

| 입력변수      | type               | default |
| ------------- | ------------------ | ------- |
| `dataframe`   | `pandas dataframe` | -       |
| `column_list` | `list`             | -       |

## return

| 출력 type | 설명                                            |
| --------- | ----------------------------------------------- |
| `bool`    | 입력한 컬럼의 존재 여부에 따른 True, False 출력 |

## 사용예시

```python
import pandas as pd
from utilskit import dataframeutils as dfu

df = pd.DataFrame([1, 2, 3, 4], columns=['value'])
if dfu.isdfvalid(df, ['value']):
    print('컬럼이 전부 존재합니다.')
'''
컬럼이 전부 존재합니다.
'''
```

## parameters detail

> `datafrmae`  | type : `pandas dataframe` 
>
> 컬럼 유무를 확인할 pandas dataframe.

> `column_list` | type : `list`
>
> dataframe 에 존재하는지 여부를 확인할 컬럼명 list.

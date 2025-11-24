# get_section

입력한 데이터에 대해서 반복되는 구간을 추출할 수 있는 함수.

반복하는 횟수를 계산할 기준값, 반복 횟수, 반복횟수에 대한 이상/이하/동일 여부, 특정 구간에 대한 반복 여부, 이상/이하/초과/미만 적용, NaN 포함, 구간 반전 기능을 제공하며 값의 기준과 반복기준에 대한 설정을 다양하게 적용할 수 있다.

예1) 데이터상의 모든 값에 대해서 10번 이상 반복되는 경우를 전부 산출

예2) 기준값 5가 7번 이상 반복되는 구간 산출

예2) 1이상 3이하의 값이 정확히 10번 반복되는 구간 산출

예3) 10 을 초과하는 값이 5번 이하 반복되는 구간에 대한 반전 구간 산출

예4) 결측치(nan)가 600번 이상 반복되는 구간 산출

## parameters

| 입력변수     | type               | default |
| ------------ | ------------------ | ------- |
| `data`       | `list`, `np.array` | -       |
| `repeat`     | `int`              | -       |
| `mode`       | `str`              | `'a'`   |
| `key`        | `all`              | `None`  |
| `max_key`    | `int`, `float`     | `None`  |
| `min_key`    | `int`, `float`     | `None`  |
| `between`    | `bool`             | `False` |
| `max_equal`  | `bool`             | `True`  |
| `min_equal`  | `bool`             | `True`  |
| `except_nan` | `bool`             | `True`  |
| `reverse`    | `bool`             | `False` |

## return

| 출력 type | 설명                                                         |
| --------- | ------------------------------------------------------------ |
| `dict`    | 기준값을 key, 반복구간 tuple 로 구성된 list 를 value 로 지닌 dict |

## 사용예시

```python
import numpy as np
from utilskit import repeatutils as rpu
data = np.array(
    [
        1, 1, 1, 1, 1,  # 0 ~ 4
        2, 2, 2, 2,     # 5 ~ 8
        3, 3,           # 9 ~ 10
        4, 4, 4,        # 11 ~ 13
        np.nan, np.nan, np.nan, np.nan,  # 14 ~ 17
        1, 1, 1, 1,     # 18 ~ 21
        3, 4, 5,        # 22 ~ 24
        np.nan, np.nan, np.nan, np.nan, np.nan, # 25 ~ 29
        1, 1, 1, 1, 1, 1, 1,    # 30 ~ 36
        np.nan, np.nan, np.nan  # 37 ~ 39
    ]
)
# 필수변수만 활용
result = rpu.get_section(
    data, 
    repeat=4
)
print(result)
'''
모든 변수값에 대해서 4번 이상 반복되는 구간을 전부 
{'1.0': [(0, 4), (18, 21), (30, 36)], '2.0': [(5, 8)]}
'''
```

```python
# 모든 변수를 활용1
result = rpu.get_section(
    data, 
    repeat=4,
    mode='e',   # 반복횟수 일치
    key=1,  # 기준값은 1
    except_nan=False,   # NaN 도 포함
    reverse=False   # 반전 없음
)
print(result)
'''
기준값 1이 정확히 4번 반복되는 구간 산출
{'1.0': [(18, 21)]}
'''
```

```python
# 모든 변수를 활용2
result = rpu.get_section(
    data, 
    repeat=4,
    mode='a',   # 반복횟수 이상
    # key=1,  # 최대 최소 범위 지정시 무시된다.
    max_key=3,  # 최대 3
    min_key=2,  # 최소 2
    between=True,   # 사잇값
    max_equal=True, # 3 이하
    min_equal=True, # 2 이상
    # except_nan=False,   # 최대 최소 범위 지정시 무시된다.
    reverse=False   # 반전 없음
)
print(result)
'''
2이상 3이하의 값이 4번 이상 반복되는 구간 산출
{'2_3': [(5, 10)]}
'''
```

## parameters detail

> `data`  | type : `list`, `np.array` 
>
> 반복되는 구간을 산출할 데이터 리스트. 데이터 내부의 값의 형식은 정해져 있지 않고 뭐든지 가능하다.

> `repeat`  | type : `int` 
>
> 계산할 구간에 대한 반복횟수 기준. 1이하 값의 경우 반복한다고 할 수 없기에 최소 2 이상의 값을 입력해야한다.

> `mode` | type : `str` | default : `'a'` | limit : `'a'`, `'b'`, `'e'`
>
> 입력한 반복횟수 기준 이상(a: above), 이하(b:below) 및 동일(e: equal) 여부를 결정하는 변수.
>
> `'a'`, `'b'`, `'e'` 3개의 값만 입력 가능하며 그 외의 값을 입력할 경우 에러 발생

```python
result = rpu.get_section(
    data, 
    repeat=4,
    mode='a'	# 기본값
)
'''
같은 값이 4번 이상반복되는 구간 전부 산출
{'1.0': [(0, 4), (18, 21), (30, 36)], '2.0': [(5, 8)]}
'''
```

```python
result = rpu.get_section(
    data, 
    repeat=4,
    mode='b'
)
'''
같은 값이 4번 이하 반복되는 구간 전부 산출
{'2.0': [(5, 8)], '3.0': [(9, 10)], '4.0': [(11, 13)], '1.0': [(18, 21)]}
'''
```

```python
result = rpu.get_section(
    data, 
    repeat=4,
    mode='e'
)
'''
같은 값이 정확히 4번 반복되는 구간 산출
{'2.0': [(5, 8)], '1.0': [(18, 21)]}
''''
```

> `key` | type : `all` | default : `None`
>
> 반복구간을 계산할때 반복되는 기준값. 예를 들어 key = 1 로 지정하면 1 이라는 값에 대해서만 반복구간을 계산한다.
>
> NaN 에 대한 반복구간을 계산하고 싶은 경우 `np.nan` 또는 `'nan'` 로 지정하면 된다. 단, `except_nan` 을 반드시 `False` 로 지정해야한다.
>
> 만약 `max_key` 또는 `min_key` 를 지정할 경우 `key` 변수는 어떤값을 지정해도 무시된다.
>
> ```python
> result = rpu.get_section(
> data, 
> repeat=4,
> key=1,  
> )
> print(result)
> '''
> 기준값 1이 4번 이상 반복되는 구간 산출
> {'1.0': [(0, 4), (18, 21), (30, 36)]}
> '''
> ```
>
> ```python
> result = rpu.get_section(
> data, 
> repeat=4,
> key='nan',
> except_nan=False,
> )
> '''
> 결측치가 4번이상 반복되는 구간 산출
> {'nan': [(14, 17), (25, 29)]}
> '''
> ```

> `max_key` | type : `int`, `float` | default : `None`
>
> 반복구간을 계산할때의 최대 기준값. `between` 및 `max_equal` 의 값에 따라 이상/이하/초과/미만 의 여부가 결정되며 기본값은 **입력된 값 이상**으로 되어있다.
>
> 이상, 이하 연산을 하는 특성상 해당 변수는 반드시 숫자값이 들어와야한다.
>
> 만약 `max_key=3` 으로 지정한 경우 3 이상의 값을 기준으로 구간을 산정한다. 이때 예를 들어 3, 3, 3, 4, 5, 6 이라는 구간이 있다면 4, 5, 6 은 각각 하나씩이라 구간 계산에서 제외되는 것이 **아니라** 3, 3, 3, 4, 5, 6 전체를 '3이상' 구간으로 한번에 계산하여 해당구간은 3이상의 값이 총 6번 반복되는것으로 판정된다.
>
> 결과의 key 값은 `{max_key}_over` 로 변경된다.
>
> ```python
> data = np.array([
> ...
> 3, 3,           # 9 ~ 10
> 4, 4, 4,        # 11 ~ 13
> ...
> ])
> result = rpu.get_section(
> data, 
> repeat=4,
> max_key=3
> )
> '''
> 3이상의 값이 4번 이상 반복되는 구간 산출
> {'3.0_over': [(9, 13)]}
> '''
> ```

> `min_key` | type : `int`, `float` | default : `None`
>
> 반복구간을 계산할때의 최소 기준값. `between` 및 `min_equal` 의 값에 따라 이상/이하/초과/미만 의 여부가 결정되며 기본값은 **입력된 값 이하**로 되어있다.
>
> 이상, 이하 연산을 하는 특성상 해당 변수는 반드시 숫자값이 들어와야한다.
>
> 만약 `min_key=2` 으로 지정한 경우 2 이하의 값을 기준으로 구간을 산정한다. 이때 예를 들어 0, 1, 2, 2, 2, 2 라는 구간이 있다면 0, 1 는 각각 하나씩이라 구간 계산에서 제외되는 것이 **아니라** 0, 1, 2, 2, 2, 2 전체를 '2이하' 구간으로 한번에 계산하여 해당구간은 2이하의 값이 총 6번 반복되는것으로 판정된다.
>
> 결과의 key 값은 `{min_key}_under` 로 변경된다.
>
> ```python
> data = np.array([
> 1, 1, 1, 1, 1,  # 0 ~ 4
> 2, 2, 2, 2,     # 5 ~ 8
> 	...
> 1, 1, 1, 1,     # 18 ~ 21
> ...
> 1, 1, 1, 1, 1, 1, 1,    # 30 ~ 36
> ])
> 
> result = rpu.get_section(
> data, 
> repeat=4,
> min_key=2
> )
> '''
> 2이하의 값이 4번이상 반복되는 구간 산출
> {'2.0_under': [(0, 8), (18, 21), (30, 36)]}
> '''
> ```

> `between`  | type : `bool` | default : `False`
>
> 최대(`max_key`) 및 최소(`min_key`) 기준값을 지정했을 때, 그 사잇값을 구할것인지의 여부를 결정하는 변수. 기본적으로는 `False` 로 되어있기에 최대 이상, 최소 이하를 계산하게되며 만약 `True` 로 지정한 경우 최소 ~ 최대의 사잇값을 기준으로 구간을 계산하게 된다.
>
> 이상/초과/이하/미만 여부는 `max_equal`, `min_equal` 에 의해 결정되며, 만약 `between` 을 `True` 로 한 경우 사잇값이라는 특성 상 `max_key` 와 `min_key` 가 전부 지정되어 있어야 하며 그렇지 않은 경우 에러가 발생한다.
>
> 결과의 key 값은 `{min_key}_{max_key}` 로 변경 된다.
>
> ```python
> data = np.array([
> 	...
> 2, 2, 2, 2,     # 5 ~ 8
> 3, 3,           # 9 ~ 10
> 	...
> ])
> 
> result = rpu.get_section(
> data, 
> repeat=4,
> max_key=3,
> min_key=2,
> between=True
> )
> '''
> 2이상 3이하의 값이 4번이상 반복되는 구간 산출
> {'2_3': [(5, 10)]}
> '''
> ```

> `max_equal` , `min_equal` | type : `bool` | default : `True`
>
> 최대, 최소 기준값을 설정할때 해당 값을 반복구간 계산에 포함할지 여부.
>
> 기본값은 `True` 로 되어있으며 이상/이하 로 계산하도록 한다.
>
> `False` 로 지정할 경우 초과/미만 으로 계산하도록 한다.
>
> ```python
> data = np.array([
> 	...
> 2, 2, 2, 2,     # 5 ~ 8
> 3, 3,           # 9 ~ 10
> 	...
> ])
> 
> result = rpu.get_section(
> data, 
> repeat=4,
> max_key=3,	
> min_key=2,
> between=True,
> max_equal=False,
> min_equal=True 	# 기본값
> )
> '''
> 2이상 3미만의 값이 4번이상 반복되는 구간 산출
> {'2_3': [(5, 8)]}
> '''
> ```

> `except_nan` | type : `bool` | default : `True`
>
> 반복구간을 계산할 값의 범위에 NaN 값을 포함시킬지 여부. 기본적으로 계산범위에 NaN 은 넣지 않는다.
>
> 단, `key` 값을 `np.nan` 또는 `'nan'` 으로 지정한 경우 계산범위에서 제외시킨경우 에러가 발생하므로 `False` 로 지정해주어야 한다.
>
> ```python
> data = np.array([
> 1, 1, 1, 1, 1,  # 0 ~ 4
> 2, 2, 2, 2,     # 5 ~ 8
> ...
> np.nan, np.nan, np.nan, np.nan,  # 14 ~ 17
> 1, 1, 1, 1,     # 18 ~ 21
> 	...
> np.nan, np.nan, np.nan, np.nan, np.nan, # 25 ~ 29
> 1, 1, 1, 1, 1, 1, 1,    # 30 ~ 36
> ...
> ])
> 
> result = rpu.get_section(
> data, 
> repeat=4,
> except_nan=False
> )
> '''
> 결측치를 포함하여 같은 값이 4번이상 반복되는 구간 전부 산출
> {'nan': [(14, 17), (25, 29)], '1.0': [(0, 4), (18, 21), (30, 36)], '2.0': [(5, 8)]}
> '''
> ```

> `reverse` | type : `bool` | default : `False`
>
> 계산한 구간에 대한 반전 구간을 계산하도록 하는 변수. 
>
> 반복 구간 계산시에 적용된 모든 설정에 대해서 최종적으로 나온 구간 결과값에 대한 반전을 진행하며 모든 `key` 값은 `{key}_rev` 로 변경된다.
>
> ```python
> result = rpu.get_section(
> data, 
> repeat=4,
> except_nan=False,
> reverse=True
> )
> '''
> 결측치가 4번 이상 반복되는 구간의 반전구간 산출
> {'nan': [(14, 17), (25, 29)], '1.0': [(0, 4), (18, 21), (30, 36)], '2.0': [(5, 8)]} 
> -->
> {'nan_rev': [(0, 13), (18, 24), (30, 39)], '1.0_rev': [(5, 17), (22, 29), (37, 39)], '2.0_rev': [(0, 4), (9, 39)]}
> '''
> ```
>
> ```python
> result = rpu.get_section(
> data, 
> repeat=4,
> max_key=3,
> min_key=2,
> reverse=True
> )
> '''
> # 2이상 3이하의 값이 4번이하 반복되는 구간의 반전구간 산출
> {'3.0_over': [(9, 13)], '2.0_under': [(0, 8), (18, 21), (30, 36)]}
> -->
> {'3.0_over_rev': [(0, 8), (14, 39)], '2.0_under_rev': [(9, 17), (22, 29), (37, 39)]}
> '''
> ```

# 
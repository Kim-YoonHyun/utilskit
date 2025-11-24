### `def` confusion_matrix

정답 리스트와 예측 리스트를 입력받아 confusion matrix 를 생성하는 함수.

#### parameters 

| 입력변수     | type               | defalut |
| ------------ | ------------------ | ------- |
| `class_dict` | `dict`             | -       |
| `true_list`  | `list`, `np.array` | -       |
| `pred_list`  | `list`, `np.array` | -       |
| `ignore_idx` | `None`, `int`      | `None`  |
| `round_num`  | `int`              | 2       |
| `percentage` | `bool`             | `True`  |

#### return

| 출력 type          | 설명                                      |
| ------------------ | ----------------------------------------- |
| `pandas dataframe` | confusion matrix 의 형태를 지닌 dataframe |

#### 사용예시

```python
from utilskit import classificationutils as clu

id2label_dict = {0:'고양이', 1:'개'}
t = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
p = [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]

print(type(id2label_dict))
cm = clu.confusion_matrix(
    class_dict=id2label_dict,
    true_list=t,
    pred_list=p,
    ignore_idx=None,
    round_num=2,
    percentage=True
)
print(cm)
'''
           고양이     개 accuracy  precision  recall  f1 score  count     0
고양이        8.0   4.0     None       73.0    67.0     69.87   12.0   NaN
개          3.0   6.0     None       60.0    67.0     63.31    9.0   NaN
count     11.0  10.0     None        NaN     NaN       NaN    NaN   NaN
accuracy   NaN   NaN      NaN        NaN     NaN       NaN    NaN  67.0
'''
```

#### parameters detail

>  `class_dict` | type : `dict`
>
>  입력된 데이터에 따라 사전의 key값을 맞추어 입력해야한다.
>
>  ```python
>  list = [0, 0, 0, 1, 1]
>  dict = {0:"고양이", 1:"개"}
>  # Valid
>  ```
>
>  만약 데이터는 정수형 (id) 인데 사전의 key 는 문자열 (label) 인 경우 에러가 발생한다.
>
>  ```python
>  list = [0, 0, 0, 1, 1]
>  dict = {"고양이":0, "개":1}
>  # Error
>  ```
>
>  데이터의 unique 값이 사전 key 값 의 부분집합이 아닌 경우 에러가 발생한다.
>
>  ```python
>  list = [0, 0, 1, 1, 2]
>  dict = {0:"고양이", 2:"개"}
>  # Error
>  ```
>
>  confusion matrix 를 만들고자 하는 정답(true_list) 및 예측(pred_list) 데이터.
>
>  데이터는 동일한 데이터 타입을 지니고 있어야한다. 타입만 동일하다면 내부의 값은 달라도 상관없다.
>
>  ```python
>  true_list = [0, 1, 1, 1, 0]
>  pred_list = [0, 0, 1, 1, 2]
>  # Valid
>  ```
>
>  데이터 타입이 다른 경우 에러가 발생한다.
>
>  ```python
>  true_list = [0, 1, 1, 1, 0]
>  pred_list = ['고양이', '개', '개', '고양이', '고양이']
>  # Error
>  ```

>  `ignore_idx` | type: `None` or `int` | default : `None`
>
>  confusion matrix 를 생성할시 무시할 id 값.
>
>  입력된 데이터가 정수형(id) 인 경우만 작동한다.
>
>  ```python
>  true_list = [0, 2, 1, 1, 0]
>  ignore_idx = 2
>  # 2 는 무시
>  ```

>  `round_num` | type : `int` | default : 2
>
>  결과를 표시할시 표시할 소숫점 자릿수

> `percentage` | type : `bool` | default : `True`
>
> 결과를 표시할 시 백분률을 적용할것인지 여부
>
> ```python
> percentage = True --> 67.32
> percentage = False --> 0.67
> ```


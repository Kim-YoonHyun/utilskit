# draw_subplot

하나의 이미지 내에 subplot 을 생성하여 복수의 그래프를 나열하는 함수.

기본적으로 서브 그래프들은 아래로 나열한다.

현재는 서브 그래프 각각에 대한 스타일 적용은 불가능하다.

## parameters

| 입력변수           | type    | default |
| ------------------ | ------- | ------- |
| `sub_title_list`   | `list`  | -       |
| `x_list`           | `list`  | -       |
| `y_list`           | `list`  | -       |
| `sub_row_idx`      | `int`   | `None`  |
| `sub_col_idx`      | `int`   | 1       |
| `x_range_list`     | `list`  | `None`  |
| `y_range_list`     | `list`  | `None`  |
| `fig_size`         | `tuple` | `None`  |
| `title_font`       | `int`   | 13      |
| `x_font`           | `int`   | 13      |
| `y_font`           | `int`   | 13      |
| `focus_list`       | `list`  | `None`  |
| `focus_color_list` | `list`  | `None`  |
| `alpha_list`       | `list`  | `None`  |
| `save_path`        | `str`   | `None`  |
| `save_name`        | `str`   | `None`  |

## return

| 출력 type      | 설명 |
| -------------- | ---- |
| return 값 없음 |      |

## 사용예시

```python
# 필수 변수만 활용
import numpy as np
from utilskit import plotutils as plu
np.random.seed(42)
x = np.arange(100)
data = np.random.randint(5, 20, size=100)
data1 = np.random.randint(0, 50, size=100)
data2 = np.random.randint(80, 90, size=100)

plu.draw_subplot(
    sub_title_list=['data', 'data1', 'data2'],
    x_list=[x, x, x],
    y_list=[data, data1, data2]
)
```

![sub_simple](plot_explain_images\sub_simple.png)

```python
# 모든 변수 활용
import numpy as np
from utilskit import plotutils as plu
np.random.seed(42)
x = np.arange(100)
data = np.random.randint(5, 20, size=100)
data1 = np.random.randint(50, 90, size=100)
data2 = np.random.randint(180, 190, size=100)

plu.draw_subplot(
    # 기본
    sub_title_list=['data', 'data1', 'data2'],
    x_list=[x, x, x],
    y_list=[data, data1, data2],
    # 서브 플롯의 위치
    sub_row_idx=3,
    sub_col_idx=1,
    # 이미지크기, 값 범위
    fig_size=[30, 5*3],
    x_range_list=[(0, 100), (-10, 110), (-20, 120)],
    y_range_list=[(-10, 100), (-10, 100), (150, 240)],
    title_font=30,
    x_font=30,
    y_font=30,
    focus_list=[(22, 27), (42, 53), (70, 76)],
    focus_color_list=['red', 'red', 'blue'],
    alpha_list=[0.1, 0.5, 1],
    save_path='./sub_image',
    save_name='sub_custom'
)
```

![sub_custom](plot_explain_images\sub_custom.png)

### parameters detail

기본

> `sub_title_list`  | type : `list` 
>
> 각 서브플롯에 명시할 제목. 순서에 따라 적용된다.

> `x_list` | type : `list`
>
> 각 서브플롯에 적용될 x 값 리스트. 순서에 따라 적용된다.

> `y_list` | type : `list`
>
> 각 서브플롯에 적용될 y 값 리스트. 순서에 따라 적용된다.

서브 플롯의 위치

> `sub_row_idx` | type : `int` | default : `None`
>
> 서브 플롯을 위치시킬 행 공간 index. 지정하지 않는 경우 기본적으로 입력된 데이터리스트의 갯수만큼 행이 늘어난다.

> `sub_col_idx` | type : `int` | default : 1
>
> 서브 플롯을 위치시킬 열 공간 index. 기본적으로 1의 값을 지닌다.

![row_col](plot_explain_images\row_col.png)

이미지 크기, 값 범위

> `fig_size` | type : `tuple` | default : `None`
>
> 전체 이미지의 크기(비율) 을 설정. 각 서브플롯 마다 적용되는 것이 아니라 전체에 적용되기에, 서브플롯의 위치에 따라 설정해줘야한다.
>
> 예를 들어 3개의 서브플롯을 3행으로 표현했을때, 각 행의 비율을 30, 5 로 해주고 싶다면 fig_size 의 값은 30, 15 (5 X 3) 으로 해줘야한다.

> `x_range_list` | type : `list` | default : `None`
>
> 각 서브 플롯의 x 값의 범위. 각각 지정 가능

> `y_range_list` | type : `list` | default : `None`
>
> 각 서브 플롯의 y 값의 범위. 각각 지정 가능.

![row_col_fig](plot_explain_images\row_col_fig.png)

 폰트

> `title_font` | type : `int` | default : 13
>
> 각 서브플롯 제목 폰트 크기 설정

> `x_font` | type : `int` | default : 13
>
> 각 서브플롯 x축 값의 폰트 크기 설정

> `y_font`  | type : `int` | default : 13
>
> 각 서브플롯 y 축 값의 폰트 크기 설정

![sub-font](plot_explain_images\sub-font.png)

구역 강조

> `focus_list` | type : `list` | default : `None`
>
> 강조 구역의 (시작, 끝) 형식의 tuple 로 구성된 list. 이때 강조 구역은 서브플롯별로 구분이 불가능하며 모든 서브플롯에 동일하게 적용된다.

> `focust_color_list` | type : `list` | default : `None`
>
> focus_list 에 설정한 각 강조 구역의 색을 설정. 색은 공통 색깔 설정 가능

> `alpha_list` | type : `list` | default : `None`
>
> focus_list 에 설정한 각 강조 구역의 색에 대한 투명도 설정. 0~1 사이의 값으로 설정하며 0에 가까울 수록 투명해진다.

![sub-focus](plot_explain_images\sub-focus.png)

저장

> `save_path` | type : `str` | default : `None`
>
> 저장경로 설정. 만약 아무런 설정을 하지 않거나 None 으로 설정한 경우 이미지를 저장하지 않는다.

> `save_name` | type : `str` | default : `None`
>
> 저장경로 설정시 저장할 이미지 파일의 이름. 만약 경로를 설정하지 않는다면 해당 변수는 아무런 의미를 지니지 않는다.
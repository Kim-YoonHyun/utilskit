# draw_plot

`matplotlib` 기반의 이미지 생성 과정에 대한 편의성을 높이고 상세 제어를 통해 원하는 형식의 이미지를 그리고 저장하는 기능을 제공

## parameters

| 입력변수              | type               | default     |
| --------------------- | ------------------ | ----------- |
| `title`               | `str`              | -           |
| `x`                   | `list`, `np.array` | -           |
| `y`                   | `list`, `np.array` | -           |
| `fig_size`            | `tuple`, `list`    | `None`      |
| `x_range`             | `tuple`, `list`    | `None`      |
| `y_range`             | `tuple`, `list`    | `None`      |
| `x_label`             | `str`              | `None`      |
| `y_label`             | `str`              | `None`      |
| `legend`              | `bool`             | `False`     |
| `title_font`          | `int`              | 13          |
| `x_font`              | `int`              | 13          |
| `y_font`              | `int`              | 13          |
| `x_label_font`        | `int`              | 13          |
| `y_label_font`        | `int`              | 13          |
| `line_style`          | `str`              | `'default'` |
| `line_size`           | `str`              | `'default'` |
| `line_color`          | `str`              | `'default'` |
| `marker_style`        | `str`              | `'default'` |
| `marker_size`         | `str`              | `'default'` |
| `marker_color`        | `str`              | `'default'` |
| `marker_border_size`  | `str`              | `'default'` |
| `marker_border_color` | `str`              | `default`   |
| `add_x_list`          | `list`             | `None`      |
| `add_y_list`          | `list`             | `None`      |
| `add_color_list`      | `list`             | `None`      |
| `focus_list`          | `list`             | `None`      |
| `focus_color_list`    | `list`             | `None`      |
| `alpha_list`          | `list`             | `None`      |
| `save_path`           | `str`              | `None`      |

## return

| 출력 type      | 설명 |
| -------------- | ---- |
| return 값 없음 | -    |

## 사용 예시

```python
# 필수 변수만 입력
import numpy as np
from utilskit import plotutils as plu
np.random.seed(42)
x = np.arange(100)
data = np.random.randint(5, 20, size=100)
    
plu.draw_plot(
    title='ex', 
    x=x, 
    y=data
)
```

![basic](plot_explain_images\basic.png)

```python
# 모든 변수 활용
import numpy as np
from utilskit import plotutils as plu
np.random.seed(42)
x = np.arange(100)
data = np.random.randint(5, 20, size=100)
data1 = np.random.randint(5, 20, size=100)
data2 = np.random.randint(5, 20, size=100)
    
plu.draw_plot(
    # 기본
    title='whole', x=x, y=data, 
    # 이미지 크기, 값 범위
    fig_size=(30, 8), x_range=(-10, 120), y_range=(0, 25), 
    # 라벨링
    x_label='x data', y_label='y data', legend=True,
    # 폰트 - 기본
    title_font=25, x_font=15, y_font=15,
    # 폰트 - 라벨
    x_label_font=23, y_label_font=23,
    # 선 스타일
    line_style='dash', line_size=5, line_color='cyan',
    # 마커 스타일
    marker_style='circle', marker_size=10, marker_color='white',
    # 마커 테두리 스타일
    marker_border_size=2, marker_border_color='black',
    # 추가 그리기 값
    add_x_list=[x, x],
    add_y_list=[data1, data2],
    add_color_list=['red', 'violet'],
    # 구역 강조
    focus_list=[(22, 27), (42, 53), (70, 76)],
    focus_color_list=['blue', 'red', 'violet'],
    alpha_list=[0.5, 0.75, 1],
    # 저장
    save_path='./image'
)
```

![basic](plot_explain_images\whole.png)

## parameters detail

색깔

>  모든 색깔 변수에 대해서 공통적용 가능
>
>  default, blue, green, red, cyan, magenta, yellow, black, white, orange, pink, khaki, gold, skyblue, navy, lightgreen, olive, violet, gray, brown

기본 구역

> `title`  | type : `str` 
>
> 이미지의 타이틀

> `x` | type : `list` 
>
> 그래프의 x 값 리스트

> `y` : type : `list`, `np.array`
>
> 그래프의 y 값 리스트

이미지 크기 & 값 범위

> `fig_size` & `x_range` & `y_range` | type : `tuple` | default : `None`
>
> 이미지의 가로 세로의 길이(비율)
>
> 이미지에 표시될 x 값의 범위
>
> 이미지에 표시될 y 값의 범위

```python
plu.draw_plot(
    title='fig', x=x, y=data, 
    fig_size=(30, 8), 
    x_range=(-10, 120), 
    y_range=(0, 25), 
)
```

![fig](plot_explain_images\fig.png)

라벨링

> `x_label` & `y_label` | type : `str` | default : `None`
>
> x 및 y 에 대한 라벨 명칭

> `legend` | type : `bool` | default : `False`
>
> 라벨의 legend 를 표시할지의 여부

```python
plu.draw_plot(
    title='label', x=x, y=data, 
    x_label='x data', 
    y_label='y data', 
    legend=True
)
```

![label](plot_explain_images\label.png)

폰트 - 기본

> `title_font`, `x_font`, `y_font` | type : `int` | default : 13
>
> 제목 글자 크기
>
> x 축 수치 글자 크기
>
> y 축 수치 글자 크기

```python
plu.draw_plot(
    title='font-basic', x=x, y=data, 
    title_font=25, 
    x_font=20, 
    y_font=20
)
```

![font-basic](plot_explain_images\font-basic.png)

폰트 - 라벨

> `x_label_font`, `y_label_font` | type : `int` | default : 13
>
> x 라벨 글자 크기
>
> y 라벨 글자 크기

```python
plu.draw_plot(
    title='font-label', x=x, y=data, 
    x_label_font=23, 
    y_label_font=23
)
```

![font-label](plot_explain_images\font-label.png)

선 스타일

> `line_style` | type : `str` | default : `'default'`
>
> 선의 스타일
>
> | 입력값       | 형태     |
> | ------------ | -------- |
> | `'default'`  | 기본(선) |
> | `'line'`     | 선       |
> | `'dash'`     | 점선     |
> | `'dot'`      | 점       |
> | `'dast-dot'` | 선 + 점  |

> `line_size` | type : `int` | default : `'default'`
>
> 선의 굵기 값

> `line_color` | type : `str` | default : `'default'`
>
> 선의 색. 공통 색깔 변수 적용 가능.

```python
plu.draw_plot(
    title='line', x=x, y=data, 
    line_style='dash', 
    line_size=3, 
    line_color='red'
)
```

![line](plot_explain_images\line.png)

마커 스타일

> `marker_style` | type : `str` | default : `'default'`
>
> 마커의 스타일
>
> | 입력값             | 형태                        |
> | ------------------ | --------------------------- |
> | `'default'`        | 기본 (픽셀)                 |
> | `'dot'`            | 점(크기조절 안되는 작은 원) |
> | `'pixel'`          | 픽셀                        |
> | `'circle'`         | 원 ○                        |
> | `'triangle_down'`  | 아래삼각형 ▽                |
> | `'triangle_up'`    | 위삼각형 △                  |
> | `'triangle_left'`  | 왼쪽삼각형 ◁                |
> | `'triangle_right'` | 오른쪽삼각형 ▷              |
> | `'tri_down'`       | 열린 아래 삼각형 ﹀         |
> | `'tri_up'`         | 열린 위쪽 삼각형 ︿         |
> | `'tri_left'`       | 열린 왼쪽 삼각형 <          |
> | `'tri_right'`      | 열린 오른쪽 삼각형 >        |
> | `'square'`         | 네모 □                      |
> | `'pentagon'`       | 오각형 ⬟                    |
> | `'star'`           | 별 ☆                        |
> | `'hexagon1'`       | 육각형(세로) ⬡              |
> | `'hexagon2'`       | 육각형(가로)                |
> | `'plus'`           | 더하기 기호 +               |
> | `'x'`              | 엑스 기호 X                 |
> | `'diamond'`        | 마름모 ◇                    |
> | `'thin_diamond'`   | 얇은 마름모 ◊               |

> `marker_size` | type : `int` | default : `'default'`
>
> 마커의 크기

> `marker_color` | type : `str` | default : `'default'`
>
> 마커의 색깔. 공통 색깔 변수 적용 가능

> `marker_border_size` | type : `int` | default : `'default'`
>
> 마커의 테두리 굵기

> `marker_border_color` | type : `str` | default : `'default'`
>
> 마커 테두리 색깔. 공통 색깔 변수 적용 가능

```python
plu.draw_plot(
    title='line', x=x, y=data, 
    marker_style='circle', 
    marker_size=10, 
    marker_color='white',
    marker_border_size=2, 
    marker_border_color='black'
)
```

![marker](plot_explain_images\marker.png)

데이터 추가

> `add_x_list` , `add_y_list`, `add_color_list` | type : `list` | default : `None`
>
> 이미지에 추가로 표시할 데이터. 기본 x, y, color 변수와 동일한 값을 `list` 로 감싸서 동일하게 입력.
>
> 순서에 맞춰서 적용됨

```python
plu.draw_plot(
    title='add', 
    x=x,
    y=data, 
  	line_color='red',
    add_x_list=[x, x],
    add_y_list=[data1, data2],
    add_color_list=['red', 'violet'],
)
```

![add](plot_explain_images\add.png)

구역 강조

> `focus_list` | type : `int list` | default : `None`
>
> 이미지에서 x 축을 기준으로 색을 칠해서 강조할 범위를 (시작, 끝) 의 형태로 넣은 `list` 값. 
>
> 한 list 에 복수의 구역을 `tuple` 형태로 입력 가능
>
> ```python
> focus_list=[(22, 27), (42, 53), (70, 76)]
> ```

> `focus_color_list` | type : `list` | default : `None`
>
> 각 강조 범위 구역에 대한 색. 공통 색 변수 지정 가능하며 `list` 에 입력한 순서를 따름.
>
> 값을 지정하지 않거나 default 로 해두면 색은 기본적으로 회색(gray) 로 지정됨.

> `alpha_list` | type : `float list` | default : `None`
>
> 각 강조 범위 구역의 투명도. 0~1 사이의 값을 지정하며 0에 가까울수록 투명해진다.
>
> 값을 지정하지 않거나 default 로 해두면 값은 기본적으로 0.2 로 지정됨

```python
plu.draw_plot(
    title='focus', x=x, y=data, 
    focus_list=[(22, 27), (42, 53), (70, 76)],
    focus_color_list=['blue', 'red', 'violet'],
    alpha_list=[0.5, 0.75, 1]
)
```

![focus](plot_explain_images\focus.png)

저장

> `save_path` | type : `str` | default : `None`
>
> 이미지를 저장할시 지정하는 경로값. 값을 지정하지 않거나 `None` 으로 입력하면 저장되지 않는다.
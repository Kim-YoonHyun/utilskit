# envs_setting

각종 random seed 값을 전부 고정하는 함수. 현재 numpy.random 과 random 2개 시드만 지정함

## parameters

| 입력변수 | type  | default |
| -------- | ----- | ------- |
| `seed`   | `int` | 42      |

## return

| 출력 type      | 설명 |
| -------------- | ---- |
| return 값 없음 | -    |

## 사용예시

```python
from utilskit import utils as u
u.envs_setting()
```

## parameters detail

> `seed`  | type : `int` | default : 42
>
> 각종 랜덤변수에 대한 시드값.

## 
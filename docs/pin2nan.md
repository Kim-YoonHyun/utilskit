## pin2nan(미완성)

이상치의 범위에는 속하지 않지만 데이터 흐름상 이상치로 볼 필요가 있는 국소 범위의 값을 결측치로 변경 후 앞뒤 채우기를 진행하는 함수

| 입력변수    | type               | default |
| ----------- | ------------------ | ------- |
| `dataframe` | `pandas dataframe` | -       |
| `column`    | `str`              | -       |
| `max_diff`  | `float`            | 0.1     |
| `repeat`    | `int`              | 3       |

| 출력 type          | 설명                                    |
| ------------------ | --------------------------------------- |
| `pandas dataframe` | 흐름상 이상치를 NaN 로 변경한 dataframe |

사용예시

```python

```

---

> `변수명`  | type : `a` | default : `a`
>
> 내용
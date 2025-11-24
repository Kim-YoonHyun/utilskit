# section_union

산출된 2개의 구간A 와 구간B 가 있을 때 그 두 구간 사이의 구간빼기, 구간합침, 구간부분집합을 계산하여 새로운 구산을 산출하는 함수

## parameters

| 입력변수       | type             | default |
| -------------- | ---------------- | ------- |
| `main_section` | `list` + `tuple` | -       |
| `sub_section`  | `list` + `tuple` | -       |
| `mode`         | `str`            | -       |

## return

| 출력 type        | 설명                                           |
| ---------------- | ---------------------------------------------- |
| `list` + `tuple` | 연산 결과 구간값을 담은 `tuple` 의 모음 `list` |

## 사용예시

```python
from utilskit import repeatutils as rpu
data_ary = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5]
_c_section1 = rpu.get_section(
    data=data_ary, 
    repeat=2,
    max_key=4, 
    min_key=2,
    between=True
)
c_section1 = _c_section1['2<=<=4']
_c_section2 = rpu.get_section(
    data=data_ary,
    repeat=2,
    max_key=5,
    min_key=3,
    between=True
)
c_section2 = _c_section2['3<=<=5']
print(f'main_section : {c_section1}')
print(f'sub_section : {c_section2}')
union_section = rpu.section_union(
    main_section=c_section1,
    sub_section=c_section2,
    mode='-'
)
print(f'union - : {union_section}')
union_section = rpu.section_union(
    main_section=c_section1,
    sub_section=c_section2,
    mode='+'
)
print(f'union + : {union_section}')
union_section = rpu.section_union(
    main_section=c_section1,
    sub_section=c_section2,
    mode='&'
)
print(f'union & : {union_section}')
'''
main_section : [(3, 23)]
sub_section : [(7, 12), (17, 27)]
union - : [(3, 6), (13, 16)]
union + : [(3, 27)]
union & : [(7, 12), (17, 23)]
'''
```

## parameters detail

> `main_section`  | type : `list` + `tuple`
>
> 구간과 구간 연산을 진행할시 그 중심이 되는 구간모음 리스트. `list` 내에 `tuple` 로 구성되어있는 형태를 입력해야한다.

> `sub_section`  | type : `list`  + `tuple`
>
> 구간과 구간 연산을 진행할 시 중심 구간에 대한 연산재료가 되는 구간모음 리스트. `list` 내에 `tuple` 로 구성되어있는 형태를 입력해야한다.

> `mode` | type : `str` | limit : `'-'`, `'+'`, `'&'`
>
> 입력한 중심, 서브 구간에 대해서 뺴기('`-`'), 더하기('`+`'), 부분집합('`&`') 방식 중 한 가지를 결정하는 변수
>
> `'-'`, `'+'`, `'&'` 3개의 값만 입력 가능하며 그 외의 값을 입력할 경우 에러 발생.
>
> 부분집합 연산의 경우 main 과 sub 를 구분하는 것의 의미가 없어짐

(사용예시 결과에 대한 시각화)

![union](repeat\union.png)


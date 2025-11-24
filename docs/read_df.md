# read_df

csv, CSV, xlsx, xls, txt 5개 확장자와 내부 데이터에 적절한 encoding 을 자동으로 설정하여 `pandas dataframe` 형태로 읽어오는 함수

## parameters

| 입력변수 | type  | default |
| -------- | ----- | ------- |
| `path`   | `str` | -       |

## return

| 출력 type          | 설명                                  |
| ------------------ | ------------------------------------- |
| `pandas dataframe` | 지정한 데이터를 지니고 있는 dataframe |

## 사용예시

```python
df = read_df('/home/path/data.csv')
df = read_df('./data.xlsx')
```

## parameters detail

> `path` | type : `str`
>
> 파일명을 포함한 상대경로 또는 절대경로를 입력한다.

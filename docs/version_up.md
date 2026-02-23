

# version_up

사용자 입력을 받아 semantic versioning 규칙에 따라 버전을 업데이트하는 함수.

대화형 인터페이스를 통해 버전 업데이트 유형을 선택하고,
선택에 따라 Major, Minor, Patch 또는 Identifier 를 변경한 새 버전과 태그를 반환한다.

## parameters

| 입력변수      | type  | default |
| ------------- | ----- | ------- |
| `name`        | `str` | -       |
| `pre_version` | `str` | -       |

## return

| 출력 type  | 설명                                            |
| ---------- | ----------------------------------------------- |
| `tuple`    | (new_version, tag_text) 형태의 튜플             |

## 사용예시

```python
from utilskit import versionutils as vu

# 현재 버전 1.1.12 에서 버전 업
new_version, tag = vu.version_up("MyProject", "1.1.12")
"""
------------------------------------------------------------
| 1 : Major-Release | Major      | 1.1.12 --> 2.0.0        |
| 2 : Feature       | Minor      | 1.1.12 --> 1.2.0        |
| 3 : Patch         | Patch      | 1.1.12 --> 1.1.13       |
| 4 : Refactoring   | Patch      | 1.1.12 --> 1.1.13       |
| 5 : Test          | Identifier | 1.1.12 --> 1.1.12+test1 |
| 6 : Post-release  | Identifier | 1.1.12 --> 1.1.12post1  |
| 0 : Ignore        | Ignore     | 1.1.12 --> 1.1.12       |
------------------------------------------------------------
MyProject(1.1.12) 버전 업 태그를 입력 :
"""
# 사용자가 3 입력시
# new_version = "1.1.13"
# tag = "Patch"

print(f"New version: {new_version}")  # "1.1.13"
print(f"Tag: {tag}")  # "Patch"

# 빈 버전에서 시작
new_version, tag = vu.version_up("NewProject", "")
# 내부적으로 "0.0.0" 으로 초기화되어 진행
```

## parameters detail

> `name`  | type : `str`
>
> 프로젝트 또는 패키지의 이름.
> 사용자 입력 프롬프트에 표시되어 어떤 프로젝트의 버전을 변경하는지 알려줌.

> `pre_version` | type: `str`
>
> 현재(이전) 버전 문자열.
> semantic versioning 형식을 따라야 함 (예: "1.2.3", "0.1.0").
> 빈 문자열("")이 입력되면 자동으로 "0.0.0" 으로 초기화됨.
>
> 사용자 입력에 따른 버전 변경 규칙:
> - 1 (Major-Release): Major 버전 증가, Minor/Patch 는 0으로 초기화
> - 2 (Feature): Minor 버전 증가, Patch 는 0으로 초기화
> - 3, 4 (Patch/Refactoring): Patch 버전 증가
> - 5, 6 (Test/Post-release): 사용자가 직접 버전 입력
> - 0 (Ignore): 버전 변경 없음
>
> ```python
> # 예시 1: Major 버전 업
> new_ver, tag = version_up("API", "1.5.3")
> # 사용자가 1 입력 -> new_ver = "2.0.0", tag = "Major-Release"
>
> # 예시 2: 테스트 버전 생성
> new_ver, tag = version_up("Library", "0.2.1")
> # 사용자가 5 입력 후 "0.2.1+test1" 입력 -> new_ver = "0.2.1+test1", tag = "Test"
>
> # 예시 3: 변경 없음
> new_ver, tag = version_up("Tool", "3.1.4")
> # 사용자가 0 입력 -> new_ver = "3.1.4", tag = "Ignore"
> ```

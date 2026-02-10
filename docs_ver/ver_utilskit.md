# Release
## 2025-11-24 ver 0.2.18

에러수정

- repeatutils 의 section_union 함수에서 mode 에 -, +, & 외의 값 입력시 에러 도출하는 유효성 검증 부분 추가

최적화

- README, docs 구조 변경

### 0.2.18.1

- README 의 하이퍼링크를 github 절대경로로 변경

### 0.2.18.2

- README 의 하이퍼링크를 github 절대경로로 변경(경로 수정)

## 0.2.17

- logutils 기능 완전 삭제 > logie 패키지로 분리
## 0.2.16
- repeatutils 의 section_union 에서 mode 를 & 으로 하고 sub 또는 main section 이 빈 리스트인 경우 빈리스트 [] 를 리턴 하도록 수정
### 0.2.16.1
- 조건문에서 & 앞에 띄어쓰기가 하나 포함되어있어 정상적 연산이 되지 않는 부분 수정
## 0.2.15
- repeatutils 의 section_union 에서 결과가 빈값일때 에러가 나는 현상 수정
## 0.2.14
- repeatutils 의 min_key 를 설정했을 때 min_equal=False 로 두는 경우 정상적인 구간 탐색을 못하는 현상 수정
## 0.2.13
- repeatutils 에 section_union 함수 추가
### 0.2.13.1
- rpu.get_section 을 써서 에러가 난 부분 수정
## 0.2.12
- dataframeutils 의 fill_repeat_nan 함수가 NaN 이 딱 하나만 있는 경우 보정하지 못하는 현상 수정
## 0.2.11
- dataframeutils 의 fill_repeat_nan 함수가 3 이하 반복되는 NaN 이 아닌 3 이상 반복되는 NaN 구간에 대해 보정하는 현상 수정
## 0.2.10
- repeatutils 에서 between 이 정상작동하지 않는 현상 수정
### 0.2.10.1
- 버전 업로드 에러 수정
### 0.2.10.2
- 함수 내부 print 제거
## 0.2.9
- repeatuils 에서 정수형 list 를 넣었을때 float 으로 변경되도록 수정
## 0.2.8
- dbutils 에서 db 의 컬럼명을 리스트로 추출하는 get_db_name 함수 추가
### 0.2.8.1
- __all__ 에 get_db_name 추가해서 사용가능하도록 설정
## 0.2.7
- repeatutils 에서 정수형 list 를 넣었을때 key 를 통한 구간 파악이 되지 않는 현상 수정
## 0.2.6
- dataframeutils 의 fill_repeat_nan 의 에러 수정
## 0.2.5
- xlsx 읽는 패키지 install 추가
## 0.2.4
- repeatutils 의 에러 제거
## 0.2.3
- dbutils 에 대한 업데이트 진행
## 0.2.2
- build 방식 변경
## 0.2.1
- repeatutila 에 get_section 함수 추가
## 0.2.0 
- 정식 최초 배포버전
- 각 함수의 사용성 강화 및 비활성 함수 지정
## 0.1.2
- repeatutils 의 get_repeat_section 에서 하나의 값이 여러 구간에서 반복될때 마지막 구간만 나오는 부분 수정
- repeatutils 의 get_repeat_section 및 get_stan_repeat_section 에서 추출되는 구간의 마지막 값이 +1 이 되는 부분 수정
## 0.1.1
- repeatutils.py 추가
- utils.py 에서 repeat 관련 함수 제거


## 2026-01-28 Version 1.0.0
**tag:** @Major-Release
**Summary:** baseline link / git + hash 기반 검증 구조 최초 적용
**Detail:**
Modified: .gitignore

Modified: README.md

Deleted: git_test.py

Modified: pyproject.toml

Modified: scripts/upload.py

Modified: utilskit/hashutils/hashutils.py
 - 해시 함수 전부 모음
 - 함수 `reset_values` 삭제
 - 함수 `combined2hash` 에서 파일 이름이 manifest.json 인 경우의 논리 제거

Modified: utilskit/utils/utils.py
 - 기존의 사용성 없는 정크 함수 전부 삭제
 - 함수 `SmartOutput` 추가
 - `get_error_info` 함수에 openai API 기반 AI에러 분석 기능 추가
 - `get_error_info` 함수에서 AI 에러 분석 기능 사용시 openai install 여부 확인
 - 신규 함수 `path_change` 를 추가

Modified: utilskit/versionutils/versionutils.py
 - `version_up` 함수 추가
 - git status 정보를 추출하는 `get_git_status` 함수 추가
 - 함수 `git_addcommit` 추가

New: .cruft.json

New: scripts/versioning.py
 - 버전업을 통해 pyproject.toml 의 버전 값을 바꾸는 기능 추가
 - git 을 통해 변경이력을 확인 (status) 하고 해시검증을 통한 대상선정, 버전업, git add&commit 까지 진행하는 기능


## 2026-01-28 Version 1.0.1
**tag:** @Patch
**Summary:** commit 안되는 현상 수정
**Detail:**
Modified: scripts/versioning.py


## 2026-01-28 Version 1.0.2
**tag:** @Patch
**Summary:** 검증 무한 루프 수정
**Detail:**
Modified: .gitignore

Modified: README.md

Modified: pyproject.toml

Modified: scripts/versioning.py
 - pyproject.toml 에 한해서는 version 이라는 라인은 해시 계산에서 제거
 - 원본대체, git add commit 순서를 변경

Modified: utilskit/hashutils/hashutils.py
 - 키워드기반으로 특정 라인을 해시 계산에서 제외하는 ignore_words 인자 추가


## 2026-01-28 Version 1.0.3
**tag:** @Patch<br>
**Summary:** README.md 수정<br>
**Detail:**
Modified: README.md


## 2026-01-29 Version 1.0.4
**Tag:** @Patch<br>
**Summary:** install 시의 option 설정<br>
**Detail:**<br>
Modified: pyproject.toml

Modified: requirements.txt

New: scripts/sync_dependencies.py

New: scripts/sync_dependencies.sh


## 2026-02-02 Version 1.0.1
**Tag:** @Refactoring<br>
**Summary:** 최적화<br>
**Detail:**<br>
- Modified: /home/kimyh/library/utilskit/src/utilskit/hashutils/hashutils.py
 - `content2bashobj` 를 __all__ 에서 제거



## 2026-02-02 Version 1.0.2
**Tag:** @Patch<br>
**Summary:** import 에러 수정<br>
**Detail:**<br>
- Modified: /home/kimyh/library/utilskit/src/utilskit/versionutils/versionutils.py
 - __all__ 추가



## 2026-02-10 Version 1.0.3
**Tag:** @Patch<br>
**Summary:** 계산 알고리즘 수정<br>
**Detail:**<br>
- Modified: /home/kimyh/library/utilskit/src/utilskit/hashutils/hashutils.py
 - `file2hash` 함수에서 경로를 해시 계산에 넣는 부분을 제거

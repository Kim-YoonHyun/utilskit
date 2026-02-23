


## 2026-02-02 Version 1.0.0
**Tag:** @Major-Release<br>
**Summary:** versioning 신규생성 및 테스트<br>
**Detail:**<br>
- Deleted: /home/kimyh/library/utilskit/scripts/sync_dependencies.sh
- Modified: /home/kimyh/library/utilskit/scripts/upload.py
 - 필요한 함수 자체를 강제 주입
 - build 하는 부분 추가함
- Deleted: /home/kimyh/library/utilskit/scripts/versioning.py
- New: /home/kimyh/library/utilskit/scripts/build.py
 - 필요한 함수 자체를 강제 주입



## 2026-02-02 Version 1.1.0
**Tag:** @Feature<br>
**Summary:** build 기능 개선<br>
**Detail:**<br>
- Modified: /home/kimyh/library/utilskit/scripts/build.py
 - lock 파일을 활용한 시스템 build 진행



## 2026-02-02 Version 1.1.1
**Tag:** @Refactoring<br>
**Summary:** 업로방식 자동화<br>
**Detail:**<br>
- Deleted: /home/kimyh/library/utilskit/scripts/build.py
- Modified: /home/kimyh/library/utilskit/scripts/upload.py
 - 파일 검증 후 버전을 수정하고 업로드까지의 내용을 전부 진행
 - 작업 디렉토리를 pack_path 에서 dist_path 로 변경



## 2026-02-02 Version 1.1.2
**Tag:** @Patch<br>
**Summary:** 설정 오류 수정<br>
**Detail:**<br>
- Modified: /home/kimyh/library/utilskit/scripts/upload.py



## 2026-02-02 Version 1.1.3
**Tag:** @Patch<br>
**Summary:** 설정 오류 수정<br>
**Detail:**<br>
- Modified: /home/kimyh/library/utilskit/scripts/upload.py
 - toml encoding 을 utf-8-sig 에서 utf-8 로 변경



## 2026-02-23 Version 1.1.4
**Tag:** @Patch<br>
**Summary:** new file<br>
**Detail:**<br>
- New: /home/kimyh/library/utilskit/scripts/get_hash_cache.py



## 2026-02-23 Version 1.1.5
**Tag:** @Refactoring<br>
**Summary:** 정합성 업데이트<br>
**Detail:**<br>
- Modified: /home/kimyh/library/utilskit/scripts/upload.py
 - 새로운 baseline 에 맞춰 exitcode 를 확인하는 방식으로 변경



## 2026-02-23 Version 1.1.6
**Tag:** @Patch<br>
**Summary:** git commit 누락 추가<br>
**Detail:**<br>
- Modified: /home/kimyh/library/utilskit/scripts/upload.py
 - 끝나고 전체 git commit 부분 추가

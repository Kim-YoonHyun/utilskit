import semver
import textwrap

def version_up(name, pre_version):
    tag_dict = {
        1:"Major-Release",
        2:"Feature",
        3:"Patch",
        4:"Refactoring",
        5:"Test",
        6:"Post-release",
        0:"Ignore"
    }
    tag_key_list = list(tag_dict.keys())
    min_tag = min(tag_key_list)
    max_tag = max(tag_key_list)

    # 버전 문자열 연산화
    if pre_version == "":
        pre_version = "0.0.0"
    v = semver.Version.parse(pre_version)

    # 버전 변경 입력값 받기
    string = textwrap.dedent(
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
        """
    )
    print(string)
    while True:
        try:
            tag = int(input(f"{name}({pre_version}) 버전 업 태그를 입력 :"))
            if tag not in tag_key_list:
                print(f'잘못된 입력값입니다. {min_tag} ~ {max_tag} 사이의 값을 입력해주세요')
            else:
                break
        except Exception:
            print(f'잘못된 입력값입니다. {min_tag} ~ {max_tag} 사이의 값을 입력해주세요')

    # ==============================================================
    # 새 버전 변경 적용
    if tag == 1:
        new_version = str(v.bump_major())
    elif tag == 2:
        new_version = str(v.bump_minor())
    elif tag in [3, 4]:
        new_version = str(v.bump_patch())
    elif tag in [5, 6]:
        new_version = input(f"변경 버전 직접 입력 --> ")
    elif tag == 0:
        new_version = pre_version
    tag_text = tag_dict[tag]

    return new_version, tag_text
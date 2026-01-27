import sys
import os
import re
import subprocess



def get_git_hash(file_path):
    """
    Git의 'hash-object' 명령을 사용하여 파일의 Blob ID(해시)를 가져옵니다.
    이 방식은 파일을 실제로 커밋하지 않고도 Git 방식의 해시를 계산합니다.
    """
    try:
        filtered_content = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if "# @log:" not in line:
                    filtered_content.append(line)
        
        # 리스트를 하나의 문자열로 합치고 바이트로 변환
        processed_data = "".join(filtered_content).encode('utf-8')

        # 명령어
        cmd = ['git', 'hash-object', '--stdin', '--path', file_path]

        # git hash-object <file_path> 명령 실행
        result = subprocess.run(
            cmd,
            input=processed_data,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            # text=True, 
            check=True
        )
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
    

def get_file_status(file_path):
    """
    파일이 현재 수정되었는지(Modified) 확인합니다.
    """
    result = subprocess.run(
        ['git', 'status', '--porcelain', file_path], 
        stdout=subprocess.PIPE, 
        text=True
    )
    status = result.stdout.strip()
    return "Changed" if status else "Unchanged"


def main():
    # 실행 예시
    target_file = '/home/kimyh/library/utilskit/utilskit/utils/utils.py'

    log_list = extract_logs_from_file(target_file)
    print(log_list)
    sys.exit()
    if os.path.exists(target_file):
        current_hash = get_git_hash(target_file)
        status = get_file_status(target_file)
        
        print(f"File: {target_file}")
        print(f"Git Blob Hash: {current_hash}")
        print(f"Status: {status}")
    else:
        print(f"{target_file} 파일이 존재하지 않습니다.")


if __name__ == "__main__":
    main()
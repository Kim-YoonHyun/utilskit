import numpy as np
import pandas as pd
import shutil
import textwrap
import os
import sys
import json
import time
import csv
from datetime import date, datetime, timedelta
import subprocess
import shlex


__all__ = ['envs_setting', 'get_error_info', "path_change"]

# @log: 기존의 사용성 없는 정크 함수 전부 삭제
def envs_setting(seed=42):
    '''
    난수지정 등의 환경설정

    parameters
    ----------
    random_seed: int
        설정할 random seed

    returns
    -------
    torch, numpy, random 등에 대한 랜덤 시드 고정    
    '''
    import random
    import numpy as np

    # seed
    np.random.seed(seed)
    random.seed(seed)


# @log: 함수 `SmartOutput` 추가
class SmartOutput:
    """
    함수 get_error_info 의 출력에 print() 를 했을 때 stream 을 하기 위한
    결과 변형용 클래스
    """
    def __init__(self, data, is_stream=False):
        self.data = data
        self.is_stream = is_stream
        self.full_text = ""

    # print()가 호출될 때 실행되는 매직 메서드
    def __repr__(self):
        if self.is_stream:
            # 스트림인 경우 루프를 돌며 실시간 출력
            for event in self.data:
                if event.type == "response.output_text.delta":
                    # event 객체 구조에 따라 event.delta 또는 event.text 등을 확인
                    if hasattr(event, 'delta') and event.delta:
                        chunk_text = event.delta
                        print(chunk_text, end="", flush=True)
                        time.sleep(0.05)
                        
                # 2. 모델의 생각이 끝났을 때 알림
                elif event.type == "response.output_item.added":
                    pass

            return "" # print의 마지막 줄바꿈을 위해 빈 값 리턴
        else:
            # 에러 메시지나 일반 문자열인 경우 바로 리턴
            return str(self.data)
        

# @log: `get_error_info` 함수에 openai API 기반 AI에러 분석 기능 추가
# @log: `get_error_info` 함수에서 AI 에러 분석 기능 사용시 openai install 여부 확인
def get_error_info(summary=False, api_key=None):
    import traceback
    
    # 요약 시
    if summary:
        # 현재 발생한 예외 정보
        etype, value, tb = sys.exc_info()
        # 전체 스택 프레임을 가져옴
        frame_list = traceback.extract_tb(tb)
        # 패키지 로직 문구 제거
        new_frame_list = []
        for frame in frame_list:
            if "site-packages" not in frame.filename:
                new_frame_list.append(frame)
        # 합치기
        stack_str = "".join(traceback.format_list(new_frame_list))
        traceback_string = f"{stack_str} {etype.__name__} : {value}"
    # 미요약 시
    else:
        traceback_string = traceback.format_exc()
    
    # AI 를 활용하여 에러 분석 진행
    if api_key is not None:
        # openai 패키지가 없을 시 설치
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError(
            "\n"
            "Optional dependency 'openai' is not installed.\n"
            "To use this LLM feature, please install it by running:\n"
            "pip install \"utilskit[llm]\""
        ) from None
        
        # api key 설정
        os.environ["OPENAI_API_KEY"] = api_key

        # AI 입력
        print("발생 에러에 대한 AI 추론 진행 중 ...")
        client = OpenAI()
        stream_response = client.responses.create(
            model="gpt-5-nano",
            input=textwrap.dedent(
                f"""
                에러 문구는 아래와 같다.
                {traceback_string}
                위의 에러 문구를 통해 
                1. 에러의 발생 위치
                2. 에러가 발생한 코드와 에러에 대한 설명
                3. 에러의 발생 원인에 대한 설명
                4. 고친 예시 코드를 출력(Markdown 형식 없이 코드 문자만)
                의 4개 결과를 간략하게 대답하시오.
                """
            ),
            stream=True
        )
        return SmartOutput(stream_response, is_stream=True)
    
    return SmartOutput(traceback_string, is_stream=False)


# @log: 신규 함수 `path_change` 를 추가
def path_change(text, **kwargs):
    """
    template: "{data2}/module" 같은 문자열
    **kwargs: 가변적인 키워드 인자 (data1=..., value1=... 등)
    """
    try:
        # format_map은 딕셔너리 형태의 데이터를 받아 문자열을 치환합니다.
        return text.format_map(kwargs)
    except KeyError as e:
        return f"Error: 문자열에 필요한 {e} 값이 인자로 전달되지 않았습니다."
    
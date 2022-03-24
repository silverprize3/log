# 모듈
import logging
import logging.handlers
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder('./logs')

# 파일 크기
LOG_MAX_SIZE = 1024 *1024 * 10
# 파일 개수 
LOG_FILE_CNT = 10


# logging 객체 생성
logger = logging.getLogger("log_youtube")

# 레벨 설정
logger.setLevel(logging.INFO) # 레벨 설정

# handler 객체 추가
# logger(logging의 객체)가 찾은 오류를 어떻게 사용자에게 보여줄지 결정
# fileHandeler = logging.FileHandler(filename="./logs/log_youtube_crawl.log", maxBytes=LOG_MAX_SIZE, backupCount=LOG_FILE_CNT) # 파일 형태
# streamHandler = logging.StreamHandler() # 콘솔 형태 
fileHandeler = logging.handlers.RotatingFileHandler( "./logs/log_youtube_crawl.log", maxBytes=LOG_MAX_SIZE, backupCount=LOG_FILE_CNT )

# handler 레벨 설정 - handler 마다 레벨설정 필요
fileHandeler.setLevel(logging.INFO) 
# streamHandler.setLevel(logging.DEBUG)

# 포매팅 생성 및 설정
# 날짜시간 - 로거이름 - 로깅레벨 - 메세지 - 로깅 호출 소스행번호 - 파일이름 
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d - %(filename)s") 
fileHandeler.setFormatter(formatter) 
# streamHandler.setFormatter(formatter)

#logger에 handler 추가
logger.addHandler(fileHandeler)
# logger.addHandler(streamHandler)

num = 2 
try:
    print(num/0)
except Exception as e:
    logger.warning("Couldn't divi : %s", num)
    logger.error( "Reason-- : %s", e )
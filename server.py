import zmq
import logging
from config import PULL_ADDRESS, PUB_ADDRESS

context=zmq.Context()

pull_socket=context.socket(zmq.PULL)
pull_socket.bind(PULL_ADDRESS)

pub_socket=context.socket(zmq.PUB)
pub_socket.bind(PUB_ADDRESS)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    filename="server.log", # 로그를 파일에 저장
    filemode="a", # 'a'는 append(이어쓰기), 'w'는 덮어쓰기
)

logging.info("서버 실행 중.. 클라이언트의 메시지를 기다리는 중입니다.")
while True:
    try:
        message=pull_socket.recv_string()
        logging.info(f"수신 받은 메시지 : {message}")

        pub_socket.send_string(message)
        logging.info("브로드캐스트 완료")
    except KeyboardInterrupt:
        logging.warning("서버 종료!")
        break
        
    
import zmq
import threading
import logging
from config import SERVER_PULL_CONNECT,SERVER_PUB_CONNECT

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
context=zmq.Context()

nickname="USER2"

#1. 서버로부터 메시지를 받는 PUSH 소켓
push_socket=context.socket(zmq.PUSH)
push_socket.connect(SERVER_PULL_CONNECT)

#2. 서버로부터 메시지를 받는 SUB 소켓
sub_socket=context.socket(zmq.SUB)
sub_socket.connect(SERVER_PUB_CONNECT)
sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")

def receive_messages():
    while True:
        try:
            message=sub_socket.recv_string()
            if message.startswith(nickname):
                continue
            logging.info(f"[받음] {message}")
        except Exception as e:
            logging.error(f"수신 에러: {e}")
            break

thread=threading.Thread(target=receive_messages,daemon=True)
thread.start()


logging.info("User1의 채팅 시작! 메시지를 입력하세요. (종료: exit)")
while True:
    msg=input()
    if msg.lower()=="exit":
        logging.infor("채팅 종료")
        break
    
    push_socket.send_string("["+nickname+"]   "+msg)
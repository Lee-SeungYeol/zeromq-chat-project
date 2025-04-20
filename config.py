#서버가 수신(PULL)할 주소
PULL_ADDRESS="tcp://*:5555"

# 서버가 전송(PUB)할 주소
PUB_ADDRESS='tcp://*:5556'

#클라이언트가 서버로 PUSH 연결할 주소
SERVER_PULL_CONNECT="tcp://localhost:5555"

#클라이언트가 서버로부터 SUB 연결할 주소
SERVER_PUB_CONNECT="tcp://localhost:5556"


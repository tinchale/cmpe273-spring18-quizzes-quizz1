
import grpc
import ping_pb2_grpc
from ping_pb2 import Request,Response

class pingClient():
    def _init_(self, host='0.0.0.0', port=3000):
        self.channel = grpc.insecure_channel('%s:%d' % (host,port))
        self.stub = ping_pb2_grpc.PingPongStub(self.channel)

    def ping(self, data):
        req = Request(data=str(data))
        return self.stub.ping(req)

def test():
        client = pingClient()
        resp = client.ping("ping")
        print("Response={}".format(resp.data))

if __name__ == '_main_':
        test()     
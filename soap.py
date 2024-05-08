#server.py

from spyne import *
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class CalculatorService(ServiceBase):
    @rpc(Integer , Integer , _returns=Iterable(Integer))
    def add(ctx , a,b):
        yield a+b

application = Application([CalculatorService] ,
                          tns='spyne.example.calculator',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())
wsgi = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('127.0.0.1' , 8000 , wsgi)
    print("SOAp is running ")
    server.serve_forever()

#client.py
from zeep import Client

c = Client('http://127.0.0.1:8000/?wsdl')

result = c.service.add(10,20)
print("result is " , result)
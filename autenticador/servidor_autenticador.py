from concurrent import futures
import grpc
import autenticador_pb2
import autenticador_pb2_grpc

class Autenticador (autenticador_pb2_grpc.AutenticadorServicer):

    def autenticar(self, request, context):
        if request.contrasena == "123": 
            return autenticador_pb2.AuthenticationReply(message="%s autenticado 1 en %s" % (request.nombre, request.lugar_nacimiento), status=True)
        else:
            return autenticador_pb2.AuthenticationReply(message="%s autenticado 1 en %s" % (request.nombre, request.lugar_nacimiento), status=False) 


def ofrece_servicios():
    puerto = "50051"
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    autenticador_pb2_grpc.add_AutenticadorServicer_to_server(Autenticador(), servidor)
    servidor.add_insecure_port("[::]:" + puerto)
    servidor.start()
    servidor.wait_for_termination()

if __name__ == "__main__":
    print("Ofreciendo servicios de autenticación")
    ofrece_servicios()
    
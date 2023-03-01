import grpc
import autenticador_pb2
import autenticador_pb2_grpc

def run():
    print("Intentando autenticador")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = autenticador_pb2_grpc.AutenticadorStub(channel)
        respuesta = stub.autenticar(autenticador_pb2.AuthenticationRequest(nombre = "Juan", 
                                                                         lugar_nacimiento = "Jalisco",
                                                                         anno_nacimiento = 2000,
                                                                         contrasena = "123"))
        
    print("El cliente recibió respuesta de autenticacion 1  ", respuesta.message, respuesta.status)

if __name__ == "__main__":
    run()
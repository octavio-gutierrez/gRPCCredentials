from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticationReply(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: bool
    def __init__(self, message: _Optional[str] = ..., status: bool = ...) -> None: ...

class AuthenticationRequest(_message.Message):
    __slots__ = ["anno_nacimiento", "contrasena", "lugar_nacimiento", "nombre"]
    ANNO_NACIMIENTO_FIELD_NUMBER: _ClassVar[int]
    CONTRASENA_FIELD_NUMBER: _ClassVar[int]
    LUGAR_NACIMIENTO_FIELD_NUMBER: _ClassVar[int]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    anno_nacimiento: int
    contrasena: str
    lugar_nacimiento: str
    nombre: str
    def __init__(self, nombre: _Optional[str] = ..., lugar_nacimiento: _Optional[str] = ..., anno_nacimiento: _Optional[int] = ..., contrasena: _Optional[str] = ...) -> None: ...

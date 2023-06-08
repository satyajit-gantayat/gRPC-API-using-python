from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Billionaire(_message.Message):
    __slots__ = ["age", "country", "name", "organization"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    age: int
    country: str
    name: str
    organization: str
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ..., country: _Optional[str] = ..., organization: _Optional[str] = ...) -> None: ...

class GetBillionaireBioByNameRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetBillionaireBioByNameResponse(_message.Message):
    __slots__ = ["billionaire"]
    BILLIONAIRE_FIELD_NUMBER: _ClassVar[int]
    billionaire: _containers.RepeatedCompositeFieldContainer[Billionaire]
    def __init__(self, billionaire: _Optional[_Iterable[_Union[Billionaire, _Mapping]]] = ...) -> None: ...

class GetBillionairesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetBillionairesResponse(_message.Message):
    __slots__ = ["billionaires"]
    BILLIONAIRES_FIELD_NUMBER: _ClassVar[int]
    billionaires: _containers.RepeatedCompositeFieldContainer[Billionaire]
    def __init__(self, billionaires: _Optional[_Iterable[_Union[Billionaire, _Mapping]]] = ...) -> None: ...

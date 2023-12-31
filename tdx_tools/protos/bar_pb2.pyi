"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Bar(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MARKET_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    CLOSE_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    VOL_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    ADJUST_FIELD_NUMBER: builtins.int
    market: typing.Text
    code: typing.Text
    open: builtins.float
    close: builtins.float
    high: builtins.float
    low: builtins.float
    vol: builtins.float
    amount: builtins.float
    timestamp: builtins.float
    adjust: typing.Text
    def __init__(self,
        *,
        market: typing.Text = ...,
        code: typing.Text = ...,
        open: builtins.float = ...,
        close: builtins.float = ...,
        high: builtins.float = ...,
        low: builtins.float = ...,
        vol: builtins.float = ...,
        amount: builtins.float = ...,
        timestamp: builtins.float = ...,
        adjust: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["adjust",b"adjust","amount",b"amount","close",b"close","code",b"code","high",b"high","low",b"low","market",b"market","open",b"open","timestamp",b"timestamp","vol",b"vol"]) -> None: ...
global___Bar = Bar

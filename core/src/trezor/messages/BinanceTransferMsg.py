# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .BinanceInputOutput import BinanceInputOutput

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class BinanceTransferMsg(p.MessageType):
    MESSAGE_WIRE_TYPE = 706

    def __init__(
        self,
        inputs: List[BinanceInputOutput] = None,
        outputs: List[BinanceInputOutput] = None,
    ) -> None:
        self.inputs = inputs if inputs is not None else []
        self.outputs = outputs if outputs is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('inputs', BinanceInputOutput, p.FLAG_REPEATED),
            2: ('outputs', BinanceInputOutput, p.FLAG_REPEATED),
        }

from typing import List, Optional, Tuple

class Spend:
    coin_id: bytes
    puzzle_hash: bytes
    height_relative: Optional[int]
    seconds_relative: int
    create_coin: List[Tuple[bytes, int, Optional[bytes]]]
    agg_sig_me: List[Tuple[bytes, bytes]]
    def __init__(
        self,
        coin_id: bytes,
        puzzle_hash: bytes,
        height_relative: Optional[int],
        seconds_relative: int,
        create_coin: List[Tuple[bytes, int, Optional[bytes]]],
        agg_sig_me: List[Tuple[bytes, bytes]],
    ) -> None: ...

class SpendBundleConditions:
    spends: List[Spend]
    reserve_fee: int
    height_absolute: int
    seconds_absolute: int
    agg_sig_unsafe: List[Tuple[bytes, bytes]]
    cost: int
    def __init__(
        self,
        spends: List[Spend],
        reserve_fee: int,
        height_absolute: int,
        seconds_absolute: int,
        agg_sig_unsafe: List[Tuple[bytes, bytes]],
        cost: int,
    ) -> None: ...

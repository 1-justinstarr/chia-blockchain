from typing import Dict, Any

from chia.rpc.rpc_client import RpcClient
from chia.types.blockchain_format.sized_bytes import bytes32


class DataLayerRpcClient(RpcClient):
    async def start_data_layer(self) -> Dict[str, Any]:
        response: Dict[str, Any] = await self.fetch("start_data_layer", {})
        return response

    async def create_kv_store(self) -> Dict[str, Any]:
        response: Dict[str, Any] = await self.fetch("create_kv_store", {})
        return response

    async def get_value(self, tree_id: bytes32, key: bytes) -> Dict[str, Any]:
        response: Dict[str, Any] = await self.fetch("get_value", {"tree_id": tree_id.hex(), "key": key.hex()})
        return response

    async def update_kv_store(self, tree_id: bytes32, changelist: Dict[str, str]) -> Dict[str, Any]:
        response: Dict[str, Any] = await self.fetch("update_kv_store", {"tree_id": tree_id, "changelist": changelist})
        return response

    async def get_tree_state(self, tree_id: bytes32) -> bytes32:
        pass

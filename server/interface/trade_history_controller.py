from typing import List

from fastapi import APIRouter

from server.domain.service.trade_data_service import TradeDataService
from server.infrastructure.connector.h5_file_reader import H5FileReader
from server.interface.dto.trade_data import TradeData

trade_history_router = APIRouter()

trade_data_service: TradeDataService = H5FileReader()


@trade_history_router.get(
    "/xrp-usdt",
    summary="Get trade log of XRP to USDT by timestamp",
    response_model=List[TradeData]
)
def get_xrp_to_usd_tether_price(start_time: int = 1582509911141, end_time: int = 1582519911141):
    return trade_data_service.get_xrp_to_usdt(start_time, end_time).to_dict("r")

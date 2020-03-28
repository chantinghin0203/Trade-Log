from pydantic import BaseModel


class TradeData(BaseModel):
    timestamp: int
    price: float
    quantity: float
    side: int

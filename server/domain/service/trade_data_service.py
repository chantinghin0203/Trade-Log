from abc import ABC, abstractmethod

import pandas as pd


class TradeDataService(ABC):
    @abstractmethod
    def get_xrp_to_usdt(self, start_time: int, end_time: int) -> pd.DataFrame:
        ...

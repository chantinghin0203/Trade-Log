from datetime import datetime
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd

from server.domain.service.trade_data_service import TradeDataService
from server.resource.configuration import Configuration


class H5FileReader(TradeDataService):
    def __init__(self) -> None:
        with h5py.File(Configuration.XRP_USDT_H5_FILE_PATH, "r") as f:
            self.df_xrp_to_usdt = pd.DataFrame(np.array(f['trade']))

    @lru_cache()
    def get_xrp_to_usdt(self, start_time: datetime, end_time: datetime) -> pd.DataFrame:
        return self.df_xrp_to_usdt[self.df_xrp_to_usdt['timestamp'].between(start_time, end_time)]

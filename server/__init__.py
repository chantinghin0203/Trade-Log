from fastapi import FastAPI

from .interface.trade_history_controller import trade_history_router

app = FastAPI(title="Trade Log API", description="API to retrieve trade data", docs_url="/")

app.include_router(router=trade_history_router, prefix="/api/v1", tags=["Historical Trade Data"])

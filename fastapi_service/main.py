# -*- coding:utf-8 -*-

"""
@date: 2025/4/5 下午4:43
@summary:
"""
import uvicorn
from fastapi import FastAPI
from fastapi_service.api.users import user_router

app = FastAPI()

@app.get("/test")
def test():
    return {"Hello": "World"}

app.include_router(user_router)

if __name__ == '__main__':
    """"""
    uvicorn.run(app, host="0.0.0.0", port=8000)
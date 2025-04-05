# -*- coding:utf-8 -*-

"""
@date: 2025/4/5 下午5:16
@summary:
"""
from fastapi import APIRouter, status
# from fastapi.responses import JSONResponse
from fastapi_service.core.responses import JSONResponse

user_router = APIRouter(prefix="/users", tags=["用户管理"])

@user_router.get("/", summary="获取所有用户")
async def get_users():
    return JSONResponse(content={"id": 1, "name": "Alice"})


@user_router.post("/create", summary="创建新用户")
async def create_user(user: dict):
    return JSONResponse(content={"message": "用户已创建"})
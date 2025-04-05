# -*- coding:utf-8 -*-

"""
@date: 2025/4/5 下午7:24
@summary: 自定义返回结果
"""
import json
import typing
from fastapi.responses import Response
from starlette.background import BackgroundTask

class JSONResponse(Response):
    media_type = "application/json"
    def __init__(
        self,
        content: typing.Any,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None
    ) -> None:
        super().__init__(content, status_code, headers, media_type, background)

    def render(self, content: typing.Any):
        return json.dumps(
            {
                "code": self.status_code,
                "message": "success" if 200 <= self.status_code < 400 else "error",
                "data": content
            },
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")
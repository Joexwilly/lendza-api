from fastapi import APIRouter

from apis.v1 import route_user,  route_login, route_loan


api_router = APIRouter()
api_router.include_router(route_user.router,prefix="",tags=["users"])
api_router.include_router(route_loan.router,prefix="",tags=["loan"])
api_router.include_router(route_login.router,prefix="/login",tags=["login"])
from fastapi import APIRouter
from . import orders,health,admin

router=APIRouter()
router.include_router(orders.router, prefix="/orders",tags=["orders"])
router.include_router(health.router, prefix="/health",tags=["health"])
router.include_router(admin.router, prefix="/admin",tags=["admin"])
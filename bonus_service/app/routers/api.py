from fastapi import APIRouter

from routers import privilege, privilege_history


router = APIRouter()
router.include_router(privilege.router)
router.include_router(privilege_history.router)

from fastapi import APIRouter

from routers import ticket


router = APIRouter()
router.include_router(ticket.router)

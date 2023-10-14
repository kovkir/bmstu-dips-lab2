from fastapi import APIRouter

from routers import flight, airport


router = APIRouter()
router.include_router(flight.router)
router.include_router(airport.router)

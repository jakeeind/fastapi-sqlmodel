from fastapi import APIRouter

router = APIRouter(prefix="/v1")


@router.get("/")
def healthy():
    return {"status": "healthy"}

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.visits.routes import router as visit_router


app = FastAPI(
    title="Afterhours Backend",
    description="Web-first backend for Afterhours",
    version="0.1.0"
)

app.include_router(visit_router)

@app.get("/")
def root():
    return JSONResponse(
        content={
            "status": "alive",
            "message": "Afterhours backend is running 🚀"
        },
        media_type="application/json; charset=utf-8"
    )


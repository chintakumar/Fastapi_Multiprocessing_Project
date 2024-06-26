from fastapi import FastAPI
from app.controllers.add_controller import router
from logging_config import configure_logging

configure_logging()
app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from restapi import user

# Initialize application
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add in routers
app.include_router(user.router)

# Run app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

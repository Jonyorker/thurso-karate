import uvicorn
from fastapi import FastAPI

from restapi import user

# Initialize application
app = FastAPI()

# Add in routers
app.include_router(user.router)

# Run app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

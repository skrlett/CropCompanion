from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth_routes, llm_routes, user_routes

app = FastAPI()

# Add CORS middleware
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

# Include routes
app.include_router(auth_routes.router)
app.include_router(llm_routes.router)
app.include_router(user_routes.router)

#client = MongoClient(MONGO_URI)
#db = client[DATABASE]
# app.include_router(db_routes.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
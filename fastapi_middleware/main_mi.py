from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Middleware for logging requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # before processing the request
    print(f"[BEFORE REQUEST] Method: {request.method}, Path: {request.url.path}")
    
    # Process the request
    response = await call_next(request)
    
       # after processing the request
    print(f"[AFTER REQUEST] Method: {request.method}, Path: {request.url.path}, Status: {response.status_code}")
    
    return response

# exception handler for 404 Not Found errors
@app.exception_handler(404)
async def not_found_exception_handler(request: Request,self):
    return JSONResponse(
        status_code=404,
        content={"message": "The requested resource was not found"}
    )

# API Endpoints
@app.get("/hello")
async def hello():
    return {"message": "Hello, Welcome to FastAPI!"}

@app.get("/")
async def root():
    return {"message": "FastAPI"}

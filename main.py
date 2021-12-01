from typing import List
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from router import loja
import uvicorn


app = FastAPI()

app.include_router(loja)



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
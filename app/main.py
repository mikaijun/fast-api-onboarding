import firebase_admin

from fastapi import FastAPI
from firebase_admin import credentials
from firebase_admin import credentials
from routers import users

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = FastAPI()
app.include_router(users.router)

# リクエストボディの定義
# class Message(BaseModel):
#   name: str

# @lru_cache()
# def get_settings():
#     return Settings()

# 認証関数の定義
# def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
#     if not cred:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"}
#         )
#     try:
#         cred = auth.verify_id_token(cred.credentials)
#     except:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"}
#         )
#     return cred

# getを定義
# @app.get("/hello")
# def read_root(cred = Depends(get_current_user)):
#     uid = cred.get("uid")
#     return {"message": f"Hello, {uid}!"}

# # postを定義
# @app.post("/hello")
# def create_message(message: Message, cred = Depends(get_current_user)):
#     uid = cred.get("uid")
#     return {"message": f"Hello, {message.name}! Your uid is [{uid}]"}

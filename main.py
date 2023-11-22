from fastapi import FastAPI,UploadFile,Form,Response,Depends
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Annotated
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
import sqlite3



con = sqlite3.connect('items.db',check_same_thread=False)
cur = con.cursor()

# 실행시킬때 테이블을 만들도록 하는데, items라는 테이블이 없을때만 생성하도록함!
cur.execute(f"""
            CREATE TABLE IF NOT EXISTS items (
	            id INTEGER PRIMARY KEY,
	            title TEXT NOT NULL,
    	        image BLOB,
	            price INTEGER NOT NULL,
	            description TEXT,
	            place TEXT NOT NULL,	
	            insertAt INTEGER NOT NULL
	);
""")

app = FastAPI()

SECRET = "super-coding"
manager = LoginManager(SECRET,'/login')

# //로그인 매니저가 쿼리를 조회할때 키를 함께 조회함
@manager.user_loader()
def query_user(data):
    WHERE_STATEMENTS = f'id="{data}"'
    if type(data) == dict:
        WHERE_STATEMENTS = f'''id="{data['id']}"'''
    
    con.row_factory =sqlite3.Row
    cur=con.cursor()
    user = cur.execute(f"""
                       SELECT * from users WHERE {WHERE_STATEMENTS}
                       """).fetchone()
    return user

@app.post('/login')
def login(id:Annotated[str,Form()],
          password:Annotated[str,Form()]):
     
    user = query_user(id)
    if not user:
        raise InvalidCredentialsException
    # status를 자동으로 내려주게됨
    elif password != user["password"]:
        # user["password"]로 했더니 에러(tuple) 나서 인덱스값으로 변경해줌 -> 컬럼명을 같이 가져오지 않았기때문임! con.row_factory =sqlite3.Row 
        raise InvalidCredentialsException
    # 파이썬에선s raise를 통해 에러메시지 던짐
    # 파이썬에선 else if = elif

    access_token = manager.create_access_token(data={
        'sub': {
        'id':user['id'],
        'name':user['name'],
        'email':user['email']        
        }
    })
    
    
    return {'access_token':access_token}




@app.post('/signup')
def signup(id:Annotated[str,Form()],password:Annotated[str,Form()],
           name:Annotated[str,Form()],
           email:Annotated[str,Form()]):
    cur.execute(f"""
                INSERT INTO users(id,name,email,password)
                VALUES ('{id}','{name}','{email}','{password}')
                """)
    con.commit()
    return '200'




@app.post('/items')
async def create_item(image:UploadFile,
                title:Annotated[str,Form()],
                price:Annotated[int,Form()],
                description:Annotated[str,Form()],
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]):
    
    image_bytes = await image.read()
    cur.execute(f"""
                INSERT INTO items(image,title,price,description,place,insertAt)
                VALUES ('{image_bytes.hex()}','{title}',{price},'{description}','{place}',{insertAt})
                """)
    con.commit()
    return '200'


@app.get('/items')
async def get_items(user=Depends(manager)):
    #컬럼명도 같이 가져옴
    con.row_factory =sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(f"""
                       SELECT * FROM items
                       """).fetchall()
    
    
    return JSONResponse(jsonable_encoder(dict(row) for row in rows))


@app.get('/images/{item_id}')
async def get_image(item_id):
    cur=con.cursor()
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id={item_id}
                              """).fetchone()[0]
    return Response(content=bytes.fromhex(image_bytes), media_type='image/*')




app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


from fastapi import FastAPI,UploadFile,Form,Response
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Annotated
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
async def get_items():
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



app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/users')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user/id')
async def get_user_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/student/update')
async def put_student_update(raw_data: schemas.PutStudentUpdate, db: Session = Depends(get_db)):
    try:
        return await service.put_student_update(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.patch('/update')
async def patch_update(raw_data: schemas.PatchUpdate, db: Session = Depends(get_db)):
    try:
        return await service.patch_update(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login/user')
async def post_login_user(raw_data: schemas.PostLoginUser, db: Session = Depends(get_db)):
    try:
        return await service.post_login_user(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/document')
async def post_document(document: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_document(db, document)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))


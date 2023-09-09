from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

# SQLAlchemy에 이미 존재하는 테이블에 맞춰 클래스를 정의
Base = declarative_base()

class Issued(Base):
    __tablename__ = 'Issued'
    
    ownerid = Column(Integer, primary_key=True)
    tokenid = Column(Integer, primary_key=True)
    contractAddr = Column(String, primary_key=True)

# 데이터베이스 연결
engine = create_engine('')

Session = sessionmaker(bind=engine)
session = Session()

# 텍스트 파일 읽기
with open('/Users/kang-yeeun/Downloads/Issued.txt', 'r') as f:
    next(f) 
    lines = f.readlines()

# 텍스트 파일 파싱 및 데이터 삽입
for line in lines:
    line = line.strip()
    if not line:
        continue
    
    parts = line.split(", ")
    
    issued = Issued(
        ownerid=int(parts[0]),
        tokenid=int(parts[1]),
        contractAddr=parts[2]
    )
    
    session.add(issued)

# 데이터베이스에 적용
session.commit()

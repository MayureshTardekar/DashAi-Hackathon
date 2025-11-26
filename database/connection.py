"""
SQLite connection for local development
Simple, always-works database setup
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# Use SQLite by default for local dev
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///ml_analytics.db')

# Create engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={'check_same_thread': False} if 'sqlite' in DATABASE_URL else {}
)
print(f"✅ Using database: {DATABASE_URL}")

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(SessionLocal)

# Base for models
Base = declarative_base()

def get_db():
    """Get database session (for dependency injection)"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database (create tables if needed)"""
    from database.models import User, AuthNonce, Upload, Forecast, AuditLog
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized")

from sqlalchemy import Integer, String

from app.models.user import User

def test_user_table_name():
    assert User.__tablename__ == "users"


def test_user_columns_exist():
    columns= User.__table__.columns
    assert "id" in columns
    assert "name" in columns
    assert "email" in columns
    assert "password" in columns
    assert "role" in columns

def test_user_id_column_type():
    id_column = User.__table__.columns["id"]
    assert isinstance(id_column.type, Integer)

def test_user_name_column_type():
    name_column = User.__table__.columns["name"]
    assert isinstance(name_column.type, String)


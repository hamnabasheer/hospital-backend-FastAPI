
from sqlalchemy import Integer, String, ForeignKey
from app.models.patient import Patient

def test_patient_table_name():
    assert Patient.__tablename__ == "patients"


def test_patient_columns_exist():
    columns = Patient.__table__.columns

    assert "id" in columns
    assert "user_id" in columns
    assert "age" in columns
    assert "gender" in columns


def test_patient_id_column_type():
    id_column = Patient.__table__.columns["id"]
    assert isinstance(id_column.type, Integer)


def test_patient_user_id_foreign_key():
    user_id_column = Patient.__table__.columns["user_id"]
    foreign_keys = list(user_id_column.foreign_keys)

    assert len(foreign_keys) == 1
    assert foreign_keys[0].target_fullname == "users.id"


def test_patient_age_column_type():
    age_column = Patient.__table__.columns["age"]
    assert isinstance(age_column.type, Integer)



def test_patient_gender_column_type():
    gender_column = Patient.__table__.columns["gender"]
    assert isinstance(gender_column.type, String)

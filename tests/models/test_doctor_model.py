from app.models.doctor import Doctor
from app.models.user import User


from sqlalchemy import Integer, String, Boolean


def test_doctor_table_name():
    assert Doctor.__tablename__ == "doctors"


def test_doctor_columns_exist():
    columns = Doctor.__table__.columns

    assert "id" in columns
    assert "user_id" in columns
    assert "specialization" in columns
    assert "experience" in columns
    assert "approved" in columns


def test_doctor_id_column_type():
    id_column = Doctor.__table__.columns["id"]
    assert isinstance(id_column.type, Integer)


def test_doctor_user_id_foreign_key():
    user_id_column = Doctor.__table__.columns["user_id"]
    foreign_keys = list(user_id_column.foreign_keys)

    assert len(foreign_keys) == 1
    assert foreign_keys[0].target_fullname == "users.id"


def test_doctor_specialization_column_type():
    specialization_column = Doctor.__table__.columns["specialization"]
    assert isinstance(specialization_column.type, String)


def test_doctor_experience_column_type():
    experience_column = Doctor.__table__.columns["experience"]
    assert isinstance(experience_column.type, Integer)


def test_doctor_approved_column_type():
    approved_column = Doctor.__table__.columns["approved"]
    assert isinstance(approved_column.type, Boolean)


def test_doctor_approved_default():
    approved_column = Doctor.__table__.columns["approved"]
    assert approved_column.default is not None

def test_create_doctor(db_session):
    # First creating a user (because Doctor depends on User via FK)
    user = User(
        name="Dr Test",
        email="drtest@example.com",
        password="hashedpassword",
        role="doctor"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    # Now creating doctor profile
    doctor = Doctor(
        user_id=user.id,
        specialization="Cardiology",
        experience=5
    )

    db_session.add(doctor)
    db_session.commit()
    db_session.refresh(doctor)

    # Assertions
    assert doctor.id is not None
    assert doctor.user_id == user.id
    assert doctor.specialization == "Cardiology"
    assert doctor.experience == 5
    assert doctor.approved is False  # default value

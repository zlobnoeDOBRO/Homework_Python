import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Импортируем из того же пакета
from lesson_09.database import Base, Student, DATABASE_URL

# Тестовые данные
TEST_NAME = "Test Student"
TEST_EMAIL = "test.student@example.com"
UPDATED_NAME = "Updated Student"
UPDATED_EMAIL = "updated.student@example.com"


@pytest.fixture
def db_session():
    """Создает сессию базы данных и очищает тестовые данные после теста"""
    engine = create_engine(DATABASE_URL)

    # Пересоздаем таблицы чтобы гарантировать правильную структуру
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    # Простая очистка тестовых данных
    session.query(Student).filter(
        Student.email.in_([TEST_EMAIL, UPDATED_EMAIL])
    ).delete()
    session.commit()
    session.close()


def test_create_student(db_session):
    """Тест добавления студента"""
    student = Student(name=TEST_NAME, email=TEST_EMAIL)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    assert student.id is not None
    assert student.name == TEST_NAME
    assert student.email == TEST_EMAIL
    assert student.deleted_at is None


def test_update_student(db_session):
    """Тест изменения студента"""
    student = Student(name=TEST_NAME, email=TEST_EMAIL)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student.name = UPDATED_NAME
    student.email = UPDATED_EMAIL
    db_session.commit()
    db_session.refresh(student)

    assert student.name == UPDATED_NAME
    assert student.email == UPDATED_EMAIL


def test_soft_delete_student(db_session):
    """Тест мягкого удаления"""
    student = Student(name=TEST_NAME, email=TEST_EMAIL)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student.deleted_at = datetime.now()
    db_session.commit()
    db_session.refresh(student)

    assert student.deleted_at is not None

    # Проверяем что не показывается в активных
    active_students = db_session.query(Student).filter(
        Student.deleted_at.is_(None)).all()
    student_emails = [s.email for s in active_students]
    assert TEST_EMAIL not in student_emails

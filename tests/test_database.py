from sqlalchemy import select

from fast_demo.models import User


def test_create_user(session):
    session.query(User).delete()
    session.commit()

    user = User(username="Test", email="test@test.com", password="secret")
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == "test@test.com"))

    assert result.id == 1

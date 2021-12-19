import pytest

from project import create_app, db
from project.models import Package, User


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("project.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="module")
def add_user():
    def _add_user(brilliant_number, package_id, next_billing_time):
        user = User(
            brilliant_number=brilliant_number,
            package_id=package_id,
            next_billing_time=next_billing_time,
        )
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user


@pytest.fixture(scope="module")
def add_package():
    def _add_package(package_name, package_size, package_price):
        package = Package(
            package_name=package_name,
            package_size=package_size,
            package_price=package_price,
        )
        db.session.add(package)
        db.session.commit()
        return package

    return _add_package

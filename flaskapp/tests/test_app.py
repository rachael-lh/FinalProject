from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app, db, Users

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                secret_key='Secret Key',
                DEBUG=True
                )        
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        # Creating a test list
        sample1 = Users(
            full_name = "Tester",
            email = "Tester@gmail.com",
            user_password = "07914757867",
        )

        # Save list to db
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_open_users(self):
        response = self.client.get(url_for('insert'))
        self.assertEqual(response.status_code, 405)
        self.assertIn(b'', response.data)
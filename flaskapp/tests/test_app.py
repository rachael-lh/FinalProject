from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app, db, usergoals

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
        sample1 = usergoals(
            goals = "Tester",
            date_started= "Tuesday",
            date_endgoal= "Friday",
            username= "Ben"
        )

        # Save list to db
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_insert_endpoint_returns_405(self):
        response = self.client.get(url_for('insert'))
        self.assertEqual(response.status_code, 405)
        self.assertIn(b'', response.data)

    def test_homepage_returns_200(self):
        response = self.client.get()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)    
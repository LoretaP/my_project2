import allure
import pytest
import requests


@pytest.fixture()
def login():
    data = {
        "username": "admin",
        "password": "password123"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://restful-booker.herokuapp.com/auth', json=data, headers=headers)
    return response.json()['token']


@pytest.fixture()
def create_booking():
    data = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://restful-booker.herokuapp.com/booking',
        json=data,
        headers=headers
    )
    return response.json()


def test_GetBookingIds():
    response = requests.get('https://restful-booker.herokuapp.com/booking')
    assert response.status_code == 200, 'Status Code is incorrect'
    assert len(response.json()) != 0, 'Error data is empty'


def test_GetBooking():
    booking_id = 1
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
    assert response.status_code == 200, 'Status Code is incorrect'



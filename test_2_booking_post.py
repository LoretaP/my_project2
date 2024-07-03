import requests
import allure
from my_data import MyData
import pytest

@allure.feature('TEST BOOKING POST - feature')
@allure.suite('TEST BOOKING POST - suite')
class TestBookingPost():

    @allure.title('Test Create Booking')
    @allure.description('This test case verifies that the system successfully create new booking')
    @pytest.mark.regression
    @pytest.mark.smoke

    def test_create_booking(self):
        data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        headers = {'Content-Type': 'application/json'}
        with allure.step('Send POST request to create new booking'):
            response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
            json=data,
            headers=headers
        )
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

        response_data = response.json()
        with allure.step('Verify the response contains "bookingid'):
            assert 'bookingid' in response_data, "The response does not contain 'bookingid'"

        booking = response_data['booking']
        with allure.step('Verify first name'):
            assert booking['firstname'] == data['firstname'], f"Expected firstname {data['firstname']}, but got {booking['firstname']}"
        with allure.step('Verify last name'):
            assert booking['lastname'] == data['lastname'], f"Expected lastname {data['lastname']}, but got {booking['lastname']}"
        with allure.step('Verify totalprice'):
            assert booking['totalprice'] == data['totalprice'], f"Expected totalprice {data['totalprice']}, but got {booking['totalprice']}"
        with allure.step('Verify depositpaid'):
            assert booking['depositpaid'] == data['depositpaid'], f"Expected depositpaid {data['depositpaid']}, but got {booking['depositpaid']}"
        with allure.step('Verify bookingdates'):
            assert booking['bookingdates']['checkin'] == data['bookingdates']['checkin'], f"Expected checkin {data['bookingdates']['checkin']}, but got {booking['bookingdates']['checkin']}"
        with allure.step('Verify checkout date'):
            assert booking['bookingdates']['checkout'] == data['bookingdates']['checkout'], f"Expected checkout {data['bookingdates']['checkout']}, but got {booking['bookingdates']['checkout']}"
        with allure.step('Verify additionalneeds'):
            assert booking['additionalneeds'] == data['additionalneeds'], f"Expected additionalneeds {data['additionalneeds']}, but got {booking['additionalneeds']}"

        MyData.booking_id = response_data['bookingid']



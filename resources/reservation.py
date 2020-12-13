from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.reservation import Reservation
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from datetime import datetime


class ReservationListResource(Resource):
    def get(self):

        reservations = Reservation.get_by_is_listed()

        data = []
        for reservation in reservations:
            data.append(reservation.data())

        return {'data': data}, HTTPStatus.OK

    @jwt_required
    def post(self):

        def is_valid_date(year, month, day):
            day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day_count_for_month[2] = 29
            return 1 <= month <= 12 and 1 <= day <= day_count_for_month[month]

        json_data = request.get_json()
        current_user = get_jwt_identity()
        date_time_str = json_data['datetime']
        date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H')

        if date_time_obj < datetime.now():
            return {'message': 'You cant time travel'}, HTTPStatus.BAD_REQUEST

        if not is_valid_date(date_time_obj.year, date_time_obj.month, date_time_obj.day):
            return {'not a real date'}, HTTPStatus.BAD_REQUEST

        if date_time_obj.weekday() > 5:
            return {'message': 'Room cant be reserved for the weekend'}, HTTPStatus.BAD_REQUEST

        ress_list = Reservation.get_by_room_id(json_data['room_id'])

        for item in ress_list:
            if item.time == date_time_obj:
                return {'message': 'Already booked'}

        reservation = Reservation(name=json_data['name'], user_id=current_user, room_id=json_data['room_id'],
                                  description=json_data['description'], time=date_time_obj)
        reservation.save()
        return reservation.data(), HTTPStatus.CREATED


class ReservationResource(Resource):

    @jwt_required
    def put(self, reservation_id):

        json_data = request.get_json()

        reservation = Reservation.get_by_id(reservation_id=reservation_id)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != reservation.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        reservation.room_id = json_data['room_id']
        reservation.description = json_data['description']
        reservation.time = json_data['time']

        reservation.save()

        return reservation.data(), HTTPStatus.OK

    @jwt_required
    def delete(self, reservation_id):

        reservation = Reservation.get_by_id(reservation_id=reservation_id)

        if reservation is None:
            return {'message': 'Reservation not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != reservation.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        reservation.delete()

        return {}, HTTPStatus.NO_CONTENT

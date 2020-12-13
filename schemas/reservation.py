from marshmallow import Schema, fields
from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError
from schemas.user import UserSchema


class ReservationSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Int(dump_only=True)
    room_id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(validate=[validate.Length(max=200)])
    time = fields.DateTime(dump_only=True)
    is_listed = fields.Boolean(dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    author = fields.Nested(UserSchema, attribute='user', dump_only=True, only=['id', 'username'])

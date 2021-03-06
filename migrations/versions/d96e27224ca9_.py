"""empty message

Revision ID: d96e27224ca9
Revises: 7b57682974f2
Create Date: 2020-12-11 16:47:35.362450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd96e27224ca9'
down_revision = '7b57682974f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('room_id', sa.Integer(), nullable=True))
    op.drop_constraint('reservation_user_id_key', 'reservation', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('reservation_user_id_key', 'reservation', ['user_id'])
    op.drop_column('reservation', 'room_id')
    # ### end Alembic commands ###

"""empty message

Revision ID: 80450b417e9d
Revises: d96e27224ca9
Create Date: 2020-12-13 10:31:26.049779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80450b417e9d'
down_revision = 'd96e27224ca9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reservation', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reservation', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###

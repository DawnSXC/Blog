"""empty message

Revision ID: 038803ec4c3a
Revises: 3e257f8c8dc4
Create Date: 2021-12-01 00:23:30.511532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '038803ec4c3a'
down_revision = '3e257f8c8dc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('dislike_times', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'dislike_times')
    # ### end Alembic commands ###

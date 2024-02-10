"""login

Revision ID: 226b56750d42
Revises: d345f1119abb
Create Date: 2024-02-05 17:10:56.394613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '226b56750d42'
down_revision = 'd345f1119abb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('is_owner', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

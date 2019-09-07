"""empty message

Revision ID: 4157ad09ab71
Revises: ee0c1e6f539b
Create Date: 2019-09-05 20:56:25.701876

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4157ad09ab71'
down_revision = 'ee0c1e6f539b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('permissions', sa.Integer(), nullable=True))
    op.drop_column('role', 'permission')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('permission', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('role', 'permissions')
    # ### end Alembic commands ###
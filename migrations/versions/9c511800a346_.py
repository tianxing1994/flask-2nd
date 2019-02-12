"""empty message

Revision ID: 9c511800a346
Revises: e02f90d10cb8
Create Date: 2019-02-12 20:57:27.485905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c511800a346'
down_revision = 'e02f90d10cb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_ibfk_1', 'user', type_='foreignkey')
    op.create_foreign_key(None, 'user', 'company', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.create_foreign_key('user_ibfk_1', 'user', 'user', ['company_id'], ['id'])
    # ### end Alembic commands ###

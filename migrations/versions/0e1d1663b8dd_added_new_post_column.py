"""Added new post column

Revision ID: 0e1d1663b8dd
Revises: c3f52ef86bfb
Create Date: 2022-09-21 10:30:55.297941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e1d1663b8dd'
down_revision = 'c3f52ef86bfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'date_created')
    # ### end Alembic commands ###

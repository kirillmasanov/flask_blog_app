"""garavarar_hash

Revision ID: 29906a7053ba
Revises: 4d0362b31018
Create Date: 2020-06-14 12:13:50.700947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29906a7053ba'
down_revision = '4d0362b31018'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###

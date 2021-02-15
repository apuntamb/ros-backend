"""empty message

Revision ID: d8648225984f
Revises: 37ef515b370d
Create Date: 2021-02-16 19:28:54.637819

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd8648225984f'
down_revision = '37ef515b370d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rh_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account', sa.Text(), nullable=False),
    sa.CheckConstraint('NOT(account IS NULL)'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('systems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('inventory_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('inventory_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('systems')
    op.drop_table('rh_accounts')
    # ### end Alembic commands ###

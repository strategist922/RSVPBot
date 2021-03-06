"""add stream and subject to event

Revision ID: ca2cae2681ac
Revises: 087277c93550
Create Date: 2017-05-16 12:58:10.917554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca2cae2681ac'
down_revision = '087277c93550'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('stream', sa.String(), nullable=True))
    op.add_column('event', sa.Column('subject', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'subject')
    op.drop_column('event', 'stream')
    # ### end Alembic commands ###

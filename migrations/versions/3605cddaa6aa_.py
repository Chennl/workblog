"""empty message

Revision ID: 3605cddaa6aa
Revises: e76e06ba8fa7
Create Date: 2020-08-01 16:07:21.088347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3605cddaa6aa'
down_revision = 'e76e06ba8fa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('host_id', sa.Integer(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###

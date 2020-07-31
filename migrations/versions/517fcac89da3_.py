"""empty message

Revision ID: 517fcac89da3
Revises: 7111c902b158
Create Date: 2020-07-29 10:51:55.293927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '517fcac89da3'
down_revision = '7111c902b158'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###

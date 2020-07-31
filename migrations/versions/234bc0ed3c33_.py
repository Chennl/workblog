"""empty message

Revision ID: 234bc0ed3c33
Revises: 517fcac89da3
Create Date: 2020-07-29 11:10:55.109921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '234bc0ed3c33'
down_revision = '517fcac89da3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('post_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###
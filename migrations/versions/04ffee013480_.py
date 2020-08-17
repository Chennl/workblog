"""empty message

Revision ID: 04ffee013480
Revises: 0262bc4cb901
Create Date: 2020-08-02 16:19:11.388775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04ffee013480'
down_revision = '0262bc4cb901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=True))
        batch_op.drop_column('categories')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('categories', sa.VARCHAR(length=50), nullable=True))
        batch_op.drop_column('category')

    # ### end Alembic commands ###
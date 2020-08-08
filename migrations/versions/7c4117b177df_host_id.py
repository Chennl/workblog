""" host_id

Revision ID: 7c4117b177df
Revises: 6e3e817bb7dd
Create Date: 2020-08-01 15:46:17.423940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c4117b177df'
down_revision = '6e3e817bb7dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #with op.batch_alter_table('comments', schema=None) as batch_op:
    #    batch_op.drop_column('thread_sequence')
    #   batch_op.drop_column('host_post_id')

    #with op.batch_alter_table('likes', schema=None) as batch_op:
    #    batch_op.drop_constraint(None, type_='foreignkey')
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])

    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('host_post_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('thread_sequence', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###

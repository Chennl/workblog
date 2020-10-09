"""empty message

Revision ID: 48a50c09818c
Revises: 79bb2830a1a3
Create Date: 2020-10-05 20:33:54.088869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48a50c09818c'
down_revision = '79bb2830a1a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mall_goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('privilegePrice', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('imgUrl', sa.String(length=256), nullable=True),
    sa.Column('details', sa.String(length=512), nullable=True),
    sa.Column('remark', sa.String(length=128), nullable=True),
    sa.Column('createDate', sa.DateTime(), nullable=True),
    sa.Column('updateDate', sa.DateTime(), nullable=True),
    sa.Column('clickRate', sa.Integer(), nullable=True),
    sa.Column('buyRate', sa.Integer(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('isHot', sa.Integer(), nullable=True),
    sa.Column('isNew', sa.Integer(), nullable=True),
    sa.Column('classifyId', sa.Integer(), nullable=True),
    sa.Column('discount', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('activityId', sa.Integer(), nullable=True),
    sa.Column('desc', sa.String(length=128), nullable=True),
    sa.Column('shopGoodsImageList', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    #op.drop_table('sqlite_sequence')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.drop_table('mall_goods')
    # ### end Alembic commands ###
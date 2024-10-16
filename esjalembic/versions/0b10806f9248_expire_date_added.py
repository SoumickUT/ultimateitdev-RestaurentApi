"""expire date added

Revision ID: 0b10806f9248
Revises: 4c8dd2e1494c
Create Date: 2022-09-15 11:08:19.377941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b10806f9248'
down_revision = '4c8dd2e1494c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_order_and_payment-checkout', sa.Column('card_expire_date', sa.DateTime(), nullable=True))
    op.drop_column('tbl_order_and_payment-checkout', 'card_month')
    op.drop_column('tbl_order_and_payment-checkout', 'card_year')
    op.add_column('tbl_order_and_payment-order', sa.Column('card_expire_date', sa.DateTime(), nullable=True))
    op.drop_column('tbl_order_and_payment-order', 'card_month')
    op.drop_column('tbl_order_and_payment-order', 'card_year')
    op.add_column('tbl_order_and_payment-plan_order', sa.Column('card_expire_date', sa.DateTime(), nullable=True))
    op.drop_column('tbl_order_and_payment-plan_order', 'card_month')
    op.drop_column('tbl_order_and_payment-plan_order', 'card_year')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_order_and_payment-plan_order', sa.Column('card_year', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tbl_order_and_payment-plan_order', sa.Column('card_month', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('tbl_order_and_payment-plan_order', 'card_expire_date')
    op.add_column('tbl_order_and_payment-order', sa.Column('card_year', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tbl_order_and_payment-order', sa.Column('card_month', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('tbl_order_and_payment-order', 'card_expire_date')
    op.add_column('tbl_order_and_payment-checkout', sa.Column('card_year', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tbl_order_and_payment-checkout', sa.Column('card_month', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('tbl_order_and_payment-checkout', 'card_expire_date')
    # ### end Alembic commands ###

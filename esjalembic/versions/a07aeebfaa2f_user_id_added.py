"""user_id added

Revision ID: a07aeebfaa2f
Revises: 55d5dd3dccea
Create Date: 2022-09-13 11:14:08.688358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a07aeebfaa2f'
down_revision = '55d5dd3dccea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_stu_adm-pricing_plan-service_type', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tbl_stu_adm-pricing_plan-service_type', 'tbl_stu_usr-users', ['user_id'], ['id'])
    op.add_column('tbl_stu_adm-pricing_plan-service_type_has_service', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tbl_stu_adm-pricing_plan-service_type_has_service', 'tbl_stu_usr-users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tbl_stu_adm-pricing_plan-service_type_has_service', type_='foreignkey')
    op.drop_column('tbl_stu_adm-pricing_plan-service_type_has_service', 'user_id')
    op.drop_constraint(None, 'tbl_stu_adm-pricing_plan-service_type', type_='foreignkey')
    op.drop_column('tbl_stu_adm-pricing_plan-service_type', 'user_id')
    # ### end Alembic commands ###

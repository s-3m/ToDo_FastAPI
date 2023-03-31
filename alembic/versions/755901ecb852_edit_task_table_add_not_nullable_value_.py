"""edit Task table - add not nullable value in user_id

Revision ID: 755901ecb852
Revises: a14675c956db
Create Date: 2023-03-30 12:36:49.561239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '755901ecb852'
down_revision = 'a14675c956db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###
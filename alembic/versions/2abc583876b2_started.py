"""started

Revision ID: 2abc583876b2
Revises: 
Create Date: 2023-10-29 11:19:04.606993

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2abc583876b2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_id', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###

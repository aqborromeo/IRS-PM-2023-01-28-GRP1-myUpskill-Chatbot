"""create user chat reference

Revision ID: 6111621905a4
Revises: 43d1f68491a5
Create Date: 2023-04-05 20:41:22.949909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6111621905a4'
down_revision = '43d1f68491a5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_chat_session_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'chat_sessions', ['last_chat_session_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'last_chat_session_id')
    # ### end Alembic commands ###
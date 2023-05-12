"""Add salary similarity column in results table

Revision ID: 8c14c1a81f61
Revises: 328ca9d437be
Create Date: 2023-05-10 00:47:48.559432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c14c1a81f61'
down_revision = '328ca9d437be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('salary_similarity', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'salary_similarity')
    # ### end Alembic commands ###
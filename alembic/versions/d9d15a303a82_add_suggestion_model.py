"""add suggestion model

Revision ID: d9d15a303a82
Revises: 2e61a0e7c3e9
Create Date: 2024-12-21 20:42:55.595271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9d15a303a82'
down_revision = '2e61a0e7c3e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suggestion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('details', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_suggestion_id'), 'suggestion', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_suggestion_id'), table_name='suggestion')
    op.drop_table('suggestion')
    # ### end Alembic commands ###
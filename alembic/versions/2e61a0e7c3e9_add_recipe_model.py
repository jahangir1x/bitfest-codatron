"""add recipe model

Revision ID: 2e61a0e7c3e9
Revises: 236efc6a4767
Create Date: 2024-12-21 20:18:51.785201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e61a0e7c3e9'
down_revision = '236efc6a4767'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('details', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recipe_id'), 'recipe', ['id'], unique=False)
    op.drop_index('ix_ingredient_name', table_name='ingredient')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_ingredient_name', 'ingredient', ['name'], unique=False)
    op.drop_index(op.f('ix_recipe_id'), table_name='recipe')
    op.drop_table('recipe')
    # ### end Alembic commands ###
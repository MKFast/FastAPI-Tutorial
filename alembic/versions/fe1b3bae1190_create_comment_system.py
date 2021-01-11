"""create comment system

Revision ID: fe1b3bae1190
Revises: 81aa16a88604
Create Date: 2021-01-10 17:29:42.137055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe1b3bae1190'
down_revision = '81aa16a88604'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('name', sa.String(100)),
        sa.Column('email', sa.String(1000)),
        sa.Column('body',sa.String(1000)),
        sa.Column('post_id',sa.Integer),
        sa.Column('is_active',sa.Boolean),
        sa.Column('created_date',sa.DateTime)
    )


def downgrade():
    pass

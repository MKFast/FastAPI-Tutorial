"""create post table

Revision ID: 89d3f657f59b
Revises: dbdf996e68d9
Create Date: 2020-11-26 21:25:49.335003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89d3f657f59b'
down_revision = 'dbdf996e68d9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('title', sa.String(100)),
        sa.Column('body',sa.String(1000)),
        sa.Column('owner_id',sa.Integer),
        sa.Column('is_active',sa.Boolean),
        sa.Column('created_date',sa.DateTime)
    )


def downgrade():
    pass

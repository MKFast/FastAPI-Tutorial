"""adding image field

Revision ID: 81aa16a88604
Revises: 89d3f657f59b
Create Date: 2020-12-11 17:50:49.578035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81aa16a88604'
down_revision = '89d3f657f59b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('url',sa.String(200))
    )


def downgrade():
    pass

"""changes email Column to yahoo

Revision ID: 94ef7b497386
Revises: 28a0408a9f41
Create Date: 2024-09-15 20:33:09.954530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94ef7b497386'
down_revision = '28a0408a9f41'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'email', new_column_name="yahoo")

def downgrade() -> None:
    op.alter_column('scholars', "yahoo", new_column_name='email')

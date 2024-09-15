"""Renaming students to scholars

Revision ID: 28a0408a9f41
Revises: 791279dd0760
Create Date: 2024-09-15 19:37:11.313679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28a0408a9f41'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

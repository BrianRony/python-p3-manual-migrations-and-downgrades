"""Renaming students to scholars

Revision ID: 2648c3f4f7b9
Revises: 791279dd0760
Create Date: 2024-07-29 11:46:39.758566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2648c3f4f7b9'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
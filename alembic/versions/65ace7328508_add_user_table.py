"""add user table

Revision ID: 65ace7328508
Revises: 4ab1d26a85c4
Create Date: 2026-06-24 23:31:49.490134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65ace7328508'
down_revision: Union[str, Sequence[str], None] = '4ab1d26a85c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
    'users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
              server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass

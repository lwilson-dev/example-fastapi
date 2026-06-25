"""add content column to posts table

Revision ID: 4ab1d26a85c4
Revises: 9d830a095110
Create Date: 2026-06-24 23:27:00.939111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ab1d26a85c4'
down_revision: Union[str, Sequence[str], None] = '9d830a095110'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", 'content')
    pass

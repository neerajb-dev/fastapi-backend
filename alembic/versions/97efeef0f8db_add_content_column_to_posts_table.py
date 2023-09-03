"""add content column to posts table

Revision ID: 97efeef0f8db
Revises: c0fc63aed401
Create Date: 2023-09-03 23:23:39.304924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "97efeef0f8db"
down_revision: Union[str, None] = "c0fc63aed401"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass

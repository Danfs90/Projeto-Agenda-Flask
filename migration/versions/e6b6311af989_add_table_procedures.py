"""add table procedures

Revision ID: e6b6311af989
Revises: d0a445b97d4c
Create Date: 2023-10-07 16:25:22.118274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6b6311af989'
down_revision: Union[str, None] = 'd0a445b97d4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('procedures',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name_procedures', sa.VARCHAR(256), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('procedures')
    # ### end Alembic commands ###

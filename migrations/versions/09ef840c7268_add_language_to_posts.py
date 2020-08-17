"""add language to posts

Revision ID: 09ef840c7268
Revises: b44aeaef5425
Create Date: 2020-08-17 22:28:55.915733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09ef840c7268'
down_revision = 'b44aeaef5425'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
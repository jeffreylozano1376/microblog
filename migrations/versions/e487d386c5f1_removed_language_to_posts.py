"""removed language to posts

Revision ID: e487d386c5f1
Revises: 09ef840c7268
Create Date: 2020-08-17 23:01:56.302521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e487d386c5f1'
down_revision = '09ef840c7268'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.VARCHAR(length=5), nullable=True))
    # ### end Alembic commands ###

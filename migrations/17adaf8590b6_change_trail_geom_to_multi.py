"""Change Trail.geom to multi

Revision ID: 17adaf8590b6
Revises: 24286ef61686
Create Date: 2014-12-03 19:22:10.906849

"""

# revision identifiers, used by Alembic.
revision = '17adaf8590b6'
down_revision = '24286ef61686'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trail', schema=None) as batch_op:
        batch_op.drop_index('idx_trail_geom')

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trail', schema=None) as batch_op:
        batch_op.create_index('idx_trail_geom', ['geom'], unique=False)

    ### end Alembic commands ###

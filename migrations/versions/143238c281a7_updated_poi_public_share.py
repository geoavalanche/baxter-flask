"""updated poi.public_share

Revision ID: 143238c281a7
Revises: 1a373dc6361a
Create Date: 2014-12-07 07:18:22.540143

"""

# revision identifiers, used by Alembic.
revision = '143238c281a7'
down_revision = '1a373dc6361a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.drop_index('idx_avalanche_paths_path', table_name='avalanche_paths')
    op.add_column('points_of_interests', sa.Column('public_share', sa.Boolean(), nullable=True))
    #op.drop_index('idx_points_of_interests_point', table_name='points_of_interests')
    op.drop_column('points_of_interests', 'public_shar')
    #op.drop_index('idx_trails_geom', table_name='trails')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.create_index('idx_trails_geom', 'trails', ['geom'], unique=False)
    op.add_column('points_of_interests', sa.Column('public_shar', sa.BOOLEAN(), autoincrement=False, nullable=True))
    #op.create_index('idx_points_of_interests_point', 'points_of_interests', ['point'], unique=False)
    op.drop_column('points_of_interests', 'public_share')
    #op.create_index('idx_avalanche_paths_path', 'avalanche_paths', ['path'], unique=False)
    ### end Alembic commands ###

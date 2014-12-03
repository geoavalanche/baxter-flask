"""Initial WeatherOb

Revision ID: 2298920e3e1e
Revises: 4792a2f6b8d8
Create Date: 2014-12-02 22:25:41.459773

"""

# revision identifiers, used by Alembic.
revision = '2298920e3e1e'
down_revision = '4792a2f6b8d8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather_observations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('observer_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('sky', sa.String(length=40), nullable=True),
    sa.Column('precip_type', sa.String(length=40), nullable=True),
    sa.Column('precip_rate', sa.Float(), nullable=True),
    sa.Column('temp_max', sa.Float(), nullable=True),
    sa.Column('temp_min', sa.Float(), nullable=True),
    sa.Column('temp_present', sa.Float(), nullable=True),
    sa.Column('temp_trend', sa.String(length=40), nullable=True),
    sa.Column('pressure_present', sa.Float(), nullable=True),
    sa.Column('pressure_trend', sa.String(length=40), nullable=True),
    sa.Column('humidity', sa.Float(), nullable=True),
    sa.Column('wind_speed', sa.Float(), nullable=True),
    sa.Column('wind_direction', sa.String(length=40), nullable=True),
    sa.Column('wind_gust_max', sa.Float(), nullable=True),
    sa.Column('rain_24', sa.Float(), nullable=True),
    sa.Column('snow_depth', sa.Float(), nullable=True),
    sa.Column('snow_24', sa.Float(), nullable=True),
    sa.Column('snow_storm', sa.Float(), nullable=True),
    sa.Column('snow_8_temp', sa.Float(), nullable=True),
    sa.Column('snow_density', sa.Float(), nullable=True),
    sa.Column('snow_foot_pen', sa.Float(), nullable=True),
    sa.Column('snow_ram_pen', sa.Float(), nullable=True),
    sa.Column('snow_surface_form', sa.String(length=80), nullable=True),
    sa.Column('snow_surface_size', sa.Float(), nullable=True),
    sa.Column('snow_blowing_extent', sa.String(length=40), nullable=True),
    sa.Column('snow_water_equil', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['observer_id'], ['observers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    #op.drop_table('spatial_ref_sys')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.create_table('spatial_ref_sys',
    #sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    #sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    #sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    #sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    #sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    #sa.PrimaryKeyConstraint('srid', name=u'spatial_ref_sys_pkey')
    #)
    op.drop_table('weather_observations')
    ### end Alembic commands ###
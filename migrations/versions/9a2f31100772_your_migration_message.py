"""Your migration message

Revision ID: 9a2f31100772
Revises: 
Create Date: 2023-09-05 20:52:00.483476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a2f31100772'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('release_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('actors',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('age', sa.Integer(), nullable=False),
                    sa.Column('gender', sa.String(), nullable=False),
                    sa.Column('movie_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_table('persons')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persons',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='persons_pkey')
                    )
    op.drop_table('actors')
    op.drop_table('movies')
    # ### end Alembic commands ###

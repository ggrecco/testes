"""empty message

Revision ID: ff70ed4c92a8
Revises: 
Create Date: 2018-06-28 21:35:19.847317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff70ed4c92a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuario_email'), 'usuario', ['email'], unique=True)
    op.create_index(op.f('ix_usuario_nome'), 'usuario', ['nome'], unique=True)
    op.create_table('servidor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=140), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('ip', sa.String(length=25), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_index(op.f('ix_servidor_timestamp'), 'servidor', ['timestamp'], unique=False)
    op.create_table('dados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('servidor_id', sa.Integer(), nullable=True),
    sa.Column('produto', sa.String(length=20), nullable=True),
    sa.Column('cveid', sa.String(length=25), nullable=True),
    sa.Column('tipo', sa.String(length=25), nullable=True),
    sa.Column('datacorrecao', sa.String(length=50), nullable=True),
    sa.Column('nota', sa.Float(precision=50), nullable=True),
    sa.Column('acesso', sa.String(length=100), nullable=True),
    sa.Column('porta', sa.String(length=10), nullable=True),
    sa.Column('comentario', sa.String(length=5000), nullable=True),
    sa.ForeignKeyConstraint(['servidor_id'], ['servidor.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dados')
    op.drop_index(op.f('ix_servidor_timestamp'), table_name='servidor')
    op.drop_table('servidor')
    op.drop_index(op.f('ix_usuario_nome'), table_name='usuario')
    op.drop_index(op.f('ix_usuario_email'), table_name='usuario')
    op.drop_table('usuario')
    # ### end Alembic commands ###

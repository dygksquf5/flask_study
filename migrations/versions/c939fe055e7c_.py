"""empty message

Revision ID: c939fe055e7c
Revises: 0f04bbe54c67
Create Date: 2021-01-19 16:09:38.957089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c939fe055e7c'
down_revision = '0f04bbe54c67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('answer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['answer_id'], ['answer.id'], name=op.f('fk_comment_answer_id_answer'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name=op.f('fk_comment_question_id_question'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_comment_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_comment'))
    )
    op.drop_table('commnet')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commnet',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('modify_date', sa.DATETIME(), nullable=True),
    sa.Column('question_id', sa.INTEGER(), nullable=True),
    sa.Column('answer_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['answer_id'], ['answer.id'], name='fk_commnet_answer_id_answer', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name='fk_commnet_question_id_question', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_commnet_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='pk_commnet')
    )
    op.drop_table('comment')
    # ### end Alembic commands ###

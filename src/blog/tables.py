import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.Text, nullable=False)
    email = sa.Column(sa.Text, nullable=False)
    password_hash = sa.Column(sa.Text)

    __table_args__ = (
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email'),
    )


class Post(Base):
    __tablename__ = 'posts'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(100), nullable=False)
    text = sa.Column(sa.String(200), nullable=False, default=False)
    user_id = sa.Column(sa.Integer(), nullable=False)

    __table_args__ = (
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
    )


class Comment(Base):
    __tablename__ = 'comments'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer(), nullable=False)
    post_id = sa.Column(sa.Integer(), nullable=False)
    text = sa.Column(sa.String(200), nullable=False, default=False)

    __table_args__ = (
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id']),
    )
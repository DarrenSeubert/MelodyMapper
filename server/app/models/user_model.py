################################################################################
# Filename: user_model.py
# Purpose:  Define the User model for representing user data in the database.
# Author:   Benjamin Goh and Darren Seubert
#
# Description:
# This file contains the definition of the User class, which is used as a model
# to represent user data in the application's database. The class includes
# attributes corresponding to the user's properties, such as its ID and name.
#
# Usage (Optional):
# TBD
#
# Notes:
# The User class should be integrated with an ORM (Object-Relational Mapping)
# tool like SQLAlchemy to facilitate database interactions. Additional attributes
# and methods may be added to the class as needed to support the application's
# functionality.
#
###############################################################################


from app.database import db
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    """
    User class representing users in the database.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
    """

    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        """
        Return a string representation of the User object.
        """
        return (
            f"<User(user_id='{self.user_id}', name='{self.name}', email='{self.email}'>"
        )

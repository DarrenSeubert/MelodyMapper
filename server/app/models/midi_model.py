################################################################################
# Filename: midi_model.py
# Purpose:  Define the Midi model for representing MIDI file data in the database.
# Author:   Benjamin Goh and Darren Seubert
#
# Description:
# This file contains the definition of the Midi class, which is used as a model
# to represent MIDI file data in the application's database. The class includes
# attributes corresponding to the MIDI file's properties, such as its ID and name.
#
# Usage (Optional):
# TBD
#
# Notes:
# The Midi class should be integrated with an ORM (Object-Relational Mapping)
# tool like SQLAlchemy to facilitate database interactions. Additional attributes
# and methods may be added to the class as needed to support the application's
# functionality.
#
###############################################################################

from app.database import db
from sqlalchemy import Integer, String, LargeBinary, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class MIDI(db.Model):
    """
    MIDIs class representing MIDI data in the database.

    Attributes:
        midi_id (int): The unique identifier for the MIDI data.
        user_id (int): The unique reference identifier for User data.
        title (str): Title of the song.
        date (DateTime): The MIDI file generation date.
        midi_data (LargeBinary): The raw MIDI data.
    """

    __tablename__ = "midis"
    midi_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id"), nullable=False
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    midi_data: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    def __repr__(self):
        """
        Return a string representation of the MIDI object.
        """
        return f"<MIDI(midi_id={self.midi_id}, user_id={self.user_id}, title='{self.title}', date={self.date.isoformat()})>"

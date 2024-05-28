/*
# Filename: init.sql
# Purpose: Create and initialize the MelodyMapper database
# Author: Roshni Venkat
#
# Description:
# This file contains the script to create and initialize MelodyMapper database.
#
# Usage (Optional):
# [Instructions or examples demonstrating how to use the code in this file.
# Include any dependencies or prerequisites required for proper usage.]
#
# Notes:
# [Any additional notes, considerations, or important information
# about the file that may be relevant to developers or users.]
#
*/

CREATE DATABASE IF NOT EXISTS mp_database;
USE mp_database;

/*
Creates the Users table in the database
Attributes:
    user_id(integer): the user id
    name(string): the user name
    email(string): the user email
*/
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

/*
Creates the MIDIs table in the database
Attributes:
    midi_id(integer): the midi id
    user_id(integer): the user id
    title: the title of the MIDI file
    date: the date it was recorded
    midi_data (bytes): the midi data
*/
CREATE TABLE IF NOT EXISTS midis (
    midi_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    date DATETIME,
    midi_data LONGBLOB,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
import sys
import shutil
import os


# build a table mapping all non-printable characters to None
NOPRINT_TRANS_TABLE = {
    i: None for i in range(0, sys.maxunicode + 1) if not chr(i).isprintable()
}


def remove_non_printable_characters(filename):
    filename = filename.translate(NOPRINT_TRANS_TABLE)
    return filename


def remove_extra_characters_from_movie_name(movie_name):
    movie_name = movie_name.replace("(", " ").replace(")", " ").replace(".", " ").replace("_", " ")
    movie_name = movie_name.strip()
    return movie_name


def move(file_name, folder_name):
    cwd = os.getcwd()
    shutil.move(os.path.join(cwd, file_name), os.path.join(cwd, folder_name, file_name))

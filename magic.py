import re
import os
import utils


regex = r"(^.*)(19[1-9]{2}|20[0-9]{2})"


def do_magic():
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for file in files:
        try:
            matches = re.findall(regex, file)
            if len(matches) == 0:
                continue
            matches = matches[0]
            movie_name, movie_year = matches[0], matches[1]
            movie_name = utils.remove_non_printable_characters(movie_name)
            movie_name = utils.remove_extra_characters_from_movie_name(movie_name)

            folder_name = f"{movie_name} ({movie_year})"
            try:
                os.makedirs(folder_name)
                print(folder_name)
            except Exception:
                print(f"Folder {folder_name} already exists")
                pass
            utils.move(file, folder_name)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    do_magic()

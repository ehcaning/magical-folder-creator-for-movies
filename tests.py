import utils
import os
from pathlib import Path
import shutil
import magic


def test_remove_non_printable_characters():
    assert utils.remove_non_printable_characters("Good Movie Name") == "Good Movie Name"
    assert utils.remove_non_printable_characters("Bad.Movie.Name.\x00\x11") == "Bad.Movie.Name."


def test_remove_extra_characters_from_movie_name():
    assert utils.remove_extra_characters_from_movie_name("On.the.Waterfront.") == "On the Waterfront"
    assert utils.remove_extra_characters_from_movie_name("The.Old.Man.And.The.Sea.") == "The Old Man And The Sea"
    assert utils.remove_extra_characters_from_movie_name("La.vita.e.bella.[Life.Is.Beautiful].") == "La vita e bella [Life Is Beautiful]"


def test_everything():
    movie_names = [
        "Spiderman_Homecoming_2017_720p_MkvCage_(DibaMovie).mkv",
        "Spiderman.Homecoming.2017.Bluray.srt",
        "Soul.2020.720p.WEB-DL.x265.10Bit.mkv",
        "Soul.2020.720p.WEB-DL.x265.10Bit.srt",
        "Snowpiercer.2013.720p.DibaMoviez.mkv",
        "The.Prestige.2006..1080p.Farsi.Dubbed.mkv",
        "The.Prestige.2006..1080p.Farsi.Dubbed.srt",
        "The.Prestige.2006.1080p.720p.Bluray.fa.srt",
        "The.Prestige.2006.720p.BLAXUP.COM.mkv",
        "The.Prestige.2006.720p.BluRay.x264-ESiR.Per.srt",
        "The.Prestige.2006.720p.BluRay.x264-ESiR.srt",
        "The.Prestige.2006.720p.BluRay.x264.ESiR.srt",
        "The.Prestige.2006.720p.YIFY.srt",
        "The.Prestige.2006.HDRip.x264-SHAn.srt",
        "The.Prestige.2006.WWW.WORLDSUBTITLE.COM.rar",
    ]
    expected_folder_names = [
        'Snowpiercer (2013)',
        'Spiderman Homecoming (2017)',
        'Soul (2020)',
        'The Prestige (2006)',
    ]
    expected_all_files = [
        './Snowpiercer (2013)/Snowpiercer.2013.720p.DibaMoviez.mkv',
        './Soul (2020)/Soul.2020.720p.WEB-DL.x265.10Bit.srt',
        './Soul (2020)/Soul.2020.720p.WEB-DL.x265.10Bit.mkv',
        './Spiderman Homecoming (2017)/Spiderman_Homecoming_2017_720p_MkvCage_(DibaMovie).mkv',
        './Spiderman Homecoming (2017)/Spiderman.Homecoming.2017.Bluray.srt',
        './The Prestige (2006)/The.Prestige.2006.720p.BluRay.x264-ESiR.Per.srt',
        './The Prestige (2006)/The.Prestige.2006.WWW.WORLDSUBTITLE.COM.rar',
        './The Prestige (2006)/The.Prestige.2006.HDRip.x264-SHAn.srt',
        './The Prestige (2006)/The.Prestige.2006.720p.BluRay.x264-ESiR.srt',
        './The Prestige (2006)/The.Prestige.2006..1080p.Farsi.Dubbed.srt',
        './The Prestige (2006)/The.Prestige.2006.720p.BluRay.x264.ESiR.srt',
        './The Prestige (2006)/The.Prestige.2006..1080p.Farsi.Dubbed.mkv',
        './The Prestige (2006)/The.Prestige.2006.720p.YIFY.srt',
        './The Prestige (2006)/The.Prestige.2006.1080p.720p.Bluray.fa.srt',
        './The Prestige (2006)/The.Prestige.2006.720p.BLAXUP.COM.mkv'
    ]

    # create a folder for temporary test and cd into it
    try:
        os.mkdir("temp")
    except Exception:
        shutil.rmtree("temp")

    os.chdir("temp")

    # create a file for each movie and subtitle
    for file in movie_names:
        Path(file).touch()

    magic.do_magic()

    # assert folder names
    folders = [f for f in os.listdir(".") if os.path.isdir(f)]
    assert set(folders) == set(expected_folder_names)

    all_files = list()
    for (dirpath, dirnames, filenames) in os.walk("."):
        all_files += [os.path.join(dirpath, file) for file in filenames]
    assert set(all_files) == set(expected_all_files)

    # remove temp folder
    os.chdir("..")
    shutil.rmtree("temp")


if __name__ == "__main__":
    test_remove_non_printable_characters()
    test_remove_extra_characters_from_movie_name()
    test_everything()
    print("PASS")

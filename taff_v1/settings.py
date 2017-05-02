"""
 Settings File:
     here you can set the settings of the TAFF

"""

import os


class settingsTaff:
    # Taff information
    VERSION = "0055"

    """
    --------------------------
        User Settings
    --------------------------
    """
    # User Settings
    USERNAME = "Larry"

    # user Data folder
    if os.name == "nt":
        USER_DATA_FOLDER = "0_Documents\\"
        USER_DATA_FOLDER_TEMP = USER_DATA_FOLDER + "temp\\"
    else:
        USER_DATA_FOLDER = "0_Documents/"
        USER_DATA_FOLDER_TEMP = USER_DATA_FOLDER + "temp/"

    """
    --------------------------
        mcps_read Settings
    --------------------------
    """
    MCPS_READ_LOG = "no"  # or "no"
    if os.name == "nt":
        MCPS_READ_FOLDER = USER_DATA_FOLDER + "mcps_read_log\\"
    else:
        MCPS_READ_FOLDER = USER_DATA_FOLDER + "mcps_read_log/"

    """
    --------------------------
        Database Settings
    --------------------------
    """
    # Database name
    DATABASE_NAME = "test2_database.db"

    # --> dont change the following values

    # Database location
    DATABASE_DIR_WIN = "database\\"
    DATABASE_DIR_UNIX = "database/"
    # Automatic gen. DATABASE File
    DATABASE_FILE_WIN = DATABASE_DIR_WIN + DATABASE_NAME
    DATABASE_FILE_UNIX = DATABASE_DIR_UNIX + DATABASE_NAME

    """
    --------------------------
        Components Settings
    --------------------------
    """
    # Components folder
    #  different path between windows and unix
    COMPONENTS_FOLDER_WIN = "components\\"
    COMPONENTS_FOLDER_UNIX = "components/"

    """
    --------------------------
        plotCm  Settings
    --------------------------
    """
    if os.name == "nt":
        PLOT_CM_FOLDER = USER_DATA_FOLDER + "PLOT_CM\\"
    else:
        PLOT_CM_FOLDER = USER_DATA_FOLDER + "PLOT_CM/"

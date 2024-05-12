from models import RunMode, ApplicationSettings, DataReaderSettings

APPLICATION_SETTINGS = ApplicationSettings(
    # data: runs only the data gathering, cleaning, data insertion
    # test: runs the full simulation for a partial sample data
    # full: runs the full simulation on all the data
    run_mode=RunMode.data,
    # Sample size is used with conjunction with run-mode, 0 also means run through all data
    sample_size=30,
    # Database block for development purposes while you're tinkering with data separation so you don't keep messing up your local db to do it all over again
    database_block=True,
    limit_sample_size=True,
    # Mode settings TBD
)

DATAREADER_SETTINGS = DataReaderSettings(
    # 0 means infinite, this is for development purposes, will be set to application_settings.sample_size by default
    read_sample_size=(
        APPLICATION_SETTINGS.sample_size
        if APPLICATION_SETTINGS.limit_sample_size
        else 0
    )
)

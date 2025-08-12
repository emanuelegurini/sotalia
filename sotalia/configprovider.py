SOTALIA_DEFAUT_SESSION_VARIABLES = {
    # logical:  config_file, env_var, default_value, conversion_func
    'profile': (None, ['AWS_DEFAULT_PROFILE', 'AWS_PROFILE'], None, None),
    'region': ('region', 'AWS_DEFAULT_REGION', None, None),
    'data_path': ('data_path', 'AWS_DATA_PATH', None, None),
    'config_file': (None, 'AWS_CONFIG_FILE', '~/.aws/config', None),
    'credentials_file': (None,'AWS_SHARED_CREDENTIALS_FILE', '~/.aws/credentials', None)
}

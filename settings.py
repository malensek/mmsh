class Settings:
    def __init__(self):
        import os
        home = os.environ['HOME']
        self.config_dir = home + '/.config/mmsh'
        if not os.path.isfile(self.config_dir + '/config.json'):
            print('error')


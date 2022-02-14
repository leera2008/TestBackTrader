import os
import yaml


class ConfigLoader(object):
    def getConfig(self):
        #取当前这个文件的上一级目录
        rootDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        print(rootDir)

        configPath = os.path.join(rootDir, "config", "setup.yml")
        f = open(configPath, 'r', encoding='utf-8')
        config = yaml.safe_load(f.read())
        config['BASE_DIR'] = rootDir
        return config


if __name__ == '__main__':
    configLoader = ConfigLoader()
    config = configLoader.getConfig()
    print(type(config))
    print(config)

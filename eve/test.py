import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")
result = config.get("test","test")
print result

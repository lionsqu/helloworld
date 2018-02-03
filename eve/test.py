from config import ConfigFile


config = ConfigFile()

config.open("config.ini")
config.read()

result = config.get("demo", "demo")

config.write()

print result

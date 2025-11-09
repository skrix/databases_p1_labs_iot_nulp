import os
import yaml

from sqlalchemy import engine_from_config
from sqlalchemy.orm import declarative_base

db_config = os.path.join(os.getcwd(), "config", "db.yml")

with open(db_config, "r") as yaml_file:
    db_config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    engine = engine_from_config(db_config, prefix='sqlalchemy.')

Base = declarative_base()

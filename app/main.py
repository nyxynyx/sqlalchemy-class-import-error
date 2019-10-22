import sys
sys.path.append('..')

from lib.db import db_session
from models.foo.Animal import Animal

if __name__ == '__main__':
    print(Animal.query.all())
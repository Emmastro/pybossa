# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2015 Scifabric LTD.
#
# PYBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PYBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PYBOSSA. If not, see <http://www.gnu.org/licenses/>.
from pybossa.core import create_app

from cli import setup_alembic_config

def db_create(app):
    with app.app_context():
        from pybossa.core import db
        from pybossa.model.category import Category
    
        db.create_all()
        # then, load the Alembic configuration and generate the
        # version table, "stamping" it with the most recent rev:
        #setup_alembic_config()
        # finally, add a minimum set of categories: Volunteer Thinking, Volunteer Sensing, Published and Draft
        categories = []
        categories.append(Category(name="Thinking",
                                   short_name='thinking',
                                   description='Volunteer Thinking projects'))
        categories.append(Category(name="Volunteer Sensing",
                                   short_name='sensing',
                                   description='Volunteer Sensing projects'))
        db.session.add_all(categories)
        db.session.commit()

if __name__ == "__main__":  # pragma: no cover
    print("Running PyBossa...")
    
    app = create_app()
    try:
        db_create(app)
    except:
        print("dtb already exists")
    # logging.basicConfig(level=logging.NOTSET)
    app.run(host=app.config['HOST'], port=app.config['PORT'],
            debug=app.config.get('DEBUG', True))
else:
    app = create_app()

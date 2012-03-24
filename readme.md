Teaspoon3 - (TSN<>P)
-------------------

a template+suggestion on how to create a web app using Tornado, SqlAlchemy, testing it using Nose and documentation using Pycco
intended to give ya just the things you need (more likely to say, I needed), nothing more, WYSIWYG...
no 'magical' 'project' generation... just download and start using the template
it is @marxus85 teaspoon clone
ported Python3 (Python3.2.2 recommended)

HOW TO:

* install these packages: tornado, sqlalchemy, nose, pycco (virtualenv is always recommended)
* download your database driver (sqlite is not need driver, because it is already included)
* psycopg2 ported to Python3 is recommended
github:https://github.com/dvarrazzo/psycopg

    git clone https://github.com/dvarrazzo/psycopg
    cd psycopg/
    python setup.py install

* download and extract
* cd teaspoon
* type 'python .' - it will print out options available to you from the __\_\_main\_\_.py__ file
* set up the db connection string at __models/\_\_init\_\_.py__
    engine = create_engine('sqlite+pysqlite:///file.db')
* type 'python . create' - it will create the tables (it wont fill them with data)
* type 'python -c "import setup.auth"' - inorder to fill with basic User/Group/Permission data to your database
* type 'python . test' - will test the application. should pass.
* type 'python . serve' - will serve the application. open your browser at http://localhost:8888, for more configuration checkout __handlers/\_\_init\_\_.py__
* type 'python . stop' - it is not work. W.I.P


after all that. RTFC. (docs directory for your convenience) and start modifing the supplied code and apply it to your needs.

shinrito@gmail.com
@shinriyo -> @twitter

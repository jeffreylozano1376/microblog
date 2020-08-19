BASIC APP
1. Create the "app" package, that will host the application
    - In Python, '__init__.py' contained in a sub-directory, considers it a package
2. Routes.py module
    - view functions, which are basically routes for the diff. URLs that the application implements
    - 'app.decorator' on top of a view function serves as a mapping for client requests, so Flask n=knows what logic to execute
3. Set-up Environment Variables (.flaskenv)
    - FLASK_APP=microblog.py
    - FLASK_DEBUG=1
4. Initialize web server (127.0.0.1/localhost)
    - flask run

TEMPLATES
1. HTML files in the 'templates' directory - web pages rendered by the app
    - base.html - base template for other templates to inherit; to share a common UI (i.e. navigation bar)
    - inheriting templates - {% extends "base.html" %} statement, to establish the inheritance link

WEB FORMS
1. Flask-WTF extension
    - uses Python classes to represent web forms
    - 'Config' module ('Config' class) - configuration settings are defined as class variables
    - SECRET_KEY configuration variable, which is necessary for web forms to be protected from CSRF attacks; consists of 2 terms which is env variable or hardcoded string
    - 'forms.py' - define form classes
    - corresponding HTML template for the form
    - <form> element as container for the webform
    - View function mapped to the specific URL that creates the form

DATABASES
1. Flask-SQLAlchemy extension
    - Object Relational Mapper(ORM) - allows managing database using classes, objects, and methods
2. Flask-Migrate extension
    - database migration framework for SQLAlchemy
3. Config for SQLALCHEMY_DATABASE_URI
    - env variables or harcoded fallback value
4. Add instances for 'database' and ' migration engine' in the application
5. Define database models in 'models.py'
    - users table
    - posts table (user_id as foreign key - a user can have many posts)
6. Create the Migration Repository
    - flask db init - creates a new migrations directory
    - flask db migrate - generate migration scripts
    - flask db upgrade - apply changes to the database (if doesn't exist yet, creates a database)
    - add user:
        >>> from app import db
        >>> from app.models import User, Post
        >>> u = User(username='john', email='john@example.com')
        >>> db.session.add(u)
        >>> db.session.commit()
    - query users:
        >>> users = User.query.all()
        >>> users
    - add a blog post:
        >>> u = User.query.get(1)
        >>> p = Post(body='my first post!', author=u)
        >>> db.session.add(p)
        >>> db.session.commit()
    - delete users
        >>> users = User.query.all()
        >>> for u in users:
        ...     db.session.delete(u)
        >>> db.session.commit()
    - delete posts
        >>> posts = Post.query.all()
        >>> for p in posts:
        ...     db.session.delete(p)
        >>> db.session.commit()
User Logins
    - 'models.py' : Class User
    - hashing of user password (Werkzeug package)
    >>> from werkzeug.security import generate_password_hash
    >>> hash = generate_password_hash('foobar')
    >>> hash
    - hashing verification
    >>> from werkzeug.security import check_password_hash
    >>> check_password_hash(hash, 'foobar')
    >>> check_password_hash(hash, 'barfoo')
    - implement 2 new methods in the user model:
    >>> u = User(username='susan', email='susan@example.com')
    >>> u.set_password('mypassword')
    >>> u.check_password('anotherpassword')
    >>> u.check_password('mypassword')
    1. Flask-Login extension
        - add 'login' instance in application
        - add 'UserMixin' class for the implementationns
        - user loader function - uses unique identifier to navigate thru pages
        - def 'login' function
        - def 'logout' function
        - 'base.html' - expose the login link in the navbar
        - '@login_required' - limit a particular views to logged-in users 

FOLLOWERS/FOLLOWING
1. Define many-to-many relationship between 2 entities
    - specifically define a "self-referential relationship" (1st: users, 2nd: users)
    - since the case is, a particular user follows many other users, and a user has many followers
    - auxiliary table (followers table) - 2 foreign keys pointing to 'users table'
    - 'followed' attribute in Class User to link User instnces to other user instances











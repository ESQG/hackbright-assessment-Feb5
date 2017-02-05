"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# The returned value is an object of the BaseQuery class defined in the flask_sqlalchemy
# module.  That means it's a query from Python to the PostgreSQL database, specifically to
# the table referred to in the SQLAlchemy Brand class, which can be
# saved so it can be asked again.  It includes methods such as .one() or .all() which
# will run the query and return a Brand class, or a list of Brand classes, or None if
# nothing matches the query.  It also includes methods for refining the SQL query, such as
# .filter(*args).

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table is an abstract table, defined for the purpose of factoring
# many-to-many relationships through an intermadiary.  By abstract I mean that although it is a
# table just like any other, its only meaningful content is the correspondences between records
# of A and B. By factoring I mean in the sense of composing functions (in this case turning
# mappings that aren't functions into mappings that are, at least in one direction).

# In a pictorial graph sense, if two tables A and B are shown with records as nodes and edges
# representing the correspondences from records in A to records in B, then after refactoring
# through an association table AB, each edge becomes a record in AB, with one field corresponding
# to the vertex in A, one field corresponding to the other vertex in B, and usually, a third
# field to label each record of AB with an integer primary key.
# If we graph the results there are no edges directly connecting A to B.
# Also, the relationships between A, B, and AB are not only many-to-one relationships
# but actually surjective functions A-->AB and B-->AB: that is, each record in A or B maps via an
# associated field to a unique record in AB, and each record in AB corresponds to at least one
# record in A and at least one record in B.

# The purpose of an association table is that of data normalization, a principle holding that no
# many-to-many relationships should be stored as such, and all must be refactored through association
# tables (or so-called middle tables: like association tables but with meaningful content of their own).
# The reasoning is that after normalizing, the only fields repeated in the database are the associated
# fields between A and B.  Without this normalization, the many-to-many relationships of tables A and B
# would require that full records of A and B be repeated in order to show the correspondences:
# potentially a lot of redundant information would be stored, making records
# inconvenient to update and more vulnerable to errors.

# Since the purpose of AB is to capture each relationships between records of A and B, if A and B
# have primary keys it is natural to use both of these as "foreign keys" in AB.
# By using foreign keys, a SQL database will enforce the surjectivity of the functions A-->AB and B-->AB.

# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = "Brand.query.get('ram')"

# Get all models with the name "Corvette" and the brand_id "che."
q2 = "Model.query.filter_by(name='Corvette', brand_id='che').all()"

# Get all models that are older than 1960.
q3 = "Model.query.filter(Model.year < 1960).all()"

# Get all brands that were founded after 1920.
q4 = "Brand.query.filter(Brand.founded > 1920).all()"

# Get all models with names that begin with "Cor."
q5 = "Model.query.filter(Model.name.like('Cor%')).all()"

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = "Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()"

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = "Brand.query.filter(Brand.discontinued.isnot(None) | (Brand.founded < 1950)).all()"

# Get any model whose brand_id is not "for."
q8 = "Model.query.filter(Model.brand_id != 'for').all()"



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    pass


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    pass


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    pass


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    pass


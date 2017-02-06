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

# If we think of the records of A and the records of B as nodes of a graph, with edges
# representing the correspondences between them, then the association table AB is a
# (numbered) list of the edges.  That is, it has 3 columns: a primary key for usual 
# record-managing purposes (although one could define an association table without this
# column), a column representing records from table A (usually: a foreign key referencing
# A's primary key), and a column representing records from table B; so that each record in
# the association table labels a correspondence between some record of A and some record
# of B.

# The purpose of an association table is to prevent redundancy of records in the tables A
# and B. In tabular format, to associate a record of table A with more than one record of
# table B, we need to use multiple rows in table A, each one referring to a different
# record of table B; and vice versa. Even if we use (as one should) just one field in A
# as a foreign key referencing B's primary key, and vice versa, all other fields in A must
# be repeated or the data is inconsistent. Thus, A and B have to store redundant information
# which is inconvenient to update and more vulnerable to mistakes.  With the aid of an
# association table AB, the tables A and B do not need to reference each other; instead, AB
# uses its foreign keys to track all the correspondences. By construction, every record in
# AB corresponds to a unique record in A and a unique record in B; this allows the database
# to follow the principle of data normalization, which states that all relationships between
# tables should be one-to-many, many-to-one, or one-to-one.  The only redundant information
# is the foreign keys of AB, but PostgreSQL (and presumably other versions of SQL) can
# reduce the hazards of updating records by enforcing the foreign key relationship.

# A less abstract analogue to an association table is called a middle table: one that
# yields the same normalization benefits as the association table, but has meaningful
# content in addition to the correspondences.

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

    year_query = db.session.query(Model.name, Brand.name, Brand.headquarters).join(
                 Brand).filter(Model.year==year)

    for info in year_query.all():
        model_name, brand_name, brand_headquarters = info
        print "Brand: %s; Headquarters: %s; Model: %s" %(brand_name, brand_headquarters, model_name)


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    brands_query = db.session.query(Model.year, Brand.name, Model.name).join(Brand)

    for car_descriptors in brands_query.all():
        print "%i %s %s" % car_descriptors


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return Brand.query.filter(Brand.name.like("%"+mystr+"%")).all()   # SQLAlchemy escapes quotes, right?  S.O. says so 

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()

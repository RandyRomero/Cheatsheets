pip install alembic

alembic init alembic

add
sqlalchemy.url = postgresql://user:password@lhost:port/database_name
to alembic.ini file

add
from your_project.models import Base
target_metadata = Base.metadata
to env.py of alembic to be able to use --autogenerate


### How to make a new automatic migration? 

answer:

`alembic revision --autogenerate -m 'first commit'`


question id: abd8ed9b-c6b1-436a-8be0-f33fe978bbc0


### How to upgrade database to the latest revision?

answer:

`alembic upgrade head`

question id: be95b83b-98b6-4618-858c-31af3e9d3197


### How to dowgrade to the previous migration?

answer:

`alembic downgrade -1`

question id: 40c4d536-888f-4add-b9ec-4a13c5c0615f


### How to check what migrations have been applied so far?

answer:

`alembic history (--verbose)`

question id: cf60fcf2-8ae5-4a43-ba1c-941f387f8246
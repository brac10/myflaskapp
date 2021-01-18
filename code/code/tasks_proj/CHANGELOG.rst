Changelog
=========

------------------------------------------------------
Changes to tests:
~~~~~~~~~~~~~~~~~

- modify tests/conftest.py:
    - parametrize ``tasks_db_session`` to test both TinyDB and MongoDB.

Known Issues:
~~~~~~~~~~~~~

- Lots of tests fail.
    - possibly due to some problem with task_id with the MongoDB version

----------------------------------------------------

0.1.0 (ch3/b/tasks_proj/tests)
------------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- modify tests/conftest.py:
    - Create a session scope fixture ``tasks_db_session``
      that connects to db.
    - Have ``tasks_db`` fixture use ``tasks_db_session`` and 
      just clean out db between tests.

- add tests/func/test_add_variety2.py
    - demonstrate paramterized fixtures


- added tests/unit/test_Task.py 
    - a few tests to demonstrate running tests

- added tests/unit/test_Task_fail.py 
    - demonstrate test failure

- added tests/func/test_api_exceptions.py
    - testing for expected exceptions

- added tests/func/test_add.py
    - testing ``tasks.add()``
    - demonstrate user defined markers 

- added tests/func/test_unique_id_1.py
    - initial tests for ``tasks.unique_id()``.

- added tests/func/test_unique_id_2.py
    - demonstrate ``@pytest.mark.skip()``.

- added tests/func/test_unique_id_3.py : 
    - demonstrate ``@pytest.mark.skipif()``.

- added tests/func/test_unique_id_4.py
    - demonstrate ``@pytest.mark.xfail()``.

- added tests/func/test_add_variety.py
    - demonstrate ``@pytest.mark.parametrize`` on functions and classes.


Changes:
~~~~~~~~

- Initial version to test RangerPi.


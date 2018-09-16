.. title: A setup for a CI in Python projects
.. slug: a-setup-for-a-ci-in-python-projects
.. date: 2017-04-22 22:46:35 UTC+02:00
.. tags: clean-code, best-practices, development, mypy, python,draft
.. category: code, best-practices
.. link:
.. description:
.. type: text

Following up on the previous entry about automating some of the checks that
are done as part of the code review code review and `another good
reference on coontinuous integration for Python by Brett Cannon
<https://snarky.ca/how-to-use-your-project-travis-to-help-test-python-itself/>`_,
now is time of summarizing what makes a good continuous integration (CI) setup
for Python projects.

In my opinion, the build is not only the place where tests are run, but more
generally where the project policies are enforced. Having the tests pass is
just one of those policies, but there could be more.

Unit Tests and linting
^^^^^^^^^^^^^^^^^^^^^^



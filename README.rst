behave-profiles
===============

`behave-profiles` helps you write more concise feature definitions,
grouping together sets of steps in the so called `profiles`. This
profiles are gherkin files with a group of steps.


Usage
-----

1. Load the steps for your language
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From your `steps.py` file import the step definition for your language:

.. code-block:: python

   import behave_profiles.steps.en  # For English
   # import behave_profiles.steps.es  # For Spanish


2. Write a profile
~~~~~~~~~~~~~~~~~~

* Create a `profiles` directory inside your `features` directory.
* Create a textfiles inside with a name ending in `.profile`. For
  example `local_mysql_server.profile`.
* Add steps to the profile file to set your environment.

.. code-block:: gherkin

   Given I have a working MySQL database server
     And I create the database schema in the MySQL server
     And I accept TCP connections to the port 3306 from 127.0.0.1


3. Reuse your profile as many times as you want
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Now you can use the `behave-profiles` steps to call your profiles:

.. code-block:: gherkin

   Feature: My new feature

   Background:
       Given the profile "local_mysql_server"

   Scenario: My first
       ...
       ...


* If you need to use multiple profiles in your feature file, you can use
  the step "the following profiles":

.. code-block:: gherkin

   Feature: My new feature 2

   Background:
       Given the following profiles
         | profiles                   |
         | local_mysql_server         |
         | running_application_server |
         | website_admin_user         |

   Scenario: My first
       ...
       ...


4. Grouping profiles together
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you end having to load multiple groups of profiles all the time you
can make a group of profiles making a profile of... well profiles.

Given the last example, you can make a new profile that loads those
three profiles. For example, you can name this new profile
"fully_working_application.profile":

.. code-block:: gherkin

   Given the following profiles
     | profiles                   |
     | local_mysql_server         |
     | running_application_server |
     | website_admin_user         |

And you can use it as any other profile:

.. code-block:: gherkin

   Given the profile "fully_woking_application"

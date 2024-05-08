.. Sphinx Demo Program documentation master file, created by
   sphinx-quickstart on Wed May  1 09:50:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to the documentation for Sphinx Demo Program!
============================================================


.. image:: /images/Main.png 
   :scale: 50%
   

------


The purpose of this program is to demonstrate how to use Python docstrings for automatic documentation from your source code.

This program is basically a GUI skeleton that does nothing.  However, it does provide an easy way to show the process.

 .. GREG!!! Make sure to set the github link once it's set up!
 
 This program was created for my How-To Python article in `Full Circle Magazine <https://fullcirclemagazine.org/>`_ # 205 (May 2024) .  
 

 The source code and all relevant files are available on my github repository at `<https://github.com/gregwa1953/FCM-205>`_
   

A bit of History
--------------------


This month's article was inspired by one of the PAGE users on the PAGE Discord forum and someone whom I consider a good friend, Professor Roberto Machorro Mejía, who started using PAGE last school year.  He teaches at **UNAM**, a public university, the largest in Mexico.  He was using PAGE to create a GUI for a project he and his students were working on.  Long story short, he has been reading Full Circle Magazine for a while now and he sent me a note that he really enjoyed my article on Sphinx in last month's issue.  He was wondering, however, if **Sphinx** worked directly on a source file.  So, I decided to write about how to make this happen.






Before you get started
----------------------------

Once you get the **Sphinx** instance set up for your program (see my How-To Python article in last month's issue (FCM # 204), you will need to edit the config.py file to include a few things.  

.. code:: python
   
   # If extensions (or modules to document with autodoc) are in another directory,
   # add these directories to sys.path here.

   import pathlib
   import sys

   sys.path.append('/home/greg/Desktop/pagetests/Page8.1f/SphinxDemo1')
   print(f"{sys.path=}")

   extensions = [
      'sphinx.ext.duration',
      'sphinx.ext.doctest',
      'sphinx.ext.autodoc',
      'sphinx.ext.autosummary']

.. tip::
   Notice the *sys.path.append()* , which adds the folder for my source file.  In this case the file in question is **sphinxDemo1_support.py** .  You will need to change this line to match your source code path.

I am going to only be talking about documenting the **support.py** module.  The **.tcl** file doesn't support docstrings and it would be regenerated from scratch every time you make any changes to the GUI.  The same goes for the **GUI.py** file.  



Doing it manually
----------------------------

Of course you can do the documentation of your functions and methods manually.  I'll create a "dummy" entry for a fictitious **Sphinx** document.

------

One of the best things about the program is for the user to have the ability to change themes at any time to any theme in the theme folder.  Of course, these are all .tcl themes.  Use the load_tcl_themes function to generate a list of all of the themes, then load this into a TCombobox values property.  Then bind the virtual **<<ComboboxSelected>>** event to the TCombobox providing a callback function whenever the user selects something from the TCombobox list.  Here is the ``sphinxDemo1_support.on_ComboSelect()`` function

.. py:function:: sphinxDemo1_support.on_ComboSelect(e)

   :param e: The virtual event ("<<ComboboxSelected>>")
   :type e: event
   :return: None
   
   
Here is the code that will actually switch the theme to the user selection...


.. code:: python
  
   def on_ComboSelect(e):
       print(e)
       sty = ttk.Style()
       selected = _w49.comboThemes.get()
       print(f"Combobox Select: {selected}")
       sty.theme_use(selected)


-----


And that works fine.  However, you have to do this for every function and if any of the functions change you have to go into your **Sphinx** .rst file and update it.  This can really take a toll on you and your team.  Why not just add docstrings into the code and let **Sphinx** do it for you?


Doing it automatically
------------------------------

In your source file, create `docstrings <https://peps.python.org/pep-0257/#abstract>`_ for each of the functions (or methods) that you want to autodocument.  Example...



Here's information about the ``sphinxDemo1_support.load_tcl_themes()`` function:

.. autofunction:: sphinxDemo1_support.load_tcl_themes



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

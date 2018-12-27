============
Installation
============

You can see the requirements in the `requirements.txt` file. Some notable
dependencies include:

- requests==2.21.0
- numpy==1.15.4
- pandas==0.23.4

You can install the API client either via `pip` or manually through the
`setup.py` file. Using `pip`, simply run the following command:

.. code-block:: shell 

   pip install git+https://github.com/thinkingmachines/linksight-api-client.git

On the other hand, you can also clone this repository then run `install`:


.. code-block:: shell

   git clone git@github.com:thinkingmachines/linksight-api-client.git 
   cd linksight-api-client
   python setup.py install

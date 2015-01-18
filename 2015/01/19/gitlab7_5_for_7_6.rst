Redhat系(CentOS/Scientific Linux等)でGitlab7.5から7.6に上げる際に必要なlibkrb5-devについて
===========================================================================================

7.5から7.6に上げる際に必要なlibkrb5-devだが、Redhat系(CentOS/Scientific Linux)ではkrb5-develという名前になっている。

.. code-block:: bash

 # krb5-devel
 yum install krb5-devel


.. author:: default
.. categories:: Gitlab
.. tags:: Gitlab
.. comments::

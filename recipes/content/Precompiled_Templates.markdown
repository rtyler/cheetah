Precompiled Templates
=====================

Why bother?
-----------
Since Cheetah supports two basic modes: dynamic and precompiled templates, you have 
a lot of options when it comes to utilizing Cheetah, particularly in web environments.

There is added speed to be gained by using pre-compiled templates, especially when
using mod_python with Apache. Precompiling your templates means Apache/mod_python
can load your template's generated module into memory and then execution is only
limited by the speed of the Python being executed, and not the Cheetah compiler.



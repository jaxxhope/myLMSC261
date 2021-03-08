Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
WARNING: The system preference "Prefer tabs when opening documents" is set to
"Always". This will cause various problems with IDLE. For the best experience,
change this setting when running IDLE (via System Preferences -> Dock).
>>> for i in range(0, n):
  for j in range(0, i+1):
    print("#",end="")
  print()

  
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    for i in range(0, n):
NameError: name 'n' is not defined
>>> n = 8
>>> for i in range(0, n):
  for j in range(0, i+1):
    print("#",end="")
  print()

  
#
##
###
####
#####
######
#######
########
>>> 
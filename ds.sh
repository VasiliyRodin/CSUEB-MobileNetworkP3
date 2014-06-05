I used these shell commands to load up each program. Each command would be it's own shell file to execute.(I just want to save paper and not print each one separately)

ds.sh:

python DataSource.py geometry.sci.csueastbay.edu 6001
pause

ha.sh:

python HomeAgent.py 6001
pause

fa1.sh:
python ForeignAgent.py 6002 6012 algebra.sci.csueastbay.edu 6004
pause

fa2.sh:

python ForeignAgent.py 6003 6013 algebra.sci.csueastbay.edu 6004
pause

mn.sh:

python MobileNode.py 6004 geometry.sci.csueastbay.edu 6001 calculus.sci.csueastbay.edu 6002 6012 arithmetic.sci.csueastbay.edu 6003 6013
pause

Locations of each proccess:

DS= trig.sci.csueastbay.edu
HA= geometry.sci.csueastbay.edu
FA1= calculus.sci.csueastbay.edu
FA2= arithmetic.sci.csueastbay.edu
MN= algebra.sci.csueastbay.edu
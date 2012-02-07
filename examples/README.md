# Proteomics library usage examples

This folder contains some example scripts showing how to use the
'proteomics' library. The code files are commented with detailed
information as to what each line is doing.

## mascot_group_file.py

The code contained herein, demonstrates how to load and use the class
file loader to load the U{Mascot <http://www.matrixscience.com/} group
file. As of Mascot version 2.2, the group file was written in XML.

The Proteomics Mascot module uses 'xml.dom.minidom' to parse the XML
file. It collects the group ID, name and the ID's of the users that
belong to that group. For each group, this information is stored in
the Group structure (also part of the 'proteomics.mascot' module).

## mascot_user_file.py

The code contained herein, demonstrates how to load and use the class
file loader to load the U{Mascot <http://www.matrixscience.com/} user
file. As of Mascot version 2.2, the group file was written in XML.

The Proteomics Mascot module uses 'xml.dom.minidom' to parse the XML
file. It collects the user ID, username, full name and e-mail of each
user, stored in a User structure (also part of the 'proteomics.mascot'
module).

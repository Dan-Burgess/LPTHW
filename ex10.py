tabby_cat     = "\tI'm tabbed in."
persian_cat   = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

out_cat = 'Meow!'

print 'To get out, the cat said, %r' % out_cat
print 'To get out, the cat said, "%s"' % out_cat

h_line = "-" * 80
v_line = "|"

cont_line = ("%s\t\t" % v_line) * 5 + ("%s" % v_line)

print h_line
print cont_line
print h_line
print cont_line
print h_line
print cont_line
print h_line
print cont_line
print h_line


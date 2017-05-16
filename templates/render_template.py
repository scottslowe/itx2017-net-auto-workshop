#!/usr/bin/env python
''' Render a template '''

from jinja2 import Template

template = Template("interface {{ intf }}\n   description Testing\n!")

for x in [1, 2]:
    print template.render(intf="Ethernet{}".format(x))

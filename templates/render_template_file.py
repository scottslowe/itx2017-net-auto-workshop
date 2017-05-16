#!/usr/bin/env python
''' Render a template '''

import jinja2

templateLoader = jinja2.FileSystemLoader( searchpath="./templates")
templateEnv = jinja2.Environment( loader=templateLoader )
TEMPLATE_FILE = "arista5.twb-tech.com-basic.j2"
template = templateEnv.get_template( TEMPLATE_FILE )


with open('render_output.cfg', 'w') as f:
    for x in [1, 2]:
        config =  template.render(port_name="Ethernet{}".format(x),
                                  description="Configured by Python")
        print config

        f.write(config + "\n")

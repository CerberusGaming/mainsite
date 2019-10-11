from dominate import tags
from flask_nav.renderers import Renderer


class AppRenderer(Renderer):
    def visit_Navbar(self, node):
        nav = tags.nav(cls="navbar navbar-expand-lg navbar-dark bg-primary")
        with nav:
            tags.span(node.title, cls="navbar-brand")
            with tags.div(id='navbarColor01', cls="collapse navbar-collapse"):
                with tags.ul(cls='navbar-nav mr-auto'):
                    for item in node.items:
                        tags.li(self.visit(item))
        return nav

    def visit_View(self, node):
        active = ' active' if node.active else ''
        link = tags.li(cls="nav-item")
        with link:
            tags.a(node.text, cls="nav-link" + active, href=node.get_url())
        return link

    def visit_Subgroup(self, node):
        link = tags.li(cls="nav-item dropdown")
        with link:
            a = tags.a(node.title, cls="nav-link dropdown-toggle", href=".", id="dropdown{}".format(node.title))
            a.attributes["data-toggle"] = "dropdown"

            div = tags.div(cls="dropdown-menu")
            div.attributes["aria-labelledby"] = "dropdown{}".format(node.title)
            with div:
                for item in node.items:
                    tags.a(item.text, cls="dropdown-item", href=item.get_url())
        return link

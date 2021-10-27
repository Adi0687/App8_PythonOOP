import justpy as jp


# Should we use Inheritance or Composition
# is Default Layout a QLayout - Inheritance
# has DefaultLayout a QLayout - Composition
# We choose inheritance, because it is a QLayout!
class DefaultLayout(jp.QLayout):

    def __init__(self, view="hHh lpR fFf", **kwargs):
        super().__init__(view=view, **kwargs)

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left", bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qList = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qList, text="Home", href="/", classes=a_classes)
        jp.Br(a=qList)
        jp.A(a=qList, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qList)
        jp.A(a=qList, text="About", href="/about", classes=a_classes)
        jp.Br(a=qList)
        # The init for this class is an instance method and not a class method like the previous one!
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True

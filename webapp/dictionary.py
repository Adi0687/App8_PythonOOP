import justpy as jp
import definition


class Dictionary:
    path = '/dictionary'
    # the classmethod passes the class itself and not an instance of the class
    # this is done so that we can reference the class later, if not justPy passes
    # a request class object for routing
    @classmethod
    def serve(cls, req):
        # QuassarPage is a class used for pages  visuals
        # Responsible for what the user sees, HTML and CSS
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English Dictionary!", classes="text-4xl m-2")
        jp.Div(a=div, text="Get your Definition Instantly!", classes="text-lg m-2")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        input_box = jp.Input(a=input_div, placeholder="Type your word here...", outputdiv=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white "
                                     "focus:outline-none focus:border-purple-500 "
                                     "py-2 px-4")
        input_box.on('input', cls.get_definition)

        # jp.Button(a=input_div, text="Get Definition", classes="border-2 tet-gray-500", click=cls.get_definition,
        #          outputdiv=output_div, inputbox=input_box)

        return wp

    # A static method is a method inside a class that behaves like a function
    # it dosent expect an instance of a class-(like a normal Method)
    # or the class itself -(like a classmethod). It is in the class for organisation
    # issues. It does do something in the class but it also independent!
    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)

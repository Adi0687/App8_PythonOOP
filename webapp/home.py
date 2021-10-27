import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        # QuassarPage is a class used for pages visuals
        # Responsible for what the user sees, HTML and CSS
        # Should we use Inheritance or Composition
        # is wp a QuasarPage - Inheritance
        # has wp a QuasarPage - Composition
        # We choose composition, because wp has a QuasarPage!
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
        dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
        dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
                    """, classes="text-lg")

        return wp



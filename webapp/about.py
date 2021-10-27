import justpy as jp
from webapp import layout
from webapp import page

class About(page.Page):
    path = '/about'

    def serve(self):
        # QuassarPage is a class used for pages with visuals
        # Responsible for what the user sees, HTML and CSS
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
        dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
        dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
                    """, classes="text-lg")

        return wp




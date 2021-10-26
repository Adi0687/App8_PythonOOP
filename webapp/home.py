import justpy as jp


class Home:
    path = '/'

    def serve(self):
        # QuassarPage is a class used for pages with visuals
        # Responsible for what the user sees, HTML and CSS
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
        dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
        dgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfhdgldfsakhjksjklsdfjklhljgksdjklfhksdjklfh
                    """, classes="text-lg")

        return wp



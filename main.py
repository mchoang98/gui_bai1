from guizero import App, Text, Picture

app = App(title= "Hello World",width=400, height=700)

title = Text(app, text="Make AI helpful for everyone", font="Arial", size=20)

text1 = Text(app, font="Arial", size=15, text="""Donec magna orci, 
            molestie a enim a, dapibus tincidunt nulla.
            Mauris nunc ligula, tincidunt sit amet efficitur nec,
            vulputate quis justo. 
            Donec feugiat neque arcu, sit amet placerat ligula dapibus congue.""")

picture = Picture(app, image="cat.jpg", width=400, height=300)

text2 = Text(app, align="left", font="Arial", text="""Donec magna orci, molestie a enim a, dapibus tincidunt nulla.\n Mauris nunc ligula, tincidunt sit amet efficitur nec, vulputate quis justo. Aenean vel dignissim diam. Vestibulum id purus sit amet turpis gravida iaculis et quis massa. Donec feugiat neque arcu, sit amet placerat ligula dapibus congue.""")
text2.resize(200,300)
# text3 = Text(app, align="left", font="Arial", text="""Donec magna orci, 
#              molestie a enim a, dapibus tincidunt nulla. Mauris nunc ligu
#              la, tincidunt sit amet efficitur nec, vulputate quis justo. In b
#              ibendum velit id augue luctus egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed vulputate imperdiet 
#              purus. Maecenas pulvinar mauris vel elit rhoncus scelerisque. Nunc id enim nec elit gravida pretium eget sed nibh. In ac mattis odio, ac tempus sapien. Aenean vel dignissim diam. Vestibulum id purus sit amet turpis gravida iaculi
#              s et quis massa. Donec feugiat neque arcu, sit amet placerat ligula dapibus congue.""")

app.display()
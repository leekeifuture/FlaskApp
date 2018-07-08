# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import view
from app import db
from app import app
from posts.blueprint import posts


app.register_blueprint(posts, url_prefix='/blog')


if __name__ == '__main__':
    app.run()

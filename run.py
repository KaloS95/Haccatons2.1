#!flask/bin/python
# -*- coding: utf-8 -*- 

from app import app
app.run(
        host=app.config.get("HOST", "localhost"),
        port=app.config.get("PORT", "5000"),
        debug=True
        )

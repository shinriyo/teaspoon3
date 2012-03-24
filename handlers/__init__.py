# -*- coding: utf-8 -*-
"""
this sets up the tornado application  and handlers.
for more information about tornado check out <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>
"""

from tornado.ioloop import IOLoop
from tornado.web import Application

# import your handlers and set the application routes and configuration
from handlers.root import RootController
      
application = Application([
        # the RootController also serve as a StaticFileHandler. 'path' is mandatory, 'default_filename' is optional
        (r'/(.*)', RootController, {'path': 'public', 'default_filename': 'index.html'})
    ],
    # just bullshit string that will be used as a ... cookie secert
    cookie_secret='change_me_to_a_long_and_secrect_string_that_no_one_can_guess_asdlkasjdsakldjsalkdjsakldjskaldjlaskjdlkajdlkasjdklasjdopizxcmwerweiunh',
    template_path='templates',
    # request that does not pass @authorized will be redirected here
    forbidden_url='/forbidden',
    # requests that does not pass @authenticated  will be redirected here
    login_url='/login',
    # integer, in minutes, for how long until the session expires
    session_expire=20,
    # debug mode uses torando.autoreload module to reload the app on modules/templates
    # change and print out errors as response. delete or set to False for production
    debug=True
)

# the port. doh
#application.listen(8888)

# calling this will start the IOLoop. open your browser and enjoy.
#__serve__ = lambda: IOLoop.instance().start()
__serve__ = lambda: start()

#TODO
#__stop__ = lambda: IOLoop.instance().close(True)
__stop__ = lambda: IOLoop.instance().stop()

def start():
    application.listen(8888)
    IOLoop.instance().start()

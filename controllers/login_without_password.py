
from odoo import http
from odoo.http import Controller, request
import logging

class LoginController(Controller):

    @http.route(['/web/redirect'], type='json', auth='none', website=True,
                csrf=False, csrf_token=None)
    def login_without_password(self):
        username="admin"
        database="TEST"
        request.session.authenticate_without_passwd(database, username)
        return request.redirect('/')


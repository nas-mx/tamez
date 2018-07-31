# -*- coding: utf-8 -*-
from odoo import http

# class FormatoCotizacionAtamez(http.Controller):
#     @http.route('/formato_cotizacion_atamez/formato_cotizacion_atamez/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formato_cotizacion_atamez/formato_cotizacion_atamez/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formato_cotizacion_atamez.listing', {
#             'root': '/formato_cotizacion_atamez/formato_cotizacion_atamez',
#             'objects': http.request.env['formato_cotizacion_atamez.formato_cotizacion_atamez'].search([]),
#         })

#     @http.route('/formato_cotizacion_atamez/formato_cotizacion_atamez/objects/<model("formato_cotizacion_atamez.formato_cotizacion_atamez"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formato_cotizacion_atamez.object', {
#             'object': obj
#         })
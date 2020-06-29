# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    partner_ids = fields.Many2many(
        comodel_name='res.partner',
    )

    partner_name = fields.Char(
        compute='compute_partner_name',
    )

    @api.one
    @api.depends('partner_ids', 'partner_name')
    def compute_partner_name(self):
        self.partner_name = 'Asistentes: '
        total_partner = 1
        separator = ', '
        for partner in self.partner_ids:
            if total_partner == len(self.partner_ids):
                separator = ''
            self.partner_name += partner.name + separator
            total_partner += 1

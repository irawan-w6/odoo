# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class CompanySettings(models.Model):
    _name = 'company.settings'
    _description = 'Company Settings'

    name = fields.Char('Name', default='New')
    company_id = fields.Many2one('res.company', 'Company', required=True)
    active = fields.Boolean('Active', default=True)

    _sql_constraints = [('not_duplicate_company_setting', 'unique (company_id)',
                         'Duplicates company are not allowed!')]

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['res.company'].browse(vals['company_id']).name
        return super(CompanySettings, self).create(vals)

    def write(self, vals):
        if 'company_id' in vals:
            vals['name'] = self.env['res.company'].browse(vals['company_id']).name
        return super(CompanySettings, self).write(vals)

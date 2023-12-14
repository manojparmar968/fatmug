from datetime import timedelta, datetime, date

from odoo import api, fields, models, _

class VendorForecast(models.Model):
    _name = 'vendor.forecast'
    _inherit = ['mail.thread']
    _description = 'vendor forecast'

    name = fields.Char("Vendor Forecast Refrence", tracking=True)
    product_id = fields.Many2one(
        'product.product',
        string='Product', tracking=True, required=True
    )
    expected_quantity = fields.Integer('Expected Quantity', tracking=True)
    forecast_date = fields.Date('Forecast Date', tracking=True, default=lambda self: fields.Date.today())#fields.Datetime.now()),fields.Date.context_today(self)

    # Add access rights for vendors
    @api.model
    def _init_access(self):
        # Make the model read-only for vendors
        group_vendor_id = self.env.ref('base.group_portal')
        if group_vendor_id:
            group_vendor_id.write({
                'implied_ids': [(4, self.env.ref('vendor_self_service_portal.group_vendor_forecast_read').id)]
            })

    #=== CRUD METHODS ===#
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('vendor.forecast') or ""

        return super(VendorForecast, self).create(vals)
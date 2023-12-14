from odoo import api, fields, models, _

class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _inherit = ['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'vendor adjustment request'

    name = fields.Char(tracking=True)
    order_id = fields.Many2one("sale.order", string="Sales Order", tracking=True, required=True)
    adjustment_detail = fields.Text('Adjustment Detail', tracking=True)
    comment = fields.Text('comment', tracking=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.id)
    partner_id = fields.Many2one('res.partner', string="Partner")
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)

    #=== CRUD METHODS ===#

    @api.model
    def create(self, vals_list):
        vals_list['name'] = self.env['ir.sequence'].next_by_code('vendor.adjustment.request') or ""

        return super().create(vals_list)
    
    #=== ACTION METHODS ===#
    def action_automated_email_send(self):
        """ where vendors can submit adjustment requests for existing
            orders, Automated email send to procurement team.
        """
        self.ensure_one()
        mail_obj = self.env['mail.mail']
        mail_template = self.env.ref('vendor_self_service_portal.email_template_vendor_adjustment_request')
        mail_template.send_mail(self.id, force_send=True)
        lang = self.env.context.get('lang')
        # for rec in self:
        #     vals = {
        #         'model': 'vendor.adjustment.request',
        #         'author_id': self.env.user.partner_id.id,#self.env.user.partner_id.name
        #         # 'auto_delete': True,
        #         # 'body_html': body,
        #         'subject': self.env.company.name + ", Procurement Team",
        #         'email_from': self.env.user.email_formatted,
        #         # 'email_to': user.email_formatted,
        #         # 'reply_to':,
        #         # 'references': ,
        #         'recipient_ids': [rec.id],
        #         'res_id': rec.id,
        #         'record_name': rec.name,
        #         # 'attachment_ids':,
        #     }
        #     print("\n\nvals: ",vals)
        #     mail_send_id = mail_obj.create(vals)
        #     mail_obj.send(mail_send_id)
        # values = self._generate_template()
        """
        Send mail while open a form view with all of its data and then click on send button mail will we send.
        """
        ctx = {
            'default_model': 'vendor.adjustment.request',
            'default_res_ids': self.ids,
            # 'default_template_id': mail_template.id if mail_template else None,
            'default_composition_mode': 'comment',
            'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
            'force_email': True,
            'model_description': self.with_context(lang=lang)
        }
        # 
        # return {
        #     'type': 'ir.actions.act_window',
        #     'view_mode': 'form',
        #     'res_model': 'mail.compose.message',
        #     'views': [(False, 'form')],
        #     'view_id': False,
        #     'target': 'new',
        #     'context': ctx,
        # }
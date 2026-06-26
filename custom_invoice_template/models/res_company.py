from odoo import _, fields, models
from odoo.exceptions import UserError


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _action_preview_invoice_template(self):
        """Open the professional invoice report on a sample invoice.

        Picks the most recent customer invoice of the current company so the
        user can preview the effect of the branding settings.
        """
        company = self.env.company
        sample = self.env['account.move'].search([
            ('company_id', '=', company.id),
            ('move_type', 'in', ('out_invoice', 'out_refund')),
        ], order='invoice_date desc, id desc', limit=1)
        if not sample:
            raise UserError(_(
                'No customer invoice was found for company "%s". '
                'Create a customer invoice first to preview the template.'
            ) % company.name)
        return self.env.ref(
            'custom_invoice_template.action_report_custom_invoice'
        ).report_action(sample)

    # --- Branding ---------------------------------------------------------
    invoice_header_color = fields.Char(
        string='Header Color',
        default='#1a1a2e',
        help='Primary color used for the header / footer band of the invoice.',
    )
    invoice_secondary_color = fields.Char(
        string='Invoice Secondary Color',
        default='#16213e',
        help='Color used for the items table header row.',
    )
    invoice_accent_color = fields.Char(
        string='Accent Color',
        default='#0f3460',
        help='Accent color used for dividers, totals and highlights.',
    )
    invoice_tagline = fields.Char(
        string='Invoice Tagline',
        help='Short tagline shown under the company name in the header.',
    )
    invoice_logo_width = fields.Integer(
        string='Logo Width (px)',
        default=120,
        help='Width of the company logo in the invoice header, in pixels.',
    )
    invoice_footer_text = fields.Text(
        string='Invoice Footer Text',
        help='Free text centered in the footer band of the invoice.',
    )

    # --- Bank details -----------------------------------------------------
    invoice_bank_name = fields.Char(string='Bank Name')
    invoice_bank_account = fields.Char(string='Bank Account Number')
    invoice_bank_iban = fields.Char(string='Bank IBAN')
    invoice_bank_swift = fields.Char(string='Bank SWIFT / BIC')

    # --- Layout options ---------------------------------------------------
    invoice_show_qr = fields.Boolean(
        string='Show QR Code',
        default=True,
        help='Display a QR code (scan to pay / view online) on the invoice.',
    )
    invoice_show_stamp_area = fields.Boolean(
        string='Show Stamp & Signature Area',
        default=True,
        help='Display the authorized signature and company stamp boxes.',
    )
    invoice_show_bank_details = fields.Boolean(
        string='Show Bank Details',
        default=True,
        help='Display the bank details box on the invoice.',
    )

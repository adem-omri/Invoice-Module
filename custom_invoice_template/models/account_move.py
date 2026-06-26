import base64
import logging
from urllib.parse import urlencode

from odoo import fields, models

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_note_custom = fields.Text(
        string='Custom Invoice Note',
        help='Free note printed on the professional invoice template.',
    )
    invoice_template_style = fields.Selection(
        selection=[
            ('modern', 'Modern'),
            ('classic', 'Classic'),
            ('minimal', 'Minimal'),
        ],
        string='Invoice Template Style',
        default='modern',
        help='Visual style applied to the professional invoice PDF.',
    )

    # ------------------------------------------------------------------
    # Helpers used by the QWeb report
    # ------------------------------------------------------------------
    def is_credit_note(self):
        """Return True when the move should be rendered as a credit note."""
        self.ensure_one()
        return self.move_type in ('out_refund', 'in_refund')

    def get_document_title(self):
        """Header title: INVOICE / CREDIT NOTE / DRAFT ..."""
        self.ensure_one()
        if self.move_type in ('out_refund', 'in_refund'):
            return 'CREDIT NOTE'
        if self.move_type in ('in_invoice',):
            return 'VENDOR BILL'
        return 'INVOICE'

    def get_status_label(self):
        """Return a (label, css_class) tuple for the status badge."""
        self.ensure_one()
        if self.payment_state in ('paid', 'in_payment', 'reversed'):
            return 'PAID', 'cit-badge-paid'
        if self.state == 'posted':
            return 'POSTED', 'cit-badge-posted'
        if self.state == 'cancel':
            return 'CANCELLED', 'cit-badge-cancel'
        return 'DRAFT', 'cit-badge-draft'

    def get_amount_in_words(self):
        """Return the invoice total written out in words (English)."""
        self.ensure_one()
        currency = self.currency_id or self.company_id.currency_id
        amount_text = currency.amount_to_text(self.amount_total)
        return amount_text

    def get_header_accent_color(self):
        """Credit notes use a red accent, invoices use the company accent."""
        self.ensure_one()
        company = self.company_id
        if self.is_credit_note():
            return '#b00020'
        return company.invoice_accent_color or '#0f3460'

    def _get_invoice_online_url(self):
        """Best-effort public URL for the invoice, used for the QR code."""
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param(
            'web.base.url', default='')
        try:
            access_token = self._portal_ensure_token()
        except Exception:  # pragma: no cover - portal mixin always present
            access_token = False
        params = {'access_token': access_token} if access_token else {}
        query = ('?' + urlencode(params)) if params else ''
        return '%s/my/invoices/%s%s' % (base_url, self.id, query)

    def get_qr_code_base64(self):
        """Generate a base64 PNG QR code pointing to the online invoice.

        Returns an empty string when generation is not possible so the
        template can simply skip the QR block.
        """
        self.ensure_one()
        value = self._get_invoice_online_url()
        if not value:
            return ''
        try:
            barcode = self.env['ir.actions.report'].barcode(
                'QR', value, width=240, height=240, humanreadable=0)
            return base64.b64encode(barcode).decode('ascii')
        except Exception as exc:  # pragma: no cover - depends on qrcode lib
            _logger.warning('Could not generate invoice QR code: %s', exc)
            return ''

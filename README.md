# Custom Invoice Template — Odoo 16

A professional, fully branded **PDF invoice & credit note** template for Odoo 16.
It replaces Odoo's plain default invoice print with a polished document driven by a
few company settings — colours, logo, bank details, QR code, signature/stamp areas,
amount in words, tax breakdown and discount support.

Works for **Customer Invoices** and **Credit Notes** (credit notes are auto-detected
and styled with a red accent and a "CREDIT NOTE" title).

## Highlights

- Branded header / footer bands driven by company colours
- Configurable bank details, QR code, and stamp & signature areas
- Amount in words, per-tax breakdown, automatic discount column
- Modern / Classic / Minimal per-invoice styles
- Dedicated company configuration tab (Branding, Bank Details, Layout)
- A "Print Professional Invoice" action on the invoice Print menu

## Installation

1. Copy the [`custom_invoice_template`](custom_invoice_template) folder into your
   Odoo `addons` directory.
2. Update the apps list and install **Custom Invoice Template**
   (depends on `account` and `web`).
3. Set your branding under **Accounting → Configuration → Invoice Template**.
4. Open any invoice or credit note and choose **Print → Professional Invoice**.

See [`custom_invoice_template/README.md`](custom_invoice_template/README.md) for the
full, plain-language guide (roles, settings, and what ends up on the PDF).

---

**Tech:** Odoo 16 · Python · QWeb · XML · CSS
**Author:** Adem Omri

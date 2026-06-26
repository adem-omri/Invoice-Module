# Custom Invoice Template — Simple Guide

This Odoo app gives your company a **professional, branded PDF** for
**Customer Invoices** and **Credit Notes**.

Instead of Odoo's plain default invoice, you get a polished document with your
colours, logo, bank details, a QR code, signature/stamp boxes and the total
written out in words — all driven by a few settings, no design work needed.

Think of it as a smart letterhead: you set your branding once, and every
invoice you print comes out looking the same and looking good.

---

## 1. The people involved (the "actors")

This module is about **printing**, not approvals, so the roles are simple — they
reuse the normal Accounting permissions you already have.

| Actor | Who they are | What they can do |
|-------|--------------|------------------|
| **Accountant / Billing user** | Anyone who handles invoices (`Accounting / Billing` group) | Open an invoice or credit note and **Print** the professional PDF |
| **Accounting Manager** | Finance lead (`Accounting / Administrator` group) | Everything above **plus** edit the company **Invoice Template** settings (colours, bank, layout) |

> There is no approval workflow here. The invoice's own status (Draft / Posted /
> Paid) comes from standard Odoo accounting — this module just **shows** it on
> the PDF as a coloured badge.

---

## 2. The things you can set up

### a) Company branding — *the look of every invoice*
Set once per company, under **Accounting → Configuration → Invoice Template**
(or the **Invoice Template** tab on the company form). It has three sections:

**Branding**
- **Header / Secondary / Accent colours** – pick with a colour picker; they drive
  the header band, the items-table header, and the highlights/totals.
- **Tagline** – a short line under the company name.
- **Logo width** – how big the logo appears in the header.
- **Footer text** – free text centred in the bottom band.

**Bank Details** (shown in a box on the invoice if enabled)
- Bank name, account number, IBAN, SWIFT/BIC.

**Layout options** (simple on/off switches)
- **Show QR code** – a "scan to view online" code.
- **Show stamp & signature area** – two dashed boxes at the bottom.
- **Show bank details** – the bank box on/off.

### b) Per-invoice settings — *small tweaks for one invoice*
On each invoice form (the **Professional Invoice** group):
- **Template style** – **Modern**, **Classic** or **Minimal** (different fonts/spacing).
- **Custom invoice note** – a free note printed on that invoice only.

---

## 3. How you use it (the everyday flow)

```
   Set branding once            Then, for every invoice
   -----------------            ------------------------
   Company → Invoice            Open invoice/credit note
   Template tab                          │
   (colours, bank,                       │  Print →
   logo, layout)                         ▼
        │                        Professional Invoice
        └──────────────►         (branded PDF) 🧾
```

In plain words:
1. **Once:** a manager fills in the company's **Invoice Template** settings.
2. **Every time:** open any customer invoice or credit note, hit
   **Print → Professional Invoice**, and the branded PDF comes out.
3. Want a quick look without printing a real one? Use the **Preview** button on
   the company settings — it opens the report on your latest invoice.

---

## 4. What the module figures out automatically

You don't have to format anything by hand — the report fills these in for you:

- **Invoice vs Credit Note** – it detects which one it is. Credit notes get the
  **"CREDIT NOTE"** title and a **red** accent automatically.
- **Status badge** – PAID / POSTED / DRAFT / CANCELLED, colour-coded.
- **Amount in words** – the total spelled out (e.g. "One thousand two hundred…").
- **Tax breakdown & totals** – subtotal, each tax group, grand total, amount due.
- **Discount column** – appears only when a line actually has a discount.
- **Bill To / Ship To** – pulled from the customer; falls back sensibly when a
  field is empty.
- **QR code** – built from the invoice's online link (if QR is switched on).

---

## 5. What ends up on the PDF (top to bottom)

- **Header band** – your logo on the left, company name + tagline + contact info
  on the right, in your header colour.
- **Title** – big **INVOICE** or **CREDIT NOTE** wordmark.
- **Identity boxes** – Invoice No., Invoice Date, Due Date, and the **status badge**.
- **Parties** – **Bill To** and **Ship To / From** side by side.
- **Items table** – lines with product reference, quantity, price, tax,
  (discount if any) and subtotal, with neat alternating rows.
- **Totals block** – subtotal, taxes, a highlighted **TOTAL**, and amount due.
- **Amount in words** bar.
- **Your note** (if you added one).
- **Bank details** box + **QR code** (if enabled).
- **Signature & stamp** boxes (if enabled).
- **Footer band** – your footer text and a **Page X of Y** counter.

---

## 6. The three styles

Switch the **Template style** field on the invoice to change the feel:

| Style | Feel |
|-------|------|
| **Modern** (default) | Clean, rounded, soft grey panels — the standard look. |
| **Classic** | Serif title, plain white boxes — more traditional. |
| **Minimal** | No fills or borders, lots of whitespace — understated. |

---

## 7. Where to find things in Odoo

- **Any invoice/credit note → Print → Professional Invoice** – get the PDF.
- **Accounting → Configuration → Invoice Template** – the company branding settings
  (managers only).
- **Company form → Invoice Template tab** – the same settings, with a **Preview** button.
- **Invoice form → Professional Invoice group** – per-invoice style & note.

---

## 8. Quick start (first time)

1. As an **Accounting Manager**, open **Configuration → Invoice Template**.
2. Set your **colours**, **logo width**, **tagline**, **footer text** and **bank details**.
3. Turn the **QR / stamp / bank** switches on or off as you like.
4. Click **Preview** to see it on your latest invoice.
5. From then on, just open any invoice and **Print → Professional Invoice**.

That's it — set the branding once, print great-looking invoices forever.

---

### Notes & requirements
- Needs the **Accounting/Invoicing** app installed (`account`).
- The PDF uses **wkhtmltopdf** (the same engine Odoo uses for all PDF reports).
- Works for **Customer Invoices** and **Credit Notes**; vendor bills show a basic
  "VENDOR BILL" title but the template is designed for customer documents.

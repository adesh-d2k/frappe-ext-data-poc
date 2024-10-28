import re

import frappe
from frappe.model.document import Document


class Director(Document):
    def validate(self):
        self.validate_pan()
        self.validate_mobile()
        self.validate_email()
        self.validate_din()

    def validate_pan(self):
        if self.pan:
            if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', self.pan):
                frappe.throw("Invalid PAN format. It should be in the format ABCDE1234F.")

    def validate_mobile(self):
        if self.phone:
            if not re.match(r'^[789]\d{9}$', self.phone):
                frappe.throw("Invalid mobile number. It should be a 10-digit number starting with 7, 8, or 9.")

    def validate_email(self):
        if self.email:
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
                frappe.throw("Invalid email format.")

    def validate_din(self):
        if self.din:
            if not re.match(r'^\d{8}$', self.din):
                frappe.throw("Invalid DIN format. It should be an 8-digit number.")


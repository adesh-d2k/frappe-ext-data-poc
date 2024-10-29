# Copyright (c) 2024, D2K and contributors
# For license information, please see license.txt

# import frappe
import re

import frappe
from frappe.model.document import Document


class Company(Document):
	def validate(self):
		self.validate_cin()
		self.validate_llpin()
		self.validate_pan()
		self.validate_roc()

	def validate_cin(self):
		if self.cin:
			if not re.match(r"^[LU]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}$", self.cin):
				frappe.throw("Invalid CIN format. It should be an 8-digit number.")

	def validate_llpin(self):
		if self.llpin:
			if not re.match(r"^[A-Z]{3}-[0-9]{4}$", self.llpin):
				frappe.throw("Invalid LLPIN format. It should be an 8-digit number.")

	def validate_pan(self):
		if self.pan:
			if not re.match(r"^[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}$", self.pan):
				frappe.throw("Invalid PAN format. It should be in the format ABCDE1234F.")

	def validate_roc(self):
		if self.roc:
			roc = frappe.db.get_value("ROC", {"name": self.roc})
			if not roc:
				frappe.throw("Invalid ROC. It should be a valid ROC name.")

	def before_save(self):
		self.validate()
		if self.cin:
			self.name = self.cin
		elif self.llpin:
			self.name = self.llpin
		elif self.pan:
			self.name = self.pan
		else:
			frappe.throw("CIN, LLPIN or PAN is required.")

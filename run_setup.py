import frappe
frappe.init(site="erpnext.localhost")
frappe.connect()
import sys
sys.path.append("/home/maharina/erpnext/apps/erpnext")
from erpnext.setup.reference_data.setup_data import after_install
after_install()
frappe.db.commit()

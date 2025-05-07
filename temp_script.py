import frappe; frappe.init(site="erpnext.localhost"); frappe.connect(); import erpnext.setup.reference_data.setup_data; erpnext.setup.reference_data.setup_data.after_install(); frappe.db.commit()

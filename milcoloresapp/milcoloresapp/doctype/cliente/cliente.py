# Copyright (c) 2021, eoch and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Cliente(Document):
	def before_insert(self):
		nuevoUsuario(self)


def nuevoUsuario(entidad):
	if entidad.correo=='sin@correo.com':
		correo = str(entidad.ruc)+'@correo.com'
	else:
		correo = entidad.correo

	existeUsuario=frappe.db.exists('User', correo)
	if not existeUsuario:
		usuario = frappe.new_doc('User')
		usuario.username=entidad.cedula
		usuario.email = correo
		usuario.first_name = entidad.nombres
		usuario.last_name = ''
		usuario.full_name = entidad.nombres
		usuario.flags.no_welcome_mail = True
		usuario.new_password = entidad.cedula
		moduleProfile()
		 
		usuario.module_profile="Cliente"
		usuario.insert()
		usuario.add_roles("CLIENTE") 
		usuario.save()

def moduleProfile():
	existemp=frappe.db.exists('Module Profile', 'Cliente')
	if not existemp:
		frappe.get_doc({
				'doctype': 'Module Profile',
				'module_profile_name': 'Cliente',
				'block_modules': [
					{'module': 'Milcoloresapp'},
					{'module': 'Contacts'},
					{'module': 'Geo'}
				]
			}).insert()

def rolProfile():
	existemp=frappe.db.exists('Role Profile', 'ROL_CLIENTE')
	if not existemp:
		frappe.get_doc({
				'doctype': 'Role Profile',
				'role_profile': 'ROL_CLIENTE',
				"roles": [
				{
					"doctype": "Has Role",
					"parentfield": "roles",
					"role": "CLIENTE"
				}]
			}).insert()
from odoo import http
from odoo.http import request
import io
import xlsxwriter

class EmployeeExcelReport(http.Controller):

    @http.route('/employee/excel_report/<int:record_id>', type='http', auth='user')
    def generate_excel(self, record_id, **kwargs):
        record = request.env['employee.data.management'].browse(record_id)

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Employee')

        # Write data
        sheet.write('A1', 'Employee ID')
        sheet.write('B1', record.employee_id)

        sheet.write('A2', 'Name')
        sheet.write('B2', record.name)

        sheet.write('A3', 'Department')
        sheet.write('B3', record.department_id.name or '')

        sheet.write('A4', 'Job Position')
        sheet.write('B4', record.job_position.name or '')

        workbook.close()
        output.seek(0)

        return request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', 'attachment; filename="employee.xlsx"')
            ]
        )
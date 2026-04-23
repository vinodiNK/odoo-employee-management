from odoo import api, fields, models

class EmployeeDataManagement(models.Model):
    _name ='employee.data.management'
    _inherit = ['mail.thread']
    _description = 'Employee Details'

    state = fields.Selection([  # ← ADD THIS
        ('draft', 'Draft'),
        ('saved', 'Saved'),
    ], string="State", default='draft', tracking=True)

    employee_id = fields.Char(
        string="Employee ID",
        required=True,
        copy=False,
        readonly=True,
        default='New'
    )

    name = fields.Char(
        string="Name", required=True, tracking=True
    )

    work_address = fields.Char(
        string="Work Address",  tracking=True
    )

    work_email = fields.Char(
        string="Work Email",  tracking=True
    )

    work_phone = fields.Char(
        string="Work Phone",  tracking=True
    )

    department_id = fields.Many2one(
        'hr.department',
        string="Department",
        required=True,
        tracking=True
    )

    job_position = fields.Many2one(
        'hr.job',
        string="Job Position",
        tracking=True
    )
    private_address = fields.Char(string="Private Address", tracking=True)

    private_email = fields.Char(string="Private Email", tracking=True)

    private_phone = fields.Char(string="Private Phone", tracking=True)



    @api.model
    def create(self, vals):
        if vals.get('employee_id', 'New') == 'New':
            vals['employee_id'] = self.env['ir.sequence'].next_by_code('employee.data.management') or 'New'
        return super(EmployeeDataManagement, self).create(vals)

    def action_save(self):
        self.state = 'saved'

    def action_draft(self):
        self.state = 'draft'
{
    "name": "Employee Data Management",
    "author" : "Vinodi Nikeshani",
    "license" : "LGPL-3",
    "version": "17.0.1.1",

    "depends": [
        "base",
        "hr"  # ✅ ADD THIS
    ],

    "data": [
"security/ir.model.access.csv",
        "data/sequence.xml",
        "views/employee_views.xml",
        "reports/employee_report.xml",
        "reports/employee_template.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,

}
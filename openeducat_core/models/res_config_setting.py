# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_openeducat_activity = fields.Boolean(string="Activity",default=True)
    module_openeducat_facility = fields.Boolean(string="Facility",default=True)
    module_openeducat_parent = fields.Boolean(string="Parent",default=True)
    module_openeducat_assignment = fields.Boolean(string="Assignment",default=True)
    module_openeducat_classroom = fields.Boolean(string="Classroom",default=True)
    module_openeducat_fees = fields.Boolean(string="Fees",default=True)
    module_openeducat_admission = fields.Boolean(string="Admission",default=True)
    module_openeducat_timetable = fields.Boolean(string="Timetable",default=True)
    module_openeducat_exam = fields.Boolean(string="Exam",default=True)
    module_openeducat_library = fields.Boolean(string="Library",default=True)
    module_openeducat_attendance = fields.Boolean(string="Attendance",default=True)
    module_openeducat_quiz = fields.Boolean(string="Quiz Enterprise",default=True)
    module_openeducat_discipline = fields.Boolean(
        string="Discipline Enterprise",default=True)
    module_openeducat_health_enterprise = fields.Boolean(
        string="Health Enterprise",default=True)
    module_openeducat_achievement_enterprise = fields.Boolean(
        string="Achievement Enterprise",default=True)
    module_openeducat_activity_enterprise = fields.Boolean(
        string="Activity Enterprise",default=True)
    module_openeducat_admission_enterprise = fields.Boolean(
        string="Admission Enterprise",default=True)
    module_openeducat_alumni_enterprise = fields.Boolean(
        string="Alumni Enterprise",default=True)
    module_openeducat_alumni_blog_enterprise = fields.Boolean(
        string="Alumni Blog Enterprise",default=True)
    module_openeducat_alumni_event_enterprise = fields.Boolean(
        string="Alumni Event Enterprise",default=True)
    module_openeducat_alumni_job_enterprise = fields.Boolean(
        string="Alumni Job Enterprise",default=True)
    module_openeducat_job_enterprise = fields.Boolean(
        string="Job Enterprise",default=True)
    module_openeducat_assignment_enterprise = fields.Boolean(
        string="Assignment Enterprise",default=True)
    module_openeducat_attendance_enterprise = fields.Boolean(
        string="Attendance Enterprise",default=True)
    module_openeducat_student_attendance_enterprise = fields.Boolean(
        string="Student Attendance Kiosk",default=True)
    module_openeducat_bigbluebutton = fields.Boolean(
        string="Bigbluebutton Enterprise",default=True)
    module_openeducat_campus_enterprise = fields.Boolean(
        string="Campus Enterprise",default=True)
    module_openeducat_classroom_enterprise = fields.Boolean(
        string="Classroom Enterprise",default=True)
    module_openeducat_exam_enterprise = fields.Boolean(
        string="Exam Enterprise",default=True)
    module_openeducat_facility_enterprise = fields.Boolean(
        string="Facility Enterprise",default=True)
    module_openeducat_fees_enterprise = fields.Boolean(
        string="Fees Enterprise",default=True)
    module_openeducat_library_barcode = fields.Boolean(
        string="Library Barcode Enterprise",default=True)
    module_openeducat_library_enterprise = fields.Boolean(
        string="Library Enterprise",default=True)
    module_openeducat_lms = fields.Boolean(
        string="LMS Enterprise",default=True)
    module_openeducat_lms_blog = fields.Boolean(
        string="LMS Blog Enterprise",default=True)
    module_openeducat_lms_forum = fields.Boolean(
        string="LMS Forum Enterprise",default=True)
    module_openeducat_lms_gamification = fields.Boolean(
        string="LMS Gamification Enterprise",default=True)
    module_openeducat_lms_sale = fields.Boolean(
        string="LMS Sale Enterprise",default=True)
    module_openeducat_lms_survey = fields.Boolean(
        string="LMS Survey Enterprise",default=True)
    module_openeducat_meeting_enterprise = fields.Boolean(
        string="Meeting Enterprise",default=True)
    module_openeducat_online_admission = fields.Boolean(
        string="Online Admission Enterprise",default=True)
    module_openeducat_parent_enterprise = fields.Boolean(
        string="Parent Enterprise",default=True)
    module_openeducat_placement_enterprise = fields.Boolean(
        string="Placement Enterprise",default=True)
    module_openeducat_placement_job_enterprise = fields.Boolean(
        string="Placement Job Enterprise",default=True)
    module_openeducat_scholarship_enterprise = fields.Boolean(
        string="Scholarship Enterprise",default=True)
    module_openeducat_timetable_enterprise = fields.Boolean(
        string="Timetable Enterprise",default=True)
    module_openeducat_transportation_enterprise = fields.Boolean(
        string="Transportation Enterprise",default=True)
    module_openeducat_lesson = fields.Boolean(
        string="Lesson Enterprise",default=True)
    module_openeducat_skill_enterprise = fields.Boolean(
        string="Skill Enterprise",default=True)

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('openeducat_core.module_openeducat_fees_enterprise', True)

    is_installed_sale = fields.Boolean(string="Is the Sale Module Installed")

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(module_openeducat_fees_enterprise=True,   module_openeducat_activity = True, module_openeducat_facility =True,
    module_openeducat_parent = True,
    module_openeducat_assignment =True,
    module_openeducat_classroom = True,
    module_openeducat_fees = True,
    module_openeducat_admission = True,
    module_openeducat_timetable = True,
    module_openeducat_exam = True,
    module_openeducat_library = True,
    module_openeducat_attendance =True,
    module_openeducat_quiz =True,
    module_openeducat_discipline = True,
    module_openeducat_health_enterprise = True,
    module_openeducat_achievement_enterprise =True,
    module_openeducat_activity_enterprise = True,
    module_openeducat_admission_enterprise =True,
    module_openeducat_alumni_enterprise = True,
    module_openeducat_alumni_blog_enterprise =True,
    module_openeducat_alumni_event_enterprise = True,
    module_openeducat_alumni_job_enterprise =True,
    module_openeducat_job_enterprise = True,
    module_openeducat_assignment_enterprise = True,
    module_openeducat_attendance_enterprise =True,
    module_openeducat_student_attendance_enterprise =True,
    module_openeducat_bigbluebutton =True,
    module_openeducat_campus_enterprise = True,
    module_openeducat_classroom_enterprise = True,
    module_openeducat_exam_enterprise = True,
    module_openeducat_facility_enterprise =True,
    module_openeducat_library_barcode = True,
    module_openeducat_library_enterprise =True,
    module_openeducat_lms = True,
    module_openeducat_lms_blog = True,
    module_openeducat_lms_forum = True,
    module_openeducat_lms_gamification = True,
    module_openeducat_lms_sale = True,
    module_openeducat_lms_survey = True,
    module_openeducat_meeting_enterprise =True,
    module_openeducat_online_admission = True,
    module_openeducat_parent_enterprise = True,
    module_openeducat_placement_enterprise =True,
    module_openeducat_placement_job_enterprise = True,
    module_openeducat_scholarship_enterprise = True,
    module_openeducat_timetable_enterprise =True,
    module_openeducat_transportation_enterprise = True,
    module_openeducat_lesson =True,
    module_openeducat_skill_enterprise =True)
        return res

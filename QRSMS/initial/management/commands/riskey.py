import json
import os
from pprint import pprint

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from actor.models import User
from initial.models import (ACADEMIC_YEAR, STUDENT_YEAR_CHOICE, Course,
                            RegularCoreCourseLoad)
from institution.models import Degree
# from student_portal.models import Student
# from teacher_portal.models import Teacher

CURRENT_SEMESTER = 'Fall' #, 0 , (1,'Fall')



class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('operations', nargs='+', type=str)

        parser.add_argument(
            '--superuser',
            action='store_true',
            help = 'Create Super User'
        )
        parser.add_argument(
            '--deletesuperuser',
            action='store_true',
            help = 'Delete all Super User'
        )
        parser.add_argument(
            '--group',
            action='store_true',
            help = 'Create Groups'
        )
        parser.add_argument(
            '--deletegroup',
            action='store_true',
            help = 'Delete All Groups'
        )
        parser.add_argument(
            '--adduseringroup',
            action='store_true',
            help = 'Add users in Groups'
        )
        parser.add_argument(
            '--university',
            action='store_true',
            help = 'Add University'
        )
    
    def handle(self, **options):

        if options['superuser']:
            #1 Add super users
            self.create_super_users()

        if options['deletesuperuser']:
            self.delete_super_users()

        if options['group']:
            #2 Create Groups
            self.create_groups()

        if options['deletegroup']:
            self.delete_groups()

        if options['adduseringroup']:
            self.add_users_in_group()
        
        if options['university']:
            self.add_university()
        


        # for operation in options['operations']:
        #     if operation == 'superuser':
        #     #1 Add super users
        #         self.create_super_users()
        #2 Add groups
        # print("I do Something")
        # print("Dropping All Students")
        # print("No. Of Students left : ", self.drop_all_students())
        # self.insert_students()
        #self.insert_degrees()
        #self.insert_students()
        #self.insert_course_loads()
        # self.insert_courses_csv()

    def add_users_in_group(self):
        for user in User.objects.all():
            if user.is_maintainer or user.is_staff:
                user.groups.add(Group.objects.get(name='maintainer_group'))
                self.stdout.write('Added ' + str(user) + ' in ' + 'maintainer_group')
            if user.is_student:
                user.groups.add(Group.objects.get(name='student_group'))
                self.stdout.write('Added ' + str(user) + ' in ' + 'student_group')
            if user.is_teacher:
                user.groups.add(Group.objects.get(name='teacher_group'))
                self.stdout.write('Added ' + str(user) + ' in ' + 'teacher_group')
            if user.is_faculty:
                user.groups.add(Group.objects.get(name='faculty_group')) 
                self.stdout.write('Added ' + str(user) + ' in ' + 'faculty_group')

    def delete_groups(self):
        status = Group.objects.all().delete()
        self.stdout.write('All Groups Deleted')


    def create_groups(self):
        GROUPS = ['student_group', 'teacher_group', 'faculty_group', 'maintainer_group']
        PERMISSIONS = ['add', 'change', 'delete', 'view']
        MODELS = ['student', 'teacher', 'faculty']

    

        for group, model in zip(GROUPS, MODELS):
            new_group, created_group = Group.objects.get_or_create(name = group)
            self.stdout.write(str(new_group) + str(created_group))
            for permission in PERMISSIONS:
                # perm_name = model+'_portal' + "|" + model + "|" + 
                #perm_name = permission + '_' + model
                perm_name = 'Can {} {}'.format(permission, model)
                self.stdout.write('creating ' + perm_name)
                try:
                    
                    model_add_perm = Permission.objects.get(name = perm_name)
                except PermissionError:
                    self.stdout.write(self.style.write('Error ' + e))
                    continue
                new_group.permissions.add(model_add_perm)
        
        # maintainer group
        new_group, created_group = Group.objects.get_or_create(name = GROUPS[3])
        self.stdout.write(str(new_group) + str(created_group))
        for model in MODELS:
            for permission in PERMISSIONS:
                # perm_name = model+'_portal' + "|" + model + "|" + 
                #perm_name = permission + '_' + model
                perm_name = 'Can {} {}'.format(permission, model)
                self.stdout.write('creating ' + perm_name)
                try:
                    
                    model_add_perm = Permission.objects.get(name = perm_name)
                except PermissionError:
                    self.stdout.write(self.style.write('Error ' + e))
                    continue
                new_group.permissions.add(model_add_perm)
                

    
    def delete_super_users(self):
        User.objects.get(is_staff = True).delete()
        self.stdout.write('Super User Deleted')

    def drop_all_students(self):
        Student.objects.all().delete()
        self.create_super_users()
        # User.objects.get(username!='admin11196').delete()

        return User.objects.all()

    def create_super_users(self):
        

        
        nu = User(username = 'admin11196', email='hassan11196@hotmail.com', is_staff=True)    
        nu.set_password('adminhassanqrsms')
        nu.is_superuser = True
        nu.is_maintainer = True
        nu.save()
        nu = User(username = 'admin3650', email='ahsan11196@hotmail.com', is_staff=True)    
        nu.set_password('adminahsanqrsms')
        nu.is_superuser = True
        nu.is_maintainer = True
        nu.save()
        self.stdout.write(nu)

    def insert_course_loads(self):
        cloads = ["CL101 CS101 MT101 SS111 SS101 SL101 EE182",
            "SS113 CS103 EE227 EL227 MT115 CL103 SS122",
            "EE213 MT104 CS211 EL213 CS201",
            "SS103 CL205 CS301 MT206 CS205",
            "CL309 CS302 CS203 EE204 CS309 CL203"
        ]
        deg = Degree.objects.get(degree_short='BS(CS)')
        for sem,cload in enumerate(cloads):
            clist = cload.split(" ")
            r1 = RegularCoreCourseLoad(semester_season=int(((sem)%2)+1),student_year=int((sem/2) + 1),credit_hour_limit=19,degree=deg)
            self.stdout.write(r1)
            r1.save()
            for c in clist:
                self.stdout.write(Course.objects.get(course_code=c))
                r1.courses.add(Course.objects.get(course_code=c))
       
        

    def insert_degrees(self):
        # Insert Degree
        Degree.objects.all().delete()

        nd = Degree(
            minimium_years_education = 12,
            completion_year = 16,
            duration = 4,
            education_level = "Bachelors",
            degree_name = "Computer Science",
            degree_short = "BS(CS)",
        )
        nd.save()
        nd = Degree(
            minimium_years_education = 12,
            completion_year = 16,
            duration = 4,
            education_level = "Bachelors",
            degree_name = "Electrical Engineering",
            degree_short = "BS(EE)",
        )
        nd.save()
        nd = Degree(
            minimium_years_education = 12,
            completion_year = 16,
            duration = 4,
            education_level = "Bachelors",
            degree_name = "Business Administration",
            degree_short = "BBA",
        )
        nd.save()

    def insert_students(self):
        # u = User(first_name = "saya",last_name = "dapra",email= "wohra@hotmail.com",password = 'redragon')
        # u.save()
        # print(u)
        # print("In test script")
        # s = Student.create("maya","khan", "maassa@hotmail.com",'redragon')
        # u = User.objects.get(id=6)
        # s = Student(user=u,uid=u.username,arn=1700006,batch=2017)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # print(BASE_DIR)
        # print(os.path.join(BASE_DIR,'..','..','Dumps/Student.json'))


        with open(os.path.join(BASE_DIR,'..','..','Dumps\Students.json'), 'r') as json_file:

            uni_domain = "nu.edu.pk"
            DEFAULT_PASSWORD = 'hassan'
            data = json.load(json_file)
            # pprint(data)
            for d in data[:10]:
                city_short = d['uid'][2]
            
                batch_short = d['uid'][0:2]
                batch_year = int("20"+batch_short)
                roll = d['uid'][4:8]
                
                temp_name = d['name'].split(" ")
                d['first_name'] = temp_name[0]
                if(len(temp_name) > 1):
                    d['last_name'] = " ".join(temp_name[1:])
                else:
                    d['last_name'] = ""

                d['is_student'] = True
                d['batch'] = "20" + d['uid'][0:2]
                d['arn'] = d['uid'][0:2] + d['arn']

                
                if d['Department'] == 'BBA':
                    d['degree_name'] = "Bachelors of Business Administration"
                    d['degree_short'] = 'BBA'
                    d['department_name'] = 'Management Sciences'

                elif d['Department'] == 'BS(CS)':
                    d['degree_name'] = "Bachelors of Computer Science"
                    d['degree_short'] = 'BS(CS)'
                    d['department_name'] = 'Computer Science'
                
                elif d['Department'] == 'BS(SE)':
                    d['degree_name'] = "Bachelors of Software Engineering"
                    d['degree_short'] = 'BS(SE)'
                    d['department_name'] = 'Computer Science'
                
                elif d['Department'] == 'BS(EE)':
                    d['degree_name'] = "Bachelors of Electrical Engineering"
                    d['degree_short'] = 'BS(EE)'
                    d['department_name'] = 'Electrical Engineering'

                
                print(batch_year)
                print(ACADEMIC_YEAR - batch_year)
                d['warning_count'] = 0
                d['student_year'] = STUDENT_YEAR_CHOICE[(ACADEMIC_YEAR - batch_year)  if (ACADEMIC_YEAR - batch_year) <= 4  else 4]
                print(d['student_year'])
                d['uni_mail'] = city_short + batch_short+ roll + '@' + uni_domain
                d['attending_semester'] = True
                d['current_semester'] = 0 # Hardcode to Fall Semester
                created_user = User(first_name=d.get('first_name'),
                            last_name=d.get('last_name'),
                            email=d.get('registration_mail'),
                            username=d.get('uid'),
                            gender=d.get('gender'),
                            is_student=True,
                            CNIC=d.get('CNIC'),
                            permanent_address = d.get('address'),
                            permanent_home_phone = d.get('home_phone'),
                            permanent_postal_code = d.get('postal_code'),
                            permanent_city = d.get('city'),
                            permanent_country = d.get('country'),
                            current_address = d.get('address'),
                            current_home_phone = d.get('home_phone'),
                            current_postal_code = d.get('postal_code'),
                            current_city = d.get('city'),
                            current_country = d.get('country'),
                            nationality = 'Pakistani',
                            DOB = d.get('DOB'),
                            mobile_contact = d.get('mobile_contact'),
                            emergency_contact = d.get('emergency_contact')
                            )
                created_user.set_password(DEFAULT_PASSWORD)
                # created_user.save()
                created_student = Student(user=created_user,
                                        uid=d.get('uid'),
                                        arn=d.get('arn'),
                                        batch=d.get('batch'),
                                        degree_name_enrolled = d.get('degree_name'), 
                                        degree_short_enrolled = d.get('degree_short'),
                                        department_name_enrolled = d.get('department_name'),
                                        uni_mail = d.get('uni_mail'),
                                        student_year = d.get('student_year'),
                                        attending_semester = d.get('attending_semester'),
                                        warning_count = d.get('warning_count'),
                                        current_semester = d.get('current_semester')
                                        )
                pprint(d)
                # created_student.save()

            
            
        # print(s)
        # print(u)
        # s.save()
    def insert_courses_csv(self):
        Course.objects.all().delete()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        course_dict = [
            "course_code",
            "course_name",
            "credit_hour",
            "type"
        ]
        courses = []

        with open(os.path.join(BASE_DIR,'..','..','Dumps\course.csv'), 'r') as csv_file:
            next(csv_file) # Skip first row
            for d in csv_file:
                temp = d.split(',')
                print(temp)
                temp[3] =  temp[3].strip()
                courses.append(temp)
    
                if temp[3] == 'Core':
                    ctype = 1
                elif temp[3] == 'Elective':
                    ctype = 2
                else :
                    ctype = 3

                nc = Course(course_code = temp[0], course_name=temp[1], credit_hour=temp[2], course_type=ctype)
                nc.save()

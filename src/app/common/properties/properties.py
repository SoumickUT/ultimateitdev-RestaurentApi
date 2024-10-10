from src.app.common.properties import properties_dev
from src.app.common.properties import properties_qa

# db_url = properties_dev.dev_db_url
db_url = properties_dev.dev_db_url_threee
# db_url = properties_qa.qa_db_url

########################################################################
# 1) MyRestaurents properties:
########################################################################
MyRestaurents               = "/MyRestaurents"
prefix                      = "/MyRestaurents"       # Delete this?
education                   = "/MyRestaurents"       # Delete this?
skill                       = "/MyRestaurents"       # Delete this?
achievement                 = "/MyRestaurents"       # Delete this?
notification                = "/MyRestaurents"       # Delete this?
tags                        = "MyRestaurents"        # Delete this?

# MyRestaurents - Signup:
signup_tag                  = 'MyRestaurents - Signup:'
student_user_reg            = '/signup'                     # /my_profile/user/create
email_verification          = '/signup/verify_email'
email_code_verify           = '/signup/verify_email/verify_code'
resend_code                 = '/signup/verify_email/resend_code'
student_user_verify         = '/verify'                     # ???

# MyRestaurents - Login:
login_tag                   = 'MyRestaurents - Login:'
student_user_login          = '/login'
forget_password_code        = '/login/forgot_password/send_code'
forget_password_code_verify = '/login/forgot_password/verify_code'
update_user_forget_password = '/login/forgot_password/update'

# MyRestaurents - My Profile:
profile_tag                 = 'MyRestaurents - My Profile:'
sign_up_tag                 = 'MyRestaurents - Signup:'
login_tag                   = 'MyRestaurents - Login:'
profile_picture_tag         = 'MyRestaurents - My Profile - Profile Picture:'
my_profile_tag              = 'MyRestaurents - view Profile:' 
get_all_student_user        = '/my_profile/user/get_all'
get_one_student_user        = '/my_profile/user/get_one/{id}'
update_user                 = '/my_profile/user/update'
destroy_student_user        = '/my_profile/user/delete'

# MyRestaurents - My Profile - Profile Picture:
create_profile_picture      = '/my_profile/profile_picture/create'
update_profile_picture      = '/my_profile/profile_picture/update/{id}'

# MyRestaurents - My Profile - Cover Picture:
create_cover_picture        = '/my_profile/cover_picture/create'
update_cover_picture        = '/my_profile/cover_picture/update/{id}'

# MyRestaurents - My Profile - Notification - My Activity:
notification_tag            = 'MyRestaurents - My Profile - Notification - My Activity:'
create_notification         = '/my_profile/notification/my_activity/create'
get_all_notification        = '/my_profile/notification/my_activity/get_all'
get_one_notification        = '/my_profile/notification/my_activity/get_one/{id}'
update_notification         = '/my_profile/notification/my_activity/update/{id}'
destroy_notification        = '/my_profile/notification/my_activity/delete/{id}'
search_activity='/my_profile/notification/my_activity/search'
get_user_activaity_filter   = '/my_profile/notification/user_activity/filter/{id}'
get_all_user_activiaty      = '/my_profile/notification/my_activity/user/{id}'


# MyRestaurents - My Profile - Settings:
settings_tag                = 'MyRestaurents - My Profile - Settings:'
forget_pass_tag             ='MyRestaurents - My Profile - Settings -Forget password:'
change_email_tag             ='MyRestaurents - My Profile - Settings -Change Email:'
change_Phone_tag             ='MyRestaurents - My Profile - Settings -Change Phone Number:'
change_username_tag             ='MyRestaurents - My Profile - Settings -Change Username:'
change_active_tag             ='MyRestaurents - My Profile - Settings - Update user active:'

update_user_email           = '/my_profile/settings/change_email'
update_email_verification   = '/my_profile/settings/change_email/verify_email'
update_email_code_verify    = '/my_profile/settings/change_email/verify_code'
update_email_resend_code    = '/my_profile/settings/change_email/resend_code'
update_user_phonenumber     = '/my_profile/settings/change_phone'
update_user_username        = '/my_profile/settings/change_username'
update_user_password        = '/my_profile/settings/change_password'

# MyRestaurents - My Profile - My Education:
education_tag               = 'MyRestaurents - My Profile - My Education:'
create_user_education       = '/my_profile/my_education/create'
get_all_user_education      = '/my_profile/my_education/get_all'
get_one_user_education      = '/my_profile/my_education/get_one'
update_user_education       = '/my_profile/my_education/update/{id}'
destroy_user_education      = '/my_profile/my_education/delete/{id}'
get_user_education          = '/my_profile/my_education/user'

# MyRestaurents - My Profile - My Skill:
skill_tag                   = 'MY Restaurants - Order Creating:'
dummy_tag                   = 'MY Restaurants - Dummy Creating:'
OrderSale_tag               = 'MY Restaurants - Order Sale:'
create_user_skill           = '/my_profile/my_skill/create'
get_all_user_skill          = '/my_profile/my_skill/get_all'
get_one_user_skill          = '/my_profile/my_skill/get_one/{id}'
update_user_skill           = '/my_profile/my_skill/update/{id}'
destroy_user_skill          = '/my_profile/my_skill/delete/{id}'
get_user_skill              = '/my_profile/my_skill/user/{id}'

Promotion_tag               = 'MY Restaurants - Promotion & Voucher Details:'
menu_tag                    = 'MY Restaurants - Menu:'
register_tag                = 'MY Restaurants - Register:'
sub_menu_tag                = 'MY Restaurants - Sub Menu:'
table_info_tag              = 'MY Restaurants - Table Info:'
waiter_info_tag             = 'MY Restaurants - Waiter Info:'
menucategory_tag            = 'MY Restaurants - Menu Category:'
jwt_category_tag            = 'MY Restaurants - jwt Category:'


# MyRestaurents - My Profile - My Achievement:
achievement_tag             ='MY Restaurants - Order Details:'
create_user_achievement     ='/my_profile/my_achievement/create/picture'
get_all_user_achievement    = '/my_profile/my_achievement/get_all'
get_one_user_achievement    = '/my_profile/my_achievement/get_one/{id}'
update_user_achievement     = '/my_profile/my_achievement/update/{id}'
destroy_user_achievement    = '/my_profile/my_achievement/delete/{id}'
get_user_achievement        = '/my_profile/my_achievement/user/{id}'
create_user_achievement_no_photo='/my_profile/my_achievement/create'

# MyRestaurents - My Profile - My Pricing Plan:
update_user_plan_id_user_plan_name = '/update_user_plan_id'

# MyRestaurents - My Profile - My Order and Payment - Payment Card:
card_tag                    = 'MyRestaurents - My Profile - My Order and Payment - Payment Card:'
create_user_card            = '/my_profile/my_order_and_payment/payment_card/create'
get_all_user_card           = '/my_profile/my_order_and_payment/payment_card/get_all'
get_one_user_card           = '/my_profile/my_order_and_payment/payment_card/get_one/{id}'
update_user_card            = '/my_profile/my_order_and_payment/payment_card/update/{id}'
destroy_user_card           = '/my_profile/my_order_and_payment/payment_card/delete/{id}'
get_user_card               = '/my_profile/my_order_and_payment/payment_card/user/{id}'

create_card_information     = '/my_profile/my_order_and_payment/payment_card/create'
get_all_card_information    = '/my_profile/my_order_and_payment/payment_card/get_all'
get_one_card_information    = '/my_profile/my_order_and_payment/payment_card/get_one/{id}'
update_card_information     = '/my_profile/my_order_and_payment/payment_card/update/{id}'
destroy_card_information    = '/my_profile/my_order_and_payment/payment_card/delete/{id}'
get_user_card_information   = '/my_profile/my_order_and_payment/payment_card/user/{id}'

# MyRestaurents - My Profile - My Order and Payment - Billing Address:
billing_address_tag         = 'MyRestaurents - My Profile - My Order and Payment - Billing Address:'
create_billing_address      = '/my_profile/my_order_and_payment/billing_address/create'
get_all_billing_address     = '/my_profile/my_order_and_payment/billing_address/get_all'
get_one_billing_address     = '/my_profile/my_order_and_payment/billing_address/get_one/{id}'
update_billing_address      = '/my_profile/my_order_and_payment/billing_address/update/{id}'
destroy_billing_address     = '/my_profile/my_order_and_payment/billing_address/delete/{id}'
get_user_biiling_address    = '/my_profile/my_order_and_payment/billing_address/user/{id}'

create_billing_has_address  = '/billing_has_address/create'
get_all_billing_has_address = '/billing_has_address/all'


########################################################################
# 2) service_student_admin properties:
#########################################################################
service_student_admin       = "/service_student_admin"
plan_has_service            = "/service_student_admin"                      # Delete this?
book_type_has_book          = "/service_student_admin/book_type_has_book"   # Delete this?
report_problem              = "/MyRestaurents/report_problem"        # Delete this?

# ====Pricing Plan====
# service_student_admin - Pricing Plan - Service Type:
Service_Type_tag                = 'service_student_admin - Pricing Plan - Service Type:'
create_service_type          = '/pricing_plan/service_type/create'
get_all_service_type = '/pricing_plan/service_type/get_all'
get_one_service_type = '/pricing_plan/service_type/get_one/{id}'
update_service_type   = '/pricing_plan/service_type/update/{id}'
delete_service_type   = '/pricing_plan/service_type/delete/{id}'

# service_student_admin - Pricing Plan - Service:
service_tag                 = 'service_student_admin - Pricing Plan - Service:'
create_service              = '/pricing_plan/service/create'
get_all_service             = '/pricing_plan/service/get_all'
get_one_service             = '/pricing_plan/service/get_one/{id}'
update_service              = '/pricing_plan/service/update/{id}'
delete_service              = '/pricing_plan/service/delete/{id}'
get_all_service_type_service= '/pricing_plan/service_type_service/all'
get_all_signup    = '/pricing_plan/get_all_signup/all'
class_name="\'Class\'"

# service_student_admin - Pricing Plan - Service Type has Service:
Service_type_has_Service_tag        = 'service_student_admin - Pricing Plan - Service Type has Service:'
create_Service_type_has_Service     = '/pricing_plan/Service_type_has_Service/create'
get_all_Service_type_has_Service    = '/pricing_plan/Service_type_has_Service/all'
get_one_Service_type_has_Service    = '/pricing_plan/Service_type_has_Service/get_one/{id}'
update_Service_type_has_Service     = '/pricing_plan/Service_type_has_Service/update/{id}'
destroy_Service_type_has_Service    = '/pricing_plan/Service_type_has_Service/delete/{id}'
get_one_service_type_under_service  = '/pricing_plan/service_type_under_service/one/{id}'
get_one_service_under_service_type  = '/pricing_plan/service_under_service_type/one/{id}'

# service_student_admin - Pricing Plan - Plan:
plan_tag                    = 'service_student_admin - Pricing Plan - Plan:'
create_plan                 = '/pricing_plan/plan/create'
get_all_plan                = '/pricing_plan/plan/get_all'
get_one_plan                = '/pricing_plan/plan/get_one/{id}'
update_plan                 = '/pricing_plan/plan/update/{id}'
delete_plan                 = '/pricing_plan/plan/delete/{id}'

# service_student_admin - Pricing Plan - Plan has Service:
plan_has_service_tag        = 'service_student_admin - Pricing Plan - Plan has Service:'
create_plan_has_service     = '/pricing_plan/plan_has_service/create'
get_all_plan_has_service    = '/pricing_plan/plan_has_service/get_all'
get_one_plan_has_service    = '/pricing_plan/plan_has_service/get_one/{id}'
update_plan_has_service     = '/pricing_plan/plan_has_service/update/{id}'
destroy_plan_has_service    = '/pricing_plan/plan_has_service/delete/{id}'
get_all_service_under_plan  = '/plan_has_service/all'
get_one_service_under_plan  = '/plan_has_service_under_plan/{id}'

# service_student_admin - Pricing Plan - Subject:
subject_tag                 = 'service_student_admin - Pricing Plan - Subject:'
create_subject              = '/pricing_plan/subject/create'
all_subjects                = '/pricing_plan/subject/get_all'
course_subjects             = '/pricing_plan/subject/course/{id}'
get_one_subject             = '/pricing_plan/subject/get_one/{id}'
destroy_subject             = '/pricing_plan/subject/delete/{id}'
update_subject              = '/pricing_plan/subject/update/{id}'

# service_student_admin - Pricing Plan - Service has Subject:
service_has_subject_tag     = 'service_student_admin - Pricing Plan - Service has Subject:'
create_service_has_subject  = '/pricing_plan/service_has_subject/create'
get_all_service_has_subject = '/pricing_plan/service_has_subject/get_all'
get_one_service_has_subject = '/pricing_plan/service_has_subject/get_one/{id}'
update_service_has_subject  = '/pricing_plan/service_has_subject/update/{id}'
destroy_service_has_subject = '/pricing_plan/service_has_subject/delete/{id}'
get_all_service_subject     = '/pricing_plan/service_has_subject/all'
get_one_subject_under_service='/pricing_plan/subject_under_service/one/{id}'

# service_student_admin - Pricing Plan - Book:
book_tag                    = 'service_student_admin - Pricing Plan - Book:'
create_book                 = '/pricing_plan/book/create'
all_course_book             = '/pricing_plan/book/get_all'
get_subject_books           = '/pricing_plan/book/subject/{id}'
get_one_book                = '/pricing_plan/book/get_one/{id}'
update_book                 = '/pricing_plan/book/update/{id}'
destroy_course_book         = '/pricing_plan/book/delete/{id}'
get_course_books            = '/pricing_plan/book/course/{id}'

# service_student_admin - Pricing Plan - Subject has Book:
Subject_has_Book_tag        = 'service_student_admin - Pricing Plan - Subject has Book:'
create_Subject_has_Book     = '/pricing_plan/subject_has_book/create'
get_all_Subject_has_Book    = '/pricing_plan/subject_has_book/get_all'
get_one_Subject_has_Book    = '/pricing_plan/subject_has_book/get_one/{id}'
update_Subject_has_Book     = '/pricing_plan/subject_has_book/update/{id}'
destroy_Subject_has_Book    = '/pricing_plan/subject_has_book/delete/{id}'
get_all_Subject_Book        = '/pricing_plan/subject_has_book/all'
get_one_book_under_subject  = '/pricing_plan/book_under_subject/one/{id}'

# service_student_admin - Pricing Plan - Book Type:
book_type_tag               = 'service_student_admin - Pricing Plan - Book Type:'
create_book_type            = '/pricing_plan/book_type/create'
get_all_book_type           = '/pricing_plan/book_type/get_all'
get_one_book_type           = '/pricing_plan/book_type/get_one/{id}'
update_book_type            = '/pricing_plan/book_type/update/{id}'
destroy_book_type           = '/pricing_plan/book_type/delete/{id}'

# service_student_admin - Pricing Plan - Book Type has Book:
book_type_has_book_tag      = 'service_student_admin - Pricing Plan - Book Type has Book:'
create_book_type_has_book   = '/pricing_plan/book_type_has_book/create'
get_all_book_type_has_book  = '/pricing_plan/book_type_has_book/get_all'
get_one_book_type_has_book  = '/pricing_plan/book_type_has_book/get_one/{id}'
update_book_type_has_book   = '/pricing_plan/book_type_has_book/update/{id}'
destroy_book_type_has_book  = '/pricing_plan/book_type_has_book/delete/{id}'
get_one_book_under_book_type= '/pricing_plan/book_under_book_type/{id}'

# ====Student User Details====
# service_student_admin - Student User Profile Details:
User_Detail_tag             = 'service_student_admin - Student User Profile Details:'
create_student_User_Details = '/pricing_plan/student_User_Details/create'
get_all_student_User_Detail = '/pricing_plan/student_User_Details/get_all'
get_one_student_User_Detail = '/pricing_plan/student_User_Details/get_one/{id}'
update_student_User_Detail  = '/pricing_plan/student_User_Details/update/{id}'
destroy_student_User_Detail = '/pricing_plan/student_User_Details/delete/{id}'

# update_user_active
update_user_active_tag      = 'service_student_admin - Student User Profile Settings:'
update_user_active          = '/update_user_active'

# ==== . ====
# service_student_admin - Help:
help_tag                    = 'service_student_admin - Help:'
create_help                 = '/manage/help/create'
get_all_help                = '/manage/help/get_all'
get_one_help                = '/manage/help/get_one/{id}'
update_help                 = '/manage/help/update/{id}' 
destroy_help                = '/manage/help/delete/{id}'

# service_student_admin - Report Problem:
report_problem_tag          = 'service_student_admin - Report Problem:'
create_report_problem       = '/manage/report_problem/create'
get_all_report_problem      = '/manage/report_problem/get_all'
get_one_report_problem      = '/manage/report_problem/get_one/{id}'
update_report_problem       = '/manage/report_problem/update/{id}'
destroy_report_problem      = '/manage/report_problem/delete/{id}'

# service_student_admin - Notice (for Student User Site):
notice_tag                  = 'service_student_admin - Notice (for Student User Site):'
create_notice               = '/manage/notice/create'
get_all_notice              = '/manage/notice/get_all'
get_one_notice              = '/manage/notice/get_one/{id}'
update_notice               = '/manage/notice/update/{id}'
destroy_notice              = '/manage/notice/delete/{id}'

# service_student_admin - JWT
jwt_tag                     = 'service_student_admin - JWT:'
jwt_user_create             = '/auth/jwt_user/create'
get_all_jwt_user            = '/auth/jwt_user/get_all'
get_one_jwt_user            = '/auth/jwt_user/get_one/{id}'
update_jwt_user             = '/auth/jwt_user/update/{id}'
destroy_jwt_user            = '/auth/jwt_user/delete/{id}'
jwt_user_login              = '/auth/jwt_user/login'


swagger_tag='service_student_admin - swagger'

swagger_autentication="/users/authentication"

successful_login='now you can access:http://dev.user.student.ui.eschooljourney.com:8000/docs#/'



# service_student_admin - Demo Data:
demodata_tag                = 'service_student_admin - Demo Data:'
create_demo_data            = '/demo/data/create'


########################################################################
# 3) service_master_admin properties:
#########################################################################
service_master_admin        = "/service_master_admin"
prefix                      = "/service_master_admin"   # Delete this?
tags                        = "service_master_admin"    # Delete this?

# ====Role Based Access Control (RBAC)====
# service_master_admin - RBAC - Permission:
permission_tag              = 'service_master_admin - RBAC - Permission:'
create_permission           = '/rbac/permission/create'
get_all_permission          = '/rbac/permission/get_all/'
get_one_permission          = '/rbac/permission/get_one/{id}'
update_permission           = '/rbac/permission/update/{id}'
destroy_permission          = '/rbac/permission/delete/{id}'

# service_master_admin - RBAC - Role:
role_tag                    = 'service_master_admin - RBAC - Role:'
create_role                 = '/rbac/role/create'
get_all_role                = '/rbac/role/get_all'
get_one_role                = '/rbac/role/get_one/{id}'
update_role                 = '/rbac/role/update/{id}'
destroy_role                = '/rbac/role/delete/{id}'

# service_master_admin - RBAC - Group:
group_tag                   = 'service_master_admin - RBAC - Group:'
create_group                = '/rbac/group/create'
get_all_group               = '/rbac/group/get_all'
get_one_group               = '/rbac/group/get_one/{id}'
update_group                = '/rbac/group/update/{id}'
destroy_group               = '/rbac/group/delete/{id}'

# service_master_admin - RBAC - Role has Permission:
role_has_permission_tag     = 'service_master_admin - RBAC - Role has Permission:'
create_role_has_permission  = '/rbac/role_has_permission/create'
get_all_role_has_permission = '/rbac/role_has_permission/get_all'
get_one_role_has_permission = '/rbac/role_has_permission/get_one/{id}'
update_role_has_permission  = '/rbac/role_has_permission/update/{id}'
destroy_role_has_permission = '/rbac/role_has_permission/delete/{id}'

# service_master_admin - RBAC - Group has Role:
group_has_role_tag          = 'service_master_admin - RBAC - Group has Role:'
create_group_has_role       = '/rbac/group_has_role/create'
get_all_group_has_role      = '/rbac/group_has_role/get_all'
get_one_group_has_role      = '/rbac/group_has_role/get_one/{id}'
update_group_has_role       = '/rbac/group_has_role/update/{id}'
destroy_group_has_role      = '/rbac/group_has_role/delete/{id}'

# service_master_admin - RBAC - Group has User:
group_has_user_tag          = 'service_master_admin - RBAC - Group has User:'
create_group_has_user       = '/rbac/group_has_user/create'
get_all_group_has_user      = '/rbac/group_has_user/get_all'
get_one_group_has_user      = '/rbac/group_has_user/get_one/{id}'
update_group_has_user       = '/rbac/group_has_user/update/{id}'
destroy_group_has_user      = '/rbac/group_has_user/delete/{id}'

# service_master_admin - RBAC - User Access Details:
User_Details_tag            = 'service_master_admin - RBAC - User Access Details:'
create_User_Details         = '/rbac/User_Details/create'
get_all_User_Detail         = '/rbac/User_Detail/get_all'
get_one_User_Detail         = '/User_Detail/get_one/{id}'
update_User_Detail          = '/User_Detail/update/{id}'
destroy_User_Detail         = '/User_Detail/delete/{id}'


########################################################################
# 4) service_order_payment properties:
#########################################################################
service_order_and_payment   = "service_order_and_payment"
checkout                    = "/service_order_and_payment"      # Delete this?

#service_order_and_payment - Checkout:
checkout_tag                = 'service_order_and_payment - Checkout:'
create_checkout             = '/checkout/create'
get_all_checkout            = '/checkout/get_all'
get_all_checkout_with_service = '/checkout/get_all_checkout_with_service'
get_one_checkout            = '/checkout/get_one/{id}'
update_checkout             = '/update_checkout/{id}'
destroy_checkout            = '/destroy_checkout/{id}'
get_user_checkout           = '/checkout/user/one/{id}'
get_user_multiple_service   ='/checkout/multiple_service/one/{id}'



# 
create_order                = '/create'
get_all_order               = '/all'
get_one_order               = '/one/{id}'
update_order                = '/update/{id}'
destroy_order               = '/delete/{id}'
get_user_order              = '/user/{id}'

# 
create_payment              = '/create'
get_all_payment             = '/all'
get_one_payment             = '/one/{id}'
update_payment              = '/update/{id}'
destroy_payment             = '/delete/{id}'
get_order_payment           = '/user/{id}'


#####################################################################
# 5) service_study_content properties:
#####################################################################
service_study_content                   = "/service_study_content"
prefix                                  = "/service_study_content"      # Delete this?
tags                                    = "service_study_content"       # Delete this?

# ====MCQ Test====
# service_study_content - MCQ Test Name (Admin):
mcq_pattern_tag                         = 'service_study_content - MCQ Test Name (Student Admin):'
create_mcqpattern                       = '/mcq_test/admin/test_name/create'
get_all_mcqpattern                      = '/mcq_test/admin/test_name/get_all'
get_one_mcqpattern                      = '/mcq_test/admin/test_name/get_one/{id}'
update_mcqpattern                       = '/mcq_test/admin/test_name/update/{id}'
destroy_mcqpattern                      = '/mcq_test/admin/test_name/delete/{id}'
get_one_book_under_mcqtest              = '/book_under_mcqtest/one/{id}'

# service_study_content - MCQ Test - Question Answer - (Student Admin):
mcq_pattern_Answer_tag                  = 'service_study_content - MCQ Test - Question Answer - (Student Admin):'
create_mcqpattern_answer                = '/admin/mcq_question_answer/create'
get_all_mcqpattern_answer               = '/admin/mcq_question_answer/get_all'
get_one_mcqpattern_answer               = '/admin/mcq_question_answer/get_one/{id}'
update_mcqpattern_answer                = '/admin/mcq_question_answer/update/{id}'
destroy_mcqpattern_answer               = '/admin/mcq_question_answer/delete/{id}'
get_user_mcqtest                        = '/mcqtest/one/{id}'
get_all_question_under_mcqtest          = '/question_under_mcqtest/all'
get_one_question_under_mcqtest          = '/question_under_mcqtest/one/{id}'

# service_study_content - MCQ Test (Student User):
mcq_pattern_take_test_tag               = 'service_study_content - MCQ Test (Student User):'
create_mcq_user_test                    = '/mcq_test/student_user/take_test/create'
get_all_mcq_user_test                   = '/mcq_test/student_user/take_test/get_all'
get_one_mcq_user_test                   = '/mcq_test/student_user/take_test/get_one/{id}'
update_mcq_user_test                    = '/mcq_test/student_user/take_test/update/{id}'
destroy_mcq_user_test                   = '/mcq_test/student_user/take_test/delete/{id}'
get_one_mcq_user_questions              = '/one/answer/'
get_mcq_user_invidual_correct           = '/all/'

get_mcq_user_answer_analysis            = '/mcq_test/student_user/take_test/one/analysis/'
get_mcq_user_answer_summary_correct     = '/one/sumcorrect/'
get_mcq_user_answer_summary_INCORRECT   = '/one/sumincorrect/'
get_one_mcq_user_invidual_correct       = '/one/individual/'
get_mcq_user_exits                      = '/mcq_user_exits/all'
get_mcq_user_question_count             = '/question_count/all'

# ====Writing Test====
# service_study_content - Writing Test Name (Student Admin):
writing_pattern_tag                     = 'service_study_content - Writing Test Name (Student Admin):'
create_writing_pattern                  = '/writing_test/admin/test_name/create'
get_all_writing_pattern                 = '/writing_test/admin/test_name/get_all'
get_one_writing_pattern                 = '/writing_test/admin/test_name/get_one/{id}'
update_writing_pattern                  = '/writing_test/admin/test_name/update/{id}'
destroy_writing_pattern                 = '/writing_test/admin/test_name/delete/{id}'
get_one_book_under_writing_pattern      = '/book_under_writing_test/one/{id}'

# service_study_content - Writing Test - Question Answer (Student Admin):
writing_pattern_Answer_tag              = 'service_study_content - Writing Test - Question Answer (Student Admin):'
create_writing_test_student_admin       = '/writing_test/admin/writing_question_answer/create'
get_all_writing_test_student_admin      = '/writing_test/admin/writing_question_answer/get_all'
get_one_writing_test_student_admin      = '/writing_test/admin/writing_question_answer/get_one/{id}'
get_all_review_writing_test_answer      = '/writing_test/admin/writing_question_answer_review/all'
update_writing_test_student_admin       = '/writing_test/admin/writing_question_answer/update/{id}'
get_user_writing_test_student_admin     = '/writing_test/admin/writing_question_answer/one/user/'
destroy_writing_test_student_admin      = '/writing_test/admin/writing_question_answer/delete/{id}'

# service_study_content - Writing Test (Student User):
writing_pattern_take_test_tag           = 'service_study_content - Writing Test (Student User):'
create_writing_test_student_user        = '/writing_test/student_user/take_test/create'
get_all_writing_test_student_user       = '/writing_test/student_user/take_test/get_all'
get_one_writing_test_student_user       = '/writing_test/student_user/take_test/get_one/{id}'
get_all_review_writing_test_user_answer = '/writing_test/student_user/take_test_review/get_all'
update_writing_test_student_user        = '/writing_test/student_user/take_test/update/{id}'
get_user_writing_test_student_user      = '/one/user/'
destroy_writing_test_student_user       = '/writing_test/student_user/take_test/delete/{id}'
get_writing_user_answer_analysis        = '/one/analysis/'

# ====Video====
# service_study_content - Video Topic (Student Admin):
video_topic_tag                 = 'service_study_content - Video Topic (Student Admin):'
create_video_topic              = '/video/admin/video_topic/create'
get_all_video_topic             = '/video/admin/video_topic/get_all'
get_one_video_topic             = '/video/admin/video_topic/one/{video_topic_id}'
update_video_topic              = '/video/admin/video_topic/update/{video_topic_id}'
destroy_video_topic             = '/video/admin/video_topic/delete/{video_topic_id}'
get_one_topic_under_subject     = '/topic_under_subject/one/{video_topic_id}'

# service_study_content - Video:
video_adding_tag                = 'service_study_content - Video:'
create_video_adding             = '/video/admin/video_detail/create'
get_all_video_adding            = '/video/admin/video_detail/get_all'
get_one_video_adding            = '/video/admin/video_detail/get_one/{video_id}'
update_video_adding             = '/video/admin/video_detail/update/{video_id}'
destroy_video_adding            = '/video/admin/video_detail/delete/{video_id}'
get_one_video_under_topic       = '/video_under_topic/one/{video_topic_id}'
video_under_subject              ='/video/admin/video_detail/video_under_subject/{subject_id}'
# ====Audio====
# service_study_content - Audio Topic (Student Admin):
audio_topic_admin_tag           = 'service_study_content - Audio Topic (Student Admin):'
create_admin_audio_topic        = '/audio/admin/audio_topic/create'
get_all_admin_audio_topic       = '/audio/admin/audio_topic/get_all'
get_one_admin_audio_topic       = '/audio/admin/audio_topic/get_one/{audio_topic_id}'
update_admin_audio_topic        = '/audio/admin/audio_topic/update/{audio_topic_id}'
destroy_admin_audio_topic       = '/audio/admin/audio_topic/delete/{audio_topic_id}'
get_one_topic_admin_subject     = '/topic_admin_subject/one/{audio_topic_id}'

# service_study_content - Audio (Student Admin):
audio_topic_admin_add_tag       = 'service_study_content - Audio (Student Admin):'
create_admin_audio              = '/audio/admin/audio_detail/create'
get_all_admin_audio             = '/audio/admin/audio_detail/get_all'
get_one_admin_audio             = '/audio/admin/audio_detail/get_one/{audio_id}'
update_admin_audio              = '/audio/admin/audio_detail/update/{audio_id}'
destroy_admin_audio             = '/audio/admin/audio_detail/delete/{audio_id}'
get_one_admin_audio_under_topic = '/admin_audio_under_topic/one/{audio_topic_id}'

# service_study_content - Audio Topic (Student User):
audio_topic_user_tag            = 'service_study_content - Audio Topic (Student User):'
create_user_audio_topic         = '/audio/student_user/audio_topic/create'
get_all_user_audio_topic        = '/audio/student_user/audio_topic/get_all'
get_one_user_audio_topic        = '/audio/student_user/audio_topic/get_one/{audio_topic_id}'
update_user_audio_topic         = '/audio/student_user/audio_topic/update/{audio_topic_id}'
destroy_user_audio_topic        = '/audio/student_user/audio_topic/delete/{audio_topic_id}'
get_one_topic_subject           = '/audio/student_user/topic_subject/one/{audio_topic_id}'

# service_study_content - Audio (Student User):
audio_topic_user_add_tag        = 'service_study_content - Audio (Student User):'
create_user_audio               = '/audio/student_user/audio_detail/create'
get_all_user_audio              = '/audio/student_user/audio_detail/get_all'
get_one_user_audio              = '/audio/student_user/audio_detail/get_one/{audio_id}'
update_user_audio               = '/audio/student_user/audio_detail/update/{audio_id}'
destroy_user_audio              = '/audio/student_user/audio_detail/delete/{audio_id}'
get_one_audio_under_topic       = '/audio_under_topic/one/{audio_topic_id}'

# ====PDF====
# 
test_pdf_book='/pdf_to_text'
get_pdf_text='/pdf_text/book'
update_pdf_text='/pdf_text/update'
pdf_to_text_without_id='/pdf_to_text/'
all_pdf_books='/pdf_book/all'
get_course_pdf_books='/course/{id}'

# 
create_chapter='/chapter/create'
all_chapters='/chapter/all'
get_books_chapter='/chapter/book/{id}'
get_one_chapter='/chapter/one/{id}'
update_chapter='/chapter/update/{id}'
destroy_chapter='/chapter/delete/{id}'

# 
create_lesson='/lesson/create'
all_lessons='/lesson/all'
get_books_lessons='/lesson/books/{id}'
get_one_lesson='/lesson/one/{id}'
update_lesson='/lesson/update/{id}'
destroy_lesson='/lesson/delete/{id}'

# 
create_picture_lesson_content='/picture_content/create'
update_lesson_content='/content/update/{id}'
create_lesson_content='/content/create'
get_all_lesson_content='/content/all'
get_one_lesson_content='/content/lesson/lesson/{id}'
get_one_content='/content/one/{id}'
get_one_lesson_content_picture='/content/picture/{id}'
destroy_lesson_content='/content/delete/{id}'
get_book_all_detail='/book_detail/all'
get_one_book_detail='/book_detail/one/{id}'
get_page_limits_book_detail='/book_detail/page_limits/'

# 
create_pdf_chapter_lesson='/pdf_chapter_lesson/create'
get_all_pdf_chapter_lesson='/pdf_chapter_lesson/all'
get_pdf_book_chapter_lesson='/pdf_chapter_lesson/pdf_book/{id}'
get_one_pdf_chapter_lesson='/pdf_chapter_lesson/one/{id}'
update_pdf_chapter_lesson='/pdf_chapter_lesson/update/{id}'
destroy_pdf_chapter_lesson='/pdf_chapter_lesson/delete/{id}'
get_pdf_book_lesson_contents='/pdf_book_lesson_contents/all'
get_pdf_book_chapter_contents='/pdf_book_chapter_contents/all'
get_page_limits_pdf_book_detail='/pdf_book_detail/page_limit'
get_pdf_book_all='/pdf_book_all/{id}'

# 
create_pdftorn='/pdftorn/create'
get_all_pdftorn='/pdftorn/all'
get_one_pdftorn='/pdftorn/one'
update_pdftorn='/pdftorn/update/{id}'
destroy_pdftorn='/pdftorn/delete/{id}'


#### Below Can be deleted ??? ########################
#
mcq_user_test_tag='service_study_content - MCQ Test:' 
create_mcq_test_answer='/mcq_test/admin/mcq_question_answer/create'
get_all_mcq_test_answer='/mcq_test/admin/mcq_question_answer/get_all'
get_one_mcq_test_answer='/mcq_test/admin/mcq_question_answer/get_one/{id}'
get_all_review_mcq_test_answer='/mcq_test/admin/mcq_question_answer_review/all'
update_mcq_test_answer='/mcq_test/admin/mcq_question_answer/update/{id}'
get_user_mcq_test_answer='/mcq_test/admin/mcq_question_answer/one/user/{id}'
destroy_mcq_test_answer='/mcq_test/admin/mcq_question_answer/delete/{id}'

error_message='Sorry for the inconvenience'
# ====


Report_Problem='tbl_stu_adm-stu_user_site_report_problem'

Student_User_Site_Help='tbl_stu_adm-stu_user_site_help'

Student_User_Site_Notice='tbl_stu_adm-stu_user_site_notice'

Group='tbl_master_admin-rbac-group'

Role='tbl_master_admin-rbac-role'

Permission='tbl_master_admin-rbac-permission'

Role_Has_Permission='tbl_master_admin-rbac-role_has_permission'

Group_Has_Role='tbl_master_admin-rbac-group_has_role'

Group_Has_User='tbl_master_admin-rbac-group_has_user'

User_Access_Details='tbl_master_admin-rbac-user_access_details'

Checkout='tbl_order_and_payment-checkout'

EsjUser='tbl_stu_usr-users'

Verify_Email='tbl_stu_usr-users_verify_email'

Verify_Phone='tbl_stu_usr-users_verify_phone'

Profile_Picture='tbl_stu_usr-my_profile-profile_picture'

Cover_Picture='tbl_stu_usr-my_profile-cover_picture'

My_Education='tbl_stu_usr-my_profile-my_education'

My_Skill='tbl_stu_usr-my_profile-my_skill'

My_Achievement='tbl_stu_usr-my_profile-my_achievement'

Notification_My_Inbox='tbl_stu_usr-my_profile-notification-my_inbox'

Notification_My_Activity='tbl_stu_usr-my_profile-notification-my_activity'

Billing_Address='tbl_stu_usr-my_profile-billing_address'

Payment_Card='tbl_stu_usr-my_profile-payment_card'

Service_Type='tbl_stu_adm-pricing_plan-service_type'

Service='tbl_stu_adm-pricing_plan-service'

Service_Type_Has_Service='tbl_stu_adm-pricing_plan-service_type_has_service'

Plan='tbl_stu_adm-pricing_plan-plan'

Plan_Has_Service='tbl_stu_adm-pricing_plan-plan_has_service'

Subject='tbl_stu_adm-pricing_plan-subject'

Service_Has_Subject='tbl_stu_adm-pricing_plan-service_has_subject'

Book='tbl_stu_adm-pricing_plan-book'

Subject_Has_Book='tbl_stu_adm-pricing_plan-subject_has_book'

Book_Type='tbl_stu_adm-pricing_plan-book_type'

Book_Type_Has_Book='tbl_stu_adm-pricing_plan-book_type_has_book'

JWT_API_Authentication='tbl_stu_adm-stu_user_site_jwt_api_auth'

Writing_Test_Name='tbl_study_content-writing_test_name'

Writing_Test_Student_Admin='tbl_study_content-writing_test_stu_admin'

Writing_Test_Student_User='tbl_study_content-writing_test_stu_user'

MCQ_Test_Name='tbl_study_content-mcq_test_name'

MCQ_Test_Student_Admin='tbl_study_content-mcq_test_stu_admin'

MCQ_Test_Student_User='tbl_study_content-mcq_test_stu_user'

Video_Topic='tbl_study_content-video_topic'

Video='tbl_study_content-video'

Audio_Topic_Student_Admin='tbl_study_content-audio_topic_stu_admin'

Audio_Student_Admin='tbl_study_content-audio_stu_admin'

Audio_Topic_Student_User='tbl_study_content-audio_topic_stu_user'

Audio_Student_User='tbl_study_content-audio_stu_user'

PDF_Book='tbl_study_content-pdf_book'

PDF_Book_Chapter='tbl_study_content-pdf_book_chapter'

PDF_Book_Lesson='tbl_study_content-pdf_book_lesson'

PDF_Book_Chapter_Lesson='tbl_study_content-pdf_book_chapter_lesson'

PDF_Book_Lesson_Content='tbl_study_content-pdf_book_lesson_content'

PDF_Book_Page_Content='tbl_study_content-pdf_book_page_content'

PDF_Book_Page_Picture='tbl_study_content-pdf_book_page_picture'

PDF_PDFtron='tbl_study_content-pdf_pdftron'


#===============================Message========================================#

create_message='successfully created' 

update_message='successfully Updated'

delete_message='successfully deleted'

login_again='Successfully Reset your password please login again'

premium_plan_login_again='Successfully Buy This Plan, please login again'
 
Service_Buy_message='Successfully Buy this Service, Check it on My service'

"""
# 
create_mcqtest='/mcqtest/create'
get_all_mcqtest='/mcqtest/all'
get_one_mcqtest='/mcqtest/one/{id}'
update_mcqtest='/mcqtest/update/{id}'
destroy_mcqtest='/mcqtest/delete/{id}'
get_subject_mcqtest='/mcqtest/all/subject/{id}'
get_book_mcqtest='/mcqtest/all/book/{id}'

create_plan_service         = '/pricing_plan/plan_service/create'
get_all_plan_service        = '/pricing_plan/plan_service/all'
get_one_plan_service        = '/pricing_plan/plan_service/one/{id}'
update_plan_service         = '/pricing_plan/plan_service/update/{id}'
delete_plan_service         = '/pricing_plan/plan_service/delete/{id}'

# 
create_mcqanswer='/mcqanswer/create'
get_all_mcqanswer='/mcqanswer/all'
get_one_mcqanswer='/mcqanswer/one/{id}'
update_mcqanswer='/mcqanswer/update/{id}'
destroy_mcqanswer='/mcqanswer/delete/{id}'
get_subject_mcqanswer='/mcqanswer/all/subject/{id}'
get_book_mcqanswer='/mcqanswer/all/book/{id}'

# 
create_study_mcq='/study_mcq/create'
get_study_mcq='/study_mcq/all'
get_one_study_mcq='/study_mcq/one/{id}'
update_study_mcq='/study_mcq/update/{id}'
destroy_study_mcq='/study_mcq/delete/{id}'

# 
create_course='/create'
get_all_courses='/all'
get_one_course='/one/{id}'
destroy_course='/delete/{id}'
update_course='/update/{id}'
update_status_course='/update_status/{id}'

# 
create_syllabus='/create'
update_syllabus='/update/{id}'
get_subject_syllabuses='/course/{id}'
get_one_subject_syllabus='/one/{id}'
get_syllabus_picture='/picture/{id}'

# 
create_exam_pattern='/create'
all_exam_pattern='/all'
subject_exam_pattern='/subject/{id}'
get_one_exam_pattern='/one/{id}'
update_exam_pattern='/update/{id}'
destroy_exam_pattern='/delete/{id}'

# 
create_board_writing_question='/writing_question_board/create'
create_institute_writing_question='/writing_question_institute/create'
all_writing_question='/writing_question/all'
get_one_writing_question='/writing_question/one/{id}'
update_writing_question='/writing_question/update/{id}'
destroy_writing_question='/writing_question/delete/{id}'
filter_board_writing_question='/writing_question/filter/board'
filter_institute_writing_question='/writing_question/filter/institute'

# 
create_board_mcq_question='/mcq_question_board/create'
create_institute_mcq_question='/mcq_question_institute/create'
all_mcq_question='/mcq_question/all'
get_one_mcq_question='/mcq_question/one/{id}'
update_mcq_question='/mcq_question/update/{id}'
destroy_mcq_question='/mcq_question/delete/{id}'
filter_board_mcq_question='/mcq_question/filter/board'
filter_institute_mcq_question='/mcq_question/filter/institute'

# 
create_option_mcq_questions='/option_mcq_questions/create'
all_option_mcq_questions='/option_mcq_questions/all'
get_bank_option_mcq_questions='/option_mcq_questions/bank/{id}'
get_one_option_mcq_questions='/option_mcq_questions/one/{id}'
update_option_mcq_questions='/option_mcq_questions/update/{id}'
destroy_option_mcq_questions='/option_mcq_question/delete/{id}'

# 
create_subscription_has_course='/subscription_has_course/create'
get_all_subscription_has_course='/subscription_has_course/all'
get_one_subscription_has_course='/subscription_has_course/one/{id}'
update_subscription_has_course='/subscription_has_course/update/{id}'
destroy_subscription_has_course='/subscription_has_course/delete/{id}'
get_subscription_has_course='/subscription_has_course/subscription_id/{id}'


# 
create_speech_and_audio='/create'
get_all_speech_and_audio='/all'
get_one_speech_and_audio='/one/{id}'
update_speech_and_audio='/update/{id}'
destroy_speech_and_audio='/delete/{id}'
get_user_speech_and_audio='/one/user/'


# 
create_course_video='/create'
get_all_course_video='/all'
get_one_course_video='/one/{id}'
update_course_video='/update/{id}'
destroy_course_video='/delete/{id}'
get_subject_course_video='/all/subject/{id}'


# 
create_writing_test='/create'
get_all_writing_test='/all'
get_one_writing_test='/one/{id}'
update_writing_test='/update/{id}'
destroy_writing_test='/delete/{id}'
get_user_writing_test='/one/user/'

#==============
create_shipping_adress      = '/shipping/create'
get_all_shipping_adress     = '/shipping/all'
get_one_shipping_adress     = '/shipping/one/{id}'
update_shipping_adress      = '/shipping/update/{id}'
destroy_shipping_adress     = '/shipping/delete/{id}'

#address_type
create_typesofaddress       = '/service/create_typesofservice'
get_all_typesofaddress      = '/service_typesofservice/all'
get_one_typesofaddress      = '/service_typesofservice/one/{id}'
update_typesofaddress       = '/service_typesofservice/update/{id}'
delete_typesofaddress       = '/service_typesofservice/delete/{id}'

# card has billing:
create_card_has_billing     = '/card_billing/create'
get_all_card_has_billing    = '/card_billing/all'
get_one_card_has_billing    = '/card_billing/one/{id}'
update_card_has_billingn    = '/card_billing/update/{id}'
destroy_card_has_billing    = '/card_billing/delete/{id}'
get_all_card_billing        = '/card_billing/all'

# shipping:
create_card_has_shipping    = '/card_shipping/create'
get_all_card_has_shipping   = '/card_shipping/all'
get_one_card_has_shipping   = '/card_shipping/one/{id}'
update_card_has_shipping    = '/card_shipping/update/{id}'
destroy_card_has_shipping   = '/card_shipping/delete/{id}'
get_all_card_shipping       = '/card_shipping/all'

# card_billing_shipping
create_card_has_card_has_shopping_billing   = '/card_has_shopping_billing/create'
get_all_card_card_has_shopping_billing      = '/card_has_shopping_billing/all'
get_one_card_has_shopping_billing           = '/card_has_shopping_billing/one/{id}'
update_card_has_shopping_billing            = '/card_has_shopping_billing/{id}'
destroy_card_has_shopping_billing           = '/card_has_shopping_billing/{id}'
get_all_card_has_shopping_billing           = '/card_has_shopping_billing/all'



# ====
create_groups_esj           = '/groups_esj/create'
get_all_groups_esj          = '/groups_esj/all'
update_groups_esj           = '/groups_esj/update/{id}'
destroy_groups_esj          = '/groups_esj/delete/{id}'


# user role group
create_esjusers_role_group_permission   = '/esjusers_role_group_permission/create'
get_all_esjusers_role_group_permission  = '/esjusers_role_group_permission/all'
get_one_esjusers_role_group_permission  = '/esjusers_role_group_permission/one/{id}'
update_esjusers_role_group_permission   = '/esjusers_role_group_permission/update/{id}'
delete_esjusers_role_group_permission   = '/esjusers_role_group_permission/delete/{id}'

create_user_has_permission_role_group   = '/esjusers_user_has_permission_role_group/create'
"""


from django.core.exceptions import ValidationError 


'National Id Validation Function'
def validate_national_id(value):
    invalid_list = ["0000000000","1111111111",
                    "2222222222","3333333333",
                    "4444444444","5555555555",
                    "6666666666","7777777777",
                    "8888888888","9999999999"]
    if len(value)==10:
        sum = 0
        if ' ' in value:
            raise ValidationError("Space is Not Allowed in N-ID")
        if value in invalid_list:
            raise ValidationError("All Numbers Cant be the Same, Enter valid N-ID")
        for index, item in enumerate(value):
            if index!=9:  
                number = int(item)
                multiplied = (number*(10-index))
                sum = (sum + multiplied)
            else:
                control_num = int(item)
                reminder = (sum % 11)
                if reminder < 2:
                    if reminder == control_num:
                        return value
                    else:
                        raise ValidationError("Entered ID is not valid, Enter valid N-ID(remainder is lower state {})".format(reminder))    
                else:
                    modified_reminder = (11-reminder)
                    if control_num == modified_reminder:
                        return value
                    else:
                        raise ValidationError("Entered ID is not valid, Enter valid N-ID(remainder is bigger state {})".format(reminder)) 
            
    else:
        raise ValidationError("Please Inter Valid N-ID(the ID should contain Exactly 10 number)")



def restrict_class_amount(value):
    'We want to have only one physical class(Location) for now, But not for future'
    if ClassHolding.objects.filter(PhysicalClass_id=value).count() >= 2:
        raise ValidationError('For Now you can just have one Physical Location for the class')

    
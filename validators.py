NEGATIVE_FIELD_ERROR = 'are invalid. Input should be a non-negative number'
REQUIRED_FIELD_ERROR = 'are required'

# This function takes invalid or missing POST request fields and generates a readable error message
# that can be send as response.
def error_message(error_fields, error_type_msg):
    error_msg = ''

    if len(error_fields) == 1:
        error_msg = '{} field {}.'.format(error_fields[0], error_type_msg).replace('are', 'is')
        return error_msg

    elif len(error_fields) > 1:
        for index, fm in enumerate(error_fields):
            if index != 0 and index == len(error_fields) - 1:
                error_msg = error_msg[:len(error_msg)-2] + ' & {} fields {}.'.format(fm, error_type_msg)
            else:
                error_msg = error_msg + '{}, '.format(fm)
        return error_msg


'''
This class has different validation methods that are used to validate POST request data.
For complex credit policies more validation methods can be added here as per our requirements.
And can also be used easily in our service(s).
'''
class Validators:

    # This method is used check if all the required fields exist in POST Request Data.
    def required(data, fields):
        missing_fields = []

        for f in fields:
            value = str(data.get(f, ''))
            if len(value) == 0:
                missing_fields.append(f)           

        if len(missing_fields):
            error_msg = error_message(missing_fields, REQUIRED_FIELD_ERROR)
            raise ValueError(error_msg)

        return True

    # This method is used to check if all the fields have numberic and non-negative values in POST Request Data.
    def invalid(data, fields):        
        invalid_fields = []
        
        for f in fields:
            try:
                if int(data[f]) < 0:
                    invalid_fields.append(f)
            except:
                    invalid_fields.append(f)

        if len(invalid_fields):
            error_msg = error_message(invalid_fields, NEGATIVE_FIELD_ERROR)
            raise ValueError(error_msg)

        return True


    
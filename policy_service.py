from base_service_class import BaseServiceClass
from validators import Validators
from run_server import run_server


class PolicyService(BaseServiceClass):

    # All Fields
    fields = [
            "customer_income",
            "customer_debt",
            "payment_remarks_12m",
            "payment_remarks",
            "customer_age"
        ]

    # All Required Fields - That must be in the POST request data.
    required_fields = [
            "customer_income",
            "customer_debt",
            "payment_remarks_12m",
            "payment_remarks",
            "customer_age"
        ]

    # POST Request Method
    def post(self):
        try:
            request_data = self.request_data()
            if Validators.required(request_data, self.required_fields) and Validators.invalid(request_data, self.fields): 
                response = self.credit_eligibility(request_data)
                #response = self.credit_eligibility_v2(request_data)
                if response['status'] == 'ACCEPT':
                    self.success_response(status= response['status'])
                else:
                    self.error_response(status= response['status'], reason=response['reason'])

        except ValueError as error:
            self.error_response(status='REJECT', reason='INVALID_INPUT', message=str(error))


    '''
    Method that evaluates credit eligibility against the POST request data.
    NOTE: This function returns only one rejection reason against the first condition that fails.
    '''
    def credit_eligibility(self, data):
        if data['customer_income'] < 500:
            return {'status': 'REJECT', 'reason': 'LOW_INCOME'}

        if data['customer_debt'] > data['customer_income']/2:
            return {'status': 'REJECT', 'reason': 'HIGH_DEBT_FOR_INCOME'}

        if data['payment_remarks_12m'] > 0:
            return {'status': 'REJECT', 'reason': 'PAYMENT_REMARKS_12M'}

        if data['payment_remarks'] > 1:
            return {'status': 'REJECT', 'reason': 'PAYMENT_REMARKS'}

        if data['customer_age'] < 18:
            return {'status': 'REJECT', 'reason': 'UNDERAGE'}

        return {'status': 'ACCEPT'}
        

    '''
    Method that evaluates credit eligibility against the POST request data.
    NOTE: This function returns only all the rejection reasons against all the conditions that fail.
    '''
    def credit_eligibility_v2(self, data):
        rejection_reasons = []

        if data['customer_income'] < 500:
            rejection_reasons.append('LOW_INCOME')

        if data['customer_debt'] > data['customer_income']/2:
            rejection_reasons.append('HIGH_DEBT_FOR_INCOME')

        if data['payment_remarks_12m'] > 0:
            rejection_reasons.append('PAYMENT_REMARKS_12M')

        if data['payment_remarks'] > 1:
            rejection_reasons.append('PAYMENT_REMARKS')

        if data['customer_age'] < 18:
            rejection_reasons.append('UNDERAGE')

        if len(rejection_reasons):
            return {'status': 'REJECT', 'reason': rejection_reasons}

        return {'status': 'ACCEPT'}


IP = '127.0.0.1'
PORT = 8000

if __name__ == "__main__":
    run_server(PolicyService, IP, PORT)


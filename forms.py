from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, DateTimeField



class Addsales(FlaskForm):

    item_code = SelectField('Item Code:',
                                choices=[('P1','PROD_001'), ('P2','PROD_002'), ('P3','PROD_003'), ('P4','PROD_004'), ('P5','PROD_005'), ('P6','PROD_006'), ('P7','PROD_008'), ('P4','PROD_008'),
                                        ('ESP1','ESP_001'), ('ESP2','ESP_002'), ('ESP3','ESP_003'), ('ESP4','ESP_004'), ('ESP','ESP_005'), ('ESP','ESP_006'), ('ESP','ESP_008'), ('ESP','ESP_008')])
    emp_id = SelectField('Employee Id:',
                                choices=[('emp1','EMP234'), ('emp2','EMP244'), ('emp3','EMP256'), ('emp4','EMP267'), ('emp5','EMP290')])
    quantity = IntegerField('Quantity:')
    sales_entry_date = DateTimeField('Date:')
    submit = SubmitField('Save')

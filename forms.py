from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, DateField, StringField



class Addsales(FlaskForm):

    item_code = SelectField(u'Item Code:', choices=[('PROD_001','PROD_001'), ('PROD_002','PROD_002'), ('PROD_003','PROD_003'), ('PROD_004','PROD_004'), ('PROD_005','PROD_005'), ('PROD_006','PROD_006'), ('PROD_007','PROD_007'), ('PROD_008','PROD_008'),
                                        ('ESP_001','ESP_001'), ('ESP_002','ESP_002'), ('ESP_003','ESP_003'), ('ESP_004','ESP_004'), ('ESP_005','ESP_005'), ('ESP_006','ESP_006'), ('ESP_008','ESP_008'), ('ESP_008','ESP_008')])
    emp_id = SelectField(u'Employee Id:',
                                           choices=[('EMP234','EMP234'), ('EMP244','EMP244'), ('EMP256','EMP256'), ('EMP267','EMP267'), ('EMP290','EMP290')])
    quantity = StringField('Quantity:')
    sales_entry_date = DateField('Date:')
    submit = SubmitField('Add')

class Delsales(FlaskForm):

    id = IntegerField('Sales Id to be removed:')
    submit = SubmitField('Remove')
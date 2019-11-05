from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class TaskSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'deadline')

class ParamsTaskSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=50))
    description = fields.Str(required=True, validate=Length(max=200))
    deadline = fields.DateTime(required=True)

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

params_task_schema = ParamsTaskSchema()
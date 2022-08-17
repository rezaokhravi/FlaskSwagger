from flask import Blueprint
from flask_restx import Api
from .evaluatesService import api as evaluatesService  
from .personsService import api as personsService  



apis = Api(title="Evaluation Apis", version="1.0", description="This is a testing apis auth by R.okhravi",prefix='/api/')


apis.add_namespace(evaluatesService)

apis.add_namespace(personsService)
from flask import jsonify
from flask_restful import Resource, request
from models.app import AppModel
from datetime import date
import json

# Resource = External representation (this is what the client talk with)
# Here we communicate with the database
class App(Resource):
    def get(self, _id):
        app = AppModel.find_by_id(_id)
        if app:
            return app.json()
        return {'message': 'App not found'}, 404

    def post(self, _id):
        all_data = request.data
        json_data = None
        if all_data:
            json_data = json.loads(all_data)
        print(str(json_data))
        if AppModel.find_by_id(_id): # First make sure app is not exist - if it's exist just add +1, otherwise create it
            if json_data:
                too = json_data['too']
                if too:
                    pa = json_data['pa']
                    mes = json_data['mes']
                    updated_app = (AppModel.update_app(_id, too, pa, mes)) # download only
                else:
                    updated_app = (AppModel.add_download(_id)) # download only
            else:
                updated_app = (AppModel.add_download(_id))  # download only
            try:
                updated_app.save_to_db()
            except Exception as ex:
                print(ex)
                return {"message": "An error occurred creating the app."}, 500
            return updated_app.json(), 201
            #return {'message': "An app with id '{}' already exists".format(_id)}, 400

        today = date.today()
        print("Today's date:", today)
        app = AppModel(_id, today, 1, False, "", "")
        try:
            app.save_to_db()
        except Exception as ex:
            print(ex)
            return {"message": "An error occurred creating the app."}, 500
       # return jsonify({'app': app})
        return app.json(), 201

    def delete(self, _id):
        app = AppModel.find_by_id(_id)
        if app:
            app.delete_from_db()
            return {'message': 'App deleted'}
        else:
            return {'message': 'App not found'}

class AppList(Resource):
    def get(self):
        return {'apps': list(map(lambda x: x.json(), AppModel.query.all()))}
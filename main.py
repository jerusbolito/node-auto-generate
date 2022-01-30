"""
Imports
"""
import os
import json
# First step - loop through files in json_models
dir_name = os.path.dirname(__file__)
model_path = os.path.join(dir_name, "json_models")
templates_path = os.path.join(dir_name, "js_templates")

def initialize_directory(project):
    """
    Initialize models, controllers, and routes directory for the JavaScript project
    """
    output_folder = os.path.join(dir_name, "output")
    folders_to_create = ["models", "controllers", "routes"]
    for folder in folders_to_create:
        try:
            folder_path = os.path.join(output_folder, project, folder)
            os.makedirs(folder_path)
        except FileExistsError:
            print(f"Skipped creating {folder} folder as it already exists.")

def create_schema(schema_name, schema_val, project):
    """
    Create the schema for each models provided in the json_models folder
    """
    model_template_path = os.path.join(templates_path, "model.temp.txt")
    model_template = open(model_template_path)
    lines_to_write = []
    for line in model_template.readlines() :
        new_text = line.replace("{{schema_name}}", schema_name)
        new_text = new_text.replace("{{schema_val}}", schema_val)
        lines_to_write.append(new_text)
    models_folder = os.path.join(dir_name, "output", project, "models")
    schema_file = open(os.path.join(models_folder, f"{schema_name}.model.js"), "w")
    schema_file.writelines(lines_to_write)

def create_controllers(schema_name, project):
    """
    Create the controller for each file provided in the json_models folder
    """
    controller_template_path = os.path.join(templates_path, "controller.temp.txt")
    controller_template = open(controller_template_path)
    lines_to_write = []
    for line in controller_template.readlines():
        new_text = line.replace("{{model_var}}", schema_name)
        new_text = new_text.replace("{{model_path}}", f"../models/{schema_name}.js")
        lines_to_write.append(new_text)
    controllers_folder = os.path.join(dir_name, "output", project, "controllers")
    controller_file = open(os.path.join(controllers_folder, f"{schema_name}.controller.js"), "w")
    controller_file.writelines(lines_to_write)

def create_routes(schema_name, project):
    """
    Create the route for each file provided in the json_models folder
    """
    router_template_path = os.path.join(templates_path, "router.temp.txt")
    router_template = open(router_template_path)
    lines_to_write = []
    for line in router_template.readlines():
        new_text = line.replace("{{controller_path}}", \
        f"../controllers/{schema_name}.controller.js")
        lines_to_write.append(new_text)
    routers_folder = os.path.join(dir_name, "output", project, "routes")
    router_file = open(os.path.join(routers_folder, f"{schema_name}.route.js"), "w")
    router_file.writelines(lines_to_write)

project_name = input("Enter the project name: ")
initialize_directory(project_name)
for file in os.listdir(model_path):
    new_path = os.path.join(model_path, file)
    json_file = open(new_path)
    json_data = json.load(json_file)
    model_name = json_data["Name"]
    print(model_name)
    SCHEMA_VAL = "{"
    for key, val in json_data["Values"].items():
        SCHEMA_VAL += f"\n{key}:{val},"
    SCHEMA_VAL += "\n}"
    print(SCHEMA_VAL)
    create_schema(model_name, SCHEMA_VAL, project_name)
    create_controllers(model_name, project_name)
    create_routes(model_name, project_name)

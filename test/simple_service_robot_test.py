import os
import yaml
from task_planner.lama_interface import LAMAInterface

if __name__ == '__main__':
    with open('../config/planner_config.yaml', 'r') as config_file:
        planner_config = yaml.safe_load(config_file)
        domain_file = os.path.join(planner_config['domain_path'], 'service_robot_domain.pddl')
        planner_cmd = planner_config['planner_cmd']
        plan_file_path = planner_config['plan_file_path']

        state_fluents = [('robotName', [('Robot', 'MyRobot')], 'true'),
                         ('robotAt', [('Robot', 'MyRobot')], 'Kitchen'),
                         ('planeAt', [('Plane', 'CoffeeTable')], 'LivingRoom'),
                         ('planeAt', [('Plane', 'DiningTable')], 'DiningRoom'),
                         ('objectOnPlane', [('Object', 'WaterBottle')], 'CoffeeTable'),
                         ('objectOnPlane', [('Object', 'CoffeeMug')], 'CoffeeTable'),
                         ('objectOnPlane', [('Object', 'MySoupPlate')], 'DiningTable'),
                         ('unexplored', [('Plane', 'CoffeeTable')], 'true'),
                         ('emptyGripper', [('Robot', 'MyRobot')], 'true')]

        planner_interface = LAMAInterface('test_kb', domain_file, planner_cmd, plan_file_path, debug=True)
        planner_interface.kb_interface.insert_fluents(state_fluents)

        task_goals = [('objectOnPlane', [('Object', 'WaterBottle')], 'DiningTable'),
                      ('emptyGripper', [('Robot', 'MyRobot')], 'true')]
        plan_found, plan = planner_interface.plan('MyRobot', task_goals)

        planner_interface.kb_interface.remove_fluents(state_fluents)
        planner_interface.kb_interface.db_client.drop_database('test_kb')
